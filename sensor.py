import paho.mqtt.client as mqtt
import random
import json
import time
import threading

# 連線設定
client = mqtt.Client()
# client.connect("192.168.50.38", 1883, 60)
client.connect("130.211.254.228", 1883, 60)
client.loop_start()

# sensor 產生資料
# ISOTIMEFORMAT = '%m/%d %H:%M:%S.%f'

def random_text(data_size):
    size = round(data_size * 1024)
    text = '1' * size
    return text

def Sensor():
    while True:
        # ### Sensor2_ARedu
        text = random_text(102400) # 100Mb
        print('S2 - Text len: ',len(text))
        t = time.time()
        payload = {'S' : 'S2', 'Text' : text, 'SensorTime' : t}
        client.publish("Sensor/S2", json.dumps(payload))
        time.sleep(10)

# 建立子執行緒
threads = []
for i in range(1):
    threads.append(threading.Thread(target = Sensor))
    threads[i].start()

# while True:

    # ### Sensor1_heartbest
    # text = random_text(0.01) #10 byte 
    # # print('S1 - Text len: ',len(text))
    # heartbeat = random.randint(101,150)
    # t = time.time()
    # payload = {'HeartBeat' : heartbeat, 'Text' : text, 'SensorTime' : t}
    # client.publish("Sensor/S1", json.dumps(payload))
    # time.sleep(1)

# --------------------------------------------------

    # ### Sensor2_ARedu
    # text = random_text(102400) # 100Mb
    # # print('S2 - Text len: ',len(text))
    # t = time.time()
    # payload = {'S' : 'S2', 'Text' : text, 'SensorTime' : t}
    # client.publish("Sensor/S2", json.dumps(payload))
    # time.sleep(10)

 # --------------------------------------------------

    # ### Sensor3_surgery
    # text = random_text(10) #10KB
    # #print('S3 - Text len: ',len(text))
    # t = time.time()
    # payload = {'Text' : text, 'SensorTime' : t}
    # client.publish("Sensor/S3", json.dumps(payload))
    # time.sleep(1)

 # --------------------------------------------------


''' 
Sensor4_temperature
Sensor5_Xray
Sensor6_ARsurgery
'''