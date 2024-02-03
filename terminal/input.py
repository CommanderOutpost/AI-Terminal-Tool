import sys
import subprocess


def get_argument_from_terminal():
    # Check if at least one argument is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    # Return the first argument (index 1, as index 0 is the script name)
    return sys.argv[1]


def run_terminal_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")
