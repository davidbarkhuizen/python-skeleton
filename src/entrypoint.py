from dataclasses import dataclass
from os import path
from config import Config, configure_from_json_file

from argparse import ArgumentParser

@dataclass
class CommandLineArgs:
    xxx: str

def parse_command_line_arguments() -> CommandLineArgs:

    parser: ArgumentParser = ArgumentParser(
        prog='yolo',
        description='you only live once',
        epilog='death'
    )
    parser.add_argument('xxx', action="store", type=str)
    
    args = parser.parse_args()

    return CommandLineArgs(
        xxx=args.xxx
    )


if __name__ == '__main__':

    command_line_args = parse_command_line_arguments()
    config: Config = configure_from_json_file()

    xxx = command_line_args.xxx 
    print(xxx)