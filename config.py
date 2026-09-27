"""
Docker-vriendelijke config voor dsmr2mqtt.
Vervangt config.rename.py: alle instellingen komen uit environment variables,
zodat één image op meerdere locaties bruikbaar is.
Configureer de DSMR-berichten nog steeds in dsmr50.py.
"""
import os


def _bool(name, default):
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


# [ LOGLEVELS ] DEBUG, INFO, WARNING, ERROR, CRITICAL
loglevel = os.getenv("LOGLEVEL", "INFO")

# [ PRODUCTION ] False = simulatie met SIMULATORFILE (geen P1-kabel nodig)
PRODUCTION = _bool("PRODUCTION", True)
SIMULATORFILE = os.getenv("SIMULATORFILE", "test/dsmr.raw")

# [ MQTT ]
MQTT_BROKER = os.getenv("MQTT_BROKER", "192.168.1.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_CLIENT_UNIQ_ID = os.getenv("MQTT_CLIENT_UNIQ_ID", "mqtt-dsmr")
MQTT_QOS = int(os.getenv("MQTT_QOS", "1"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "")
MQTT_MAXRATE = int(os.getenv("MQTT_MAXRATE", "60"))

if PRODUCTION:
    MQTT_TOPIC_PREFIX = os.getenv("MQTT_TOPIC_PREFIX", "dsmr")
    MQTT_CLIENT_UNIQ = MQTT_CLIENT_UNIQ_ID
    HA_ID = os.getenv("HA_ID", "")
else:
    MQTT_TOPIC_PREFIX = os.getenv("MQTT_TOPIC_PREFIX", "test_dsmr")
    MQTT_CLIENT_UNIQ = MQTT_CLIENT_UNIQ_ID + "-test"
    HA_ID = os.getenv("HA_ID", "TEST")

# [ Home Assistant ]
HA_DISCOVERY = _bool("HA_DISCOVERY", True)
HA_DELETECONFIG = _bool("HA_DELETECONFIG", True)
HA_DISCOVERY_RATE = int(os.getenv("HA_DISCOVERY_RATE", "12"))

# [ P1 USB serial ] pad BINNEN de container
ser_port = os.getenv("SER_PORT", "/dev/ttyUSB0")
ser_baudrate = int(os.getenv("SER_BAUDRATE", "115200"))
