import pprint
import threading
import pymongo
import random
import time


# Function to generate temperature between 30 C° and 40 C°
def gerar_temp():
    return random.uniform(30, 40)


# Function to generate and store information in MongoDB:
def sensor(nome_sensor, tempoExecucao, collection):
    while True:
        temperatura = gerar_temp()
        print(f"{nome_sensor}: {temperatura:.2f}°C")
        document = {
            "nomeSensor": nome_sensor,
            "valorSensor": temperatura,
            "unidadeMedida": "C°",
            "sensorAlarmado": False
        }

        collection.replace_one({"nomeSensor": nome_sensor}, document, upsert=True)
        print(f"document {nome_sensor} successfully added!")

        # Sensor alarmed:
        if temperatura > 38:
            print(f"Atenção! Temperatura muito alta! Verificar {nome_sensor}!")
            collection.update_one({"nomeSensor": nome_sensor}, {"$set": {"sensorAlarmado": True}})
            print(f"document {nome_sensor} updated successfully!")
            break
        else:
            time.sleep(tempoExecucao)


# Create the MongoDB connection and select the appropriate database and collection:
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bancoiot"]
collection = db["sensores"]

# Create the threads to simulate the sensors:
thread1 = threading.Thread(target=sensor, args=("Sensor1", 5, collection))
thread2 = threading.Thread(target=sensor, args=("Sensor2", 10, collection))
thread3 = threading.Thread(target=sensor, args=("Sensor3", 15, collection))

# Start the threads:
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish:
thread1.join()
thread2.join()
thread3.join()

# Presenting information:
print("\n")
results = collection.find()
for information in results:
    pprint.pprint(information)
