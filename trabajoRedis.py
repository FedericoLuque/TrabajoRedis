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
baseDatosRedis.set('barco_7', 'EcoMarine')

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