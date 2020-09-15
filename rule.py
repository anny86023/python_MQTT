import paho.mqtt.client as mqtt
import json
import time

# 連線伺服器得到回應要進行的動作
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Sensor/#")

# 當接收訊息時要進行的動作
def on_message(client, userdata, msg):
    #print(msg.topic+" "+ msg.payload.decode('utf-8'))
    t1 = time.time()

    data = rule_S2(json.loads(msg.payload.decode('utf-8')), t1)
    client.publish('Rule', json.dumps(data))

# Rule
def rule_S1(data, t1):
    heartbeat = data["HeartBeat"]
    data["RuleTime"] = t1

    #print('Rule_1 S1 - Text len: ',len(data["Text"]))
    if heartbeat > 100:
        return data

def rule_S2(data, t1):
    #print('Rule_1 S2 - Text len: ',len(data["Text"]))
    data["RuleTime"] = t1
    return data

# 連線設定
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("0.0.0.0", 1883, 60)
#client.connect("192.168.50.11", 1883, 60)
#client.connect("ssh.tenoz.tw", 1883, 60)
client.loop_forever()


'''
# 連線設定
client1 = mqtt.Client()
client1.on_connect = on_connect
client1.on_message = on_message
client1.connect("0.0.0.0", 1883, 60)

client2 = mqtt.Client()
client2.on_connect = on_connect
client2.connect("ssh.tenoz.tw", 1883, 60)

client1.loop_forever()
client2.loop_forever()
'''