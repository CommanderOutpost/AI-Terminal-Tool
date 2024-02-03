from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command

user_command = get_argument_from_terminal()

ai_command = generate_command(user_command)

run_terminal_command(ai_command)
