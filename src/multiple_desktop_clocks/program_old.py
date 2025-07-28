import os

import multiple_desktop_clocks.about as about
import multiple_desktop_clocks.modules.configure as configure 

# Caminho para o arquivo de configuração
CONFIG_PATH = os.path.join(os.path.expanduser("~"),".config",about.__package__,"config.json")

configure.verify_default_config(CONFIG_PATH, default_content={"casa":"verde"})

CONFIG=configure.load_config(CONFIG_PATH)
print("Hola!")
