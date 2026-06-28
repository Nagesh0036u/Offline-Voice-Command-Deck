import subprocess
import webbrowser
import os
from command_manager import get_action


def execute_command(command):
    action = get_action(command)

    if action is None:
        return False

    # Open websites
    if action.startswith("http"):
        webbrowser.open(action)
        return True

    # Initialize Workspace
    if action == "workspace":

        # Open VS Code if installed
        vscode = r"C:\Users\Likitha bn\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        if os.path.exists(vscode):
            subprocess.Popen(vscode)

        # Open GitHub
        webbrowser.open("https://github.com")

        return True

    # Open Windows applications
    try:
        subprocess.Popen(action)
        return True
    except Exception as e:
        print("Error:", e)
        return False