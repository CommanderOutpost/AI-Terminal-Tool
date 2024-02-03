from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command

user_command = get_argument_from_terminal()

max_ite = 3

for _ in range(max_ite):
    ai_command = generate_command(user_command)
    terminal_output = run_terminal_command(ai_command)

    if "error" not in terminal_output.lower():
        print(terminal_output)
        break

    user_command = user_command + "[" + terminal_output.lower() + "]"

    print(terminal_output)
