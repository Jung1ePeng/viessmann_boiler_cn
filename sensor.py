"""Sensor platform for gas_boiler_temperature."""
from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Gas Boiler Temperature sensor."""
    async_add_entities([GasBoilerTemperatureSensor()])

class GasBoilerTemperatureSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Gas Boiler Temperature'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # 此处添加获取燃气锅炉水温的逻辑
        self._state = 60  # 示例温度
