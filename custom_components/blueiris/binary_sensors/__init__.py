from homeassistant.core import HomeAssistant

from ..helpers.const import *
from ..models.entity_data import EntityData
from .audio import BlueIrisAudioBinarySensor
from .connectivity import BlueIrisConnectivityBinarySensor
from .main import BlueIrisMainBinarySensor
from .motion import BlueIrisMotionBinarySensor

BINARY_SENSOR_TYPES = {
    SENSOR_CONNECTIVITY_NAME: BlueIrisConnectivityBinarySensor,
    SENSOR_MOTION_NAME: BlueIrisMotionBinarySensor,
    SENSOR_AUDIO_NAME: BlueIrisAudioBinarySensor,
    SENSOR_MAIN_NAME: BlueIrisMainBinarySensor,
}

CURRENT_DOMAIN = DOMAIN_BINARY_SENSOR


def get_binary_sensor(hass: HomeAssistant, host: str, entity: EntityData):
    entity_sensor_type = entity.type
    binary_sensor_ctor = BINARY_SENSOR_TYPES[entity_sensor_type]

    binary_sensor = binary_sensor_ctor()
    binary_sensor.initialize(hass, host, entity, CURRENT_DOMAIN)

    return binary_sensor
