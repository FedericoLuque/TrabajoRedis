#Ejecutar docker run -d --name mi_redis -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
#Ejecutar docker exec -it mi_redis bash


import redis

# Conexion
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

# 1 - Crear registros clave-valor(0.5 puntos)

baseDatosRedis.set('barco_1', 'BlueWave')
baseDatosRedis.set('barco_2', 'OceanSweepers')
baseDatosRedis.set('barco_3', 'SeaGuardian')
baseDatosRedis.set('barco_4', 'AquaClean')
baseDatosRedis.set('barco_5', 'ClearSea')
baseDatosRedis.set('barco_6', 'WaveKeepers')
baseDatosRedis.set('barco_7', 'ClearSea')

# 2 - Obtener y mostrar el número de claves registradas (0.5 puntos)

num_claves = baseDatosRedis.dbsize()

# Mostrar el resultado
print(f"Número de claves en Redis: {num_claves}")

# 3 - Obtener y mostrar un registro en base a una clave (0.5 puntos)

barco_1 = baseDatosRedis.get('barco_1')

# Mostrar el resultado
print(f"Barco 1: {barco_1}")

# 4 - Actualizar el valor de una clave y mostrar el nuevo valor(0.5 puntos)

baseDatosRedis.set('barco_1', 'BlueWave 2.0')
barco_1 = baseDatosRedis.get('barco_1')

# Mostrar el resultado
print(f"Barco 1: {barco_1}")

# 5 - Eliminar una clave-valor y mostrar la clave y el valor eliminado(0.5 puntos)

baseDatosRedis.delete('barco_1')
barco_1 = baseDatosRedis.get('barco_1')

# Mostrar el resultado
print(f"Barco 1: {barco_1}")

# 6 - Obtener y mostrar todas las claves guardadas (0.5 puntos)

claves = baseDatosRedis.keys('*')

# Mostrar el resultado
print(f"Claves: {claves}")

# 7 - Obtener y mostrar todos los valores guardados(0.5 puntos)

valores = baseDatosRedis.mget(claves)

# Mostrar el resultado
print(f"Valores: {valores}")

# 8 - Obtener y mostrar varios registros con una clave con un patrón en común usando * (0.5 puntos)

claves = baseDatosRedis.keys('barco_*')

# Mostrar el resultado
print(f"Claves con *: {claves}")

# 9 - Obtener y mostrar varios registros con una clave con un patrón en común usando [] (0.5 puntos)

claves = baseDatosRedis.keys('barco_[2-6]')

# Mostrar el resultado
print(f"Claves de barcos del 2 al 6: {claves}")
print(f"Valores: {valores}")

# 10 - Obtener y mostrar varios registros con una clave con un patrón en común usando ? (0.5 puntos)

claves = baseDatosRedis.keys('barco_?')

# Mostrar el resultado
print(f"Claves de barcos con ?: {claves}")
print(f"Valores: {valores}")

# 11 - Obtener y mostrar varios registros y filtrarlos por un valor en concreto. (0.5 puntos)

claves = baseDatosRedis.keys('*')

# Filtrar por un valor en concreto
filtro = 'ClearSea'
claves_filtradas = [claves[i] for i in range(len(claves)) if valores[i] == filtro]

# Mostrar el resultado
print(f"Claves con el valor {filtro}: {claves_filtradas}")

# 12 - Actualizar una serie de registros en base a un filtro (por ejemplo aumentar su valor en 1 )(0.5 puntos)

# Actualizar los valores
for clave in claves:
    valor = baseDatosRedis.get(clave)  # Obtener el valor actual
    if "AquaClean" in valor:  # Filtrar por nombre de barco
        mod = valor.replace("AquaClean", "Perdido")  # Cambiar "AquaClean" por "Perdido"
        baseDatosRedis.set(clave, mod)  # Actualizar el valor

# Mostrar el resultado
valores = baseDatosRedis.mget(claves)
print(f"Valores actualizados: {valores}")

# 13 - Eliminar una serie de registros en base a un filtro (0.5 puntos)

# Eliminar los registros
for clave in claves:
    valor = baseDatosRedis.get(clave)  # Obtener el valor actual
    if "Perdido" in valor:  # Filtrar por nombre de barco
        baseDatosRedis.delete(clave)

# Mostrar el resultado
claves = baseDatosRedis.keys('*')
valores = baseDatosRedis.mget(claves)
print(f"Claves: {claves}")
print(f"Valores: {valores}")

# 14 - Crear una estructura en JSON de array de los datos que vayais a almacenar(0.5 puntos)

import json

# Crear la estructura en JSON
datos = {
    "barcos": [
        {"nombre": "BlueWave"},
        {"nombre": "OceanSweepers"},
        {"nombre": "SeaGuardian"},
        {"nombre": "AquaClean"},
        {"nombre": "ClearSea"},
        {"nombre": "WaveKeepers"}
    ]
}

# Convertir a JSON
datos_json = json.dumps(datos)

# Mostrar el resultado
print(f"Datos en JSON: {datos_json}")

# 15 - Realizar un filtro por cada atributo de la estructura JSON anterior (0.5 puntos)

# Filtrar por cada atributo
filtro = "AquaClean"
barcos = datos["barcos"]
barcos_filtrados = [barco for barco in barcos if filtro in barco["nombre"]]
print(f"Barcos con {filtro}: {barcos_filtrados}")

# 16 - Crear una lista en Redis (0.5 puntos)

# Crear la lista
baseDatosRedis.rpush('barcos', 'BlueWave')
baseDatosRedis.rpush('barcos', 'OceanSweepers')
baseDatosRedis.rpush('barcos', 'SeaGuardian')
baseDatosRedis.rpush('barcos', 'AquaClean')
baseDatosRedis.rpush('barcos', 'ClearSea')
baseDatosRedis.rpush('barcos', 'WaveKeepers')

#imprimir la lista
lista = baseDatosRedis.lrange('barcos', 0, -1)
print(f"Lista de barcos: {lista}")

# 17 - Obtener elementos de una lista con un filtro en concreto(0.5 puntos)

# Filtrar por un valor en concreto
filtro = 'ClearSea'
barcos_filtrados = [barco for barco in lista if filtro in barco]
print(f"Barcos con {filtro}: {barcos_filtrados}")

# 18 - En Redis hay otras formas de almacenar datos: Set, Hashes, SortedSet,Streams, Geopatial, Bitmaps, Bitfields,Probabilistic y Time Series. Elige dos de estos tipos, y crea una función que los guarde en la base de datos y otra que los obtenga. (1.5 puntos)

# Set
def guardar_set():
    baseDatosRedis.sadd('barcos_set', 'BlueWave')
    baseDatosRedis.sadd('barcos_set', 'OceanSweepers')
    baseDatosRedis.sadd('barcos_set', 'SeaGuardian')
    baseDatosRedis.sadd('barcos_set', 'AquaClean')
    baseDatosRedis.sadd('barcos_set', 'ClearSea')
    baseDatosRedis.sadd('barcos_set', 'WaveKeepers')

def obtener_set():
    barcos_set = baseDatosRedis.smembers('barcos_set')
    print(f"Barcos en set: {barcos_set}")

guardar_set()
obtener_set()

# Hashes

def guardar_hash():
    baseDatosRedis.hset('barcos_hash', 'barco_1', 'BlueWave')
    baseDatosRedis.hset('barcos_hash', 'barco_2', 'OceanSweepers')
    baseDatosRedis.hset('barcos_hash', 'barco_3', 'SeaGuardian')
    baseDatosRedis.hset('barcos_hash', 'barco_4', 'AquaClean')
    baseDatosRedis.hset('barcos_hash', 'barco_5', 'ClearSea')
    baseDatosRedis.hset('barcos_hash', 'barco_6', 'WaveKeepers')

def obtener_hash():
    barcos_hash = baseDatosRedis.hgetall('barcos_hash')
    print(f"Barcos en hash: {barcos_hash}")

guardar_hash()
obtener_hash()
