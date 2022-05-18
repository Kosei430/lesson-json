# 課題1
import json

with open('data/sensor.json', 'r', encoding='utf-8_sig') as f:
    df = json.load(f)
    print(df["sensordata"]["accel"])
    print(df["sensordata"]["light"]["light"])
    print(df["sensordata"]["touch"][0]["x"])
    print(df["sensordata"]["touch"][0]["y"])
    print(df["sensordata"]["touch"][1]["x"])
    print(df["sensordata"]["touch"][1]["y"])
    print(df["timestamp"])
