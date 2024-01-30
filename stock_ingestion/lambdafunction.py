import json
import base64
from pprint import pprint
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    dynamodb_res = boto3.resource('dynamodb', region_name='us-east-2')
    print(event)
    result = 0

    
    for record in event['Records']:
        print(record)
        payload = base64.b64decode(record['kinesis']['data'])
        payload = str(payload, 'utf-8')
        print('payload check here', payload) 
        pprint(payload, sort_dicts=False)
        
        payload_std = payload.replace('Timestamp', 'Timestamp').replace('stock', 'Stock').replace('Close', 'Close').replace('fiftyTwoWeekLow', 'fiftyTwoWeekLow').replace('fiftyTwoWeekHigh', 'fiftyTwoWeekHigh')  
        
        try:
            payload_rec = json.loads(payload_std, parse_float=Decimal)
            print('coming here')
            pprint(payload_rec, sort_dicts=False)
            
            Timestamp = payload_rec['Timestamp']
            stock = payload_rec['Stock']
            close_value = payload_rec['Close']
            fifty_two_week_low = payload_rec['fiftyTwoWeekLow']
            fifty_two_week_high = payload_rec['fiftyTwoWeekHigh']
            
            if close_value >= (fifty_two_week_high / Decimal(1.2)) or close_value <= (fifty_two_week_low * Decimal(1.2)):
                
                if close_value >= (fifty_two_week_high / Decimal(1.2)):
                    payload_rec['flag'] = 'Stock is near the fifty two week high'
                else:
                    payload_rec['flag'] = 'Stock is near the fifty two week low'
                    
                table = dynamodb_res.Table('poitable')
                response = table.put_item(Item=payload_rec)
                print('Item added to DynamoDB table')
                    
                client = boto3.client('sns', region_name='us-east-2')
                topic_arn = "arn:aws:sns:us-east-2:728146017015:cloudprojsns"
                snsmessgae = payload_rec['flag'] + ' for ' + stock
                    
                try:
                    client.publish(TopicArn=topic_arn, Message=snsmessgae, Subject="POI is created for the stock")
                    result = 1
                except Exception:
                    result = 0
    
        except ValueError as e:
            print('JSON conversion error:', str(e))
            print('Invalid JSON payload:', payload)
            
    return result