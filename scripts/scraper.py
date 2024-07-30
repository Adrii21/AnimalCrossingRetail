import requests
from bs4 import BeautifulSoup
import json
from confluent_kafka import Producer

# Kafka producer configuration 
conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(**conf)

# callback for message delivery
def delivery_report(err, msg):
    if err is not None:
        print('Error al enviar el mensaje: {}'.format(err))
    else:
        print('Mensaje enviado a {} [{}]'.format(msg.topic(), msg.partition()))

# web scrap
url = "https://nookipedia.com/wiki/Furniture/New_Horizons/Housewares"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# parsing info
items = []
table = soup.find('table', {'class': 'sortable'})
 # Ignore table header
for row in table.find_all('tr')[1:]: 
    columns = row.find_all('td')
    if len(columns) > 0:
        image_tag = columns[2].find('img')
        item = {
            'name': columns[1].text.strip(),
            'image': image_tag['src'].strip() if image_tag else None,
            'buy_price': columns[3].text.strip(),
            'source': columns[5].text.strip(),
            'theme': columns[6].text.strip(),
            'category': columns[7].text.strip(),
            'customizable': columns[8].text.strip(),
        }
        items.append(item)

# Sending data to kafka
for item in items:
    producer.produce('scraped-data', key=item['name'], value=json.dumps(item), callback=delivery_report)
    producer.poll(0)

producer.flush()
