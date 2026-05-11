import logging 

#congiguración del archivo de Log

logging.basicConfig(
    filename='sistema.log', #Indica el archivo donde se guardarán los logs, en este caso "sistema.log"
    level=logging.INFO, # Indica el nivel de severidad de los logs que se guardarán, en este caso se guardarán los logs de nivel INFO y superiores (WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s' #define el formato de los mensajes de log, incluyendo la fecha y hora del evento, el nivel de severidad y el mensaje de log en sí (los mensajes se definen en las funciones, logger.info/error(mensaje))
)

logger = logging.getLogger('software_fj') #Crea un objeto logger con el nombre "software_fj" que se utilizará para registrar los eventos en el sistema. Este logger se puede usar en cualquier parte del código para registrar mensajes de log utilizando los métodos logger.info(), logger.error(), etc.
