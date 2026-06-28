import json
import os

COMMAND_FILE = "commands.json"


def load_commands():
    """Load all commands from commands.json"""
    if not os.path.exists(COMMAND_FILE):
        return {}

    with open(COMMAND_FILE, "r") as file:
        return json.load(file)


def save_commands(commands):
    """Save commands to commands.json"""
    with open(COMMAND_FILE, "w") as file:
        json.dump(commands, file, indent=4)


def add_command(command_name, action):
    commands = load_commands()
    commands[command_name.lower()] = action
    save_commands(commands)


def get_action(command_name):
    commands = load_commands()
    return commands.get(command_name.lower(), None)


def get_all_commands():
    return load_commands()