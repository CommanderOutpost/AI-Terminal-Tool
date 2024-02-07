# Import necessary modules and classes
from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command
from ai.ai_reply_storage import RedisDatabase
import datetime
import signal
from terminal.interruption import cleanup

# Initialize RedisDatabase instance for storing AI commands and terminal outputs
redis_db = RedisDatabase()

# Get the user command from the terminal
user_command = get_argument_from_terminal()

# Set up a signal handler for Ctrl+C to perform cleanup on interruption
signal.signal(signal.SIGINT, cleanup)

# Define the maximum number of iterations for the loop
MAX_ITE = 5

# Iterate a maximum of MAX_ITE times
for _ in range(MAX_ITE):
    # Generate AI command based on user input
    ai_command = generate_command(user_command)

    # Check if the AI command contains the word "stop" and break the loop if true
    if "stop" in ai_command.lower():
        print(terminal_output)
        redis_db.delete_all_data()
        break

    # Run the AI command in the terminal and store the output
    terminal_output = run_terminal_command(ai_command)

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Create a dictionary with AI command as key and terminal output as value
    data = {ai_command: terminal_output}

    # Add the data to the Redis database with the current date and time as the key
    redis_db.add_item(str(current_datetime), str(data))

    # Update the user command for the next iteration
    user_command = user_command + "[" + terminal_output.lower() + "]"

    # Print AI command and terminal output for the current iteration
    print("AI Command: ", ai_command, "\nTerminal Output: ", terminal_output)

# Perform cleanup by deleting all data from the Redis database
redis_db.delete_all_data()
