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

