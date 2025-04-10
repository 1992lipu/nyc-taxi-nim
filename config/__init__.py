import toml
import os

# Load the settings from the TOML file
config_path = os.path.join(os.path.dirname(__file__), 'settings.toml')
config = toml.load(config_path)

# Extract the required settings
NIM_SQL_API_URL = config['api']['NIM_SQL_API_URL']
NIM_IMAGE_API_URL = config['api']['NIM_IMAGE_API_URL']
NIM_API_KEY = config['api']['NIM_API_KEY']