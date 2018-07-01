# mcdemo parser

import json
import datetime
import time

print('Loading function')

def lambda_handler(event, context):
    
    print("Received event: " + json.dumps(event, indent=2))
    
    deviceid = json.dumps(event['device']).strip('"')                   # device id
    temp = float.fromhex('0x' + json.dumps(event['data']).strip('"'))   # data
    message_timestamp = json.dumps(event['time']).strip('"')            # message timestamp
    message_datetime = datetime.datetime.utcfromtimestamp(int(message_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    snr = json.dumps(event['snr']).strip('"')                           # snr of message
    station = json.dumps(event['station']).strip('"')                   # base station of message
    avgsnr = json.dumps(event['avgSnr']).strip('"')                     # average snr
    lat = json.dumps(event['lat']).strip('"')                           # base station lat
    lng = json.dumps(event['lng']).strip('"')                           # base station lng
    rssi = json.dumps(event['rssi']).strip('"')                         # rssi of message
    seqnumber = json.dumps(event['seqNumber']).strip('"')               # seq number of message
    timestamp = int(time.time() * 1000)                                 # created at timestamp
    

    item = {
        'deviceid': str(deviceid),
        'temperature': str(temp),
        'message_timestamp': str(message_timestamp),
        'message_datetime': str(message_datetime),
        'snr': str(snr),
        'station': str(station),
        'avgsnr': str(avgsnr),
        'lat': str(lat),
        'lng': str(lng),
        'rssi': str(rssi),
        'seqnumber': str(seqnumber),
        'timestamp': str(timestamp)
    }

    return json.dumps(item)
