import os
import pwd
import subprocess


def get_owner_of_folder(path: str) -> str:
    uid = os.stat(path).st_uid
    username = pwd.getpwuid(uid).pw_name
    return username


def set_ownership_recursive(user: str, path: str):
    _ = subprocess.run([f"chown -R {user}:{user} {path}"])
