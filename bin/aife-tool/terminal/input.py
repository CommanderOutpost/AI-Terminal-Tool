import sys
from subprocess import run, PIPE, CalledProcessError


def get_argument_from_terminal():
    # Check if at least one command-line argument is provided
    if len(sys.argv) < 2:
        # Print a usage message and exit the program with status code 1
        print("Usage: python main.py <argument>")
        sys.exit(1)

    # Return the first command-line argument (index 1, as index 0 is the script name)
    return sys.argv[1]


def run_terminal_command(command):
    try:
        # Run the terminal command, capturing the result
        result = run(command, shell=True, check=True, stdout=PIPE, stderr=PIPE)

        # Check if there is any standard output
        if result.stdout is not None:
            # Decode the standard output from bytes to UTF-8 string
            output = result.stdout.decode("utf-8")
        else:
            output = ""

        # Return a success message along with the command output
        return f"Command '{command}' executed successfully. Output: {output}"

    except CalledProcessError as e:
        # Return an error message along with the command's stderr output
        return f"Error executing command '{command}': {e.stderr.decode('utf-8')}"
