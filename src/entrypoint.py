from argparse import ArgumentParser
from dataclasses import dataclass

from config import Config, configure_from_json_file


@dataclass
class CommandLineArgs:
    xxx: str


def parse_command_line_arguments() -> CommandLineArgs:

    parser: ArgumentParser = ArgumentParser(prog="yolo")
    parser.add_argument("xxx", action="store", type=str)

    args = parser.parse_args()

    return CommandLineArgs(xxx=args.xxx)


if __name__ == "__main__":
    config: Config = configure_from_json_file()
    print(config)

    command_line_args = parse_command_line_arguments()
    print(command_line_args.xxx)
