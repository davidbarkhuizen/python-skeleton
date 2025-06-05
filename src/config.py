from dataclasses import dataclass, asdict, field
import json
from typing import Type
from dacite import from_dict

CONFIG_FILE_PATH = './config.json'

@dataclass
class LogConfig:
    root_folder: str = 'log'

@dataclass
class Config:
    log: LogConfig = field(default_factory=lambda: LogConfig())

def load_config_from_json_file(json_file_path: str, data_class_type: Type[dataclass]) -> dict:
    
    data: dict = None
    with open(json_file_path) as f:
        data = json.load(f)

    return from_dict(
        data_class=data_class_type, 
        data=data
    )

def write_config_to_json_file(config: Type[dataclass], json_file_path: str) -> dict:
    with open(json_file_path, 'w') as json_file:
        json.dump(
            asdict(config), 
            json_file
        )

def load_config_from_file(config_file_path: str) -> Config:

    try:
        return load_config_from_json_file(
            json_file_path=config_file_path,
            data_class_type=Config
        )
    except FileNotFoundError as e:
        print(f'exception attempting to load config file {config_file_path}: {e}')

    return None

def configure_from_json_file(json_config_file_path: str = CONFIG_FILE_PATH) -> Config:

    config = load_config_from_file(json_config_file_path)

    if config is None:
        print(f'not configured.  creating a new config file @ {json_config_file_path} ...')
        
        config = Config()
        
        write_config_to_json_file(
            config=config,
            json_file_path=json_config_file_path
        )
        print(f'... created a new.')
        
    return config
