import paho.mqtt.client as mqtt
import json
import time

count = [0, 0]
summ = [0, 0]
x = []
y = []

# 連線伺服器得到回應要進行的動作
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Rule/#")

# 當接收訊息時要進行的動作
def on_message(client, userdata, msg):
    t = time.time()
    #print(msg.topic+" "+ msg.payload.decode('utf-8'))

    data = json.loads(msg.payload.decode('utf-8'))
    data["ReceiveTime"] = t
    timeLag(data["ReceiveTime"], data["SensorTime"])


def timeLag(Rt, St):
    rt = Rt - St

    count[0] += 1
    summ[0] += rt
    summ[1] += rt
    print(count[0], ':', rt)

    x.append(count[0])
    y.append(rt)
    # print(x)
    # print(y)

    if count[0] % 10 == 0:
        avg = summ[0] / count[0] 
        print(count[0] , 'S_avg =', avg)
        print(x)
        print(y)

    # if count[0] % 1 == 0:
    #     avg10.append(summ[1] / 1)
    #     summ[1] = 0

def avg1000(summ, count, x ,y):
    avg = summ / count
    print('10s_10 avg = ', avg)
    # print('10s avg = ', avg10)

    # f = open("10s_10.txt", "w+")
    # f.write(str(x)+'\n')
    # f.write(str(y)+'\n')
    # f.close()

def tryy(Rt, St):
    rt = Rt - St

    count[1] += 1
    summ[1] += rt
    print('s1 10KB : ',count[1], ' : ', rt)

    if count[1] % 10 == 0:
        avg = summ[1] / count[1]
        print('s1 10KB : 10s_10 avg = ', avg)


# 連線設定
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.connect("192.168.50.38", 1883, 60)
client.connect("130.211.254.228", 1883, 60)
client.loop_forever()
