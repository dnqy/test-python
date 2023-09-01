from influxdb_client import WritePrecision, InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

bucket = 'test'
org = 'myorg'
token = 'myadmintoken'
# Store the URL of your InfluxDB instance
url='http://influxdb:8086'

client = InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Write script
write_api = client.write_api(write_options=SYNCHRONOUS)

p = Point('my_measurement').tag('location', 'raspberry01').\
field('temperature', 25.3).field('humidity', 45.0).\
time(datetime.utcnow(), WritePrecision.MS)

write_api.write(bucket=bucket, org=org, record=p)