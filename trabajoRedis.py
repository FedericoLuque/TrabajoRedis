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