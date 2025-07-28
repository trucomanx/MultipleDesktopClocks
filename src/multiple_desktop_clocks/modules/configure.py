import os
import json

# Lê o JSON no início do programa
def load_config(config_path):
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
            return data.get("timezones", [])
        except:
            return []
    return []
    
def save_config(config_path,timezones):
    data = {"timezones": timezones}
    directory_name = os.path.dirname(config_path)
    os.makedirs(directory_name, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(data, f, indent=4)
