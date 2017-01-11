from picamera import PiCamera
from time import sleep
import csv
from testpolly import make_audio


camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

import boto3

    

s3= boto3.client('s3')

s3.upload_file("/home/pi/Desktop/image.jpg","bonbon10", "image.jpg")

client = boto3.client('rekognition')

response = client.detect_labels(
    Image={
        'S3Object':{
            'Bucket': 'bonbon10',
            'Name': 'image.jpg'
            }
        }
)


#Import things to filter
#fileThings = open("/home/pi/Desktop/things.csv")
#thingData = csv.reader(fileThings)
#print(thingData)

#Find all the things in the picture
things = []
for d in response['Labels']:
    if (d['Confidence'] > 80):
        things.append((d['Confidence'],d['Name']))

#Sort all the in terms of accuracy
things.sort(reverse = True)

if len(things) >= 2:
    print("Two things with highest accuracy: ")
    print(things[0][1],things[1][1])
elif len(things) == 1:
    print(things[0][1])
else:
    print("nothing detected!")


make_audio('fdsfsfsdfsdfsdf')

