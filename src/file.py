from dataclasses import dataclass, asdict
import json
import os
import pwd
from dacite import from_dict
from typing import Type

def get_owner_of_folder(path: str) -> str:
    uid = os.stat(path).st_uid
    username = pwd.getpwuid(uid).pw_name
    return username

def set_ownership_recursive(user: str, path: str):
    os.system(f'chown -R {user}:{user} {path}')

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
