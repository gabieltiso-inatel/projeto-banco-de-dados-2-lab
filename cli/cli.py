from utils import clear_screen

class SimpleCLI:
    def __init__(self):
        self.commands = []

    # `command_tuple` assumes the form of a tuple, which takes 
    # a string as its first argument, representing the name of
    # the command, and a function as the second argument, which
    # is the action taken by the command
    def add_command(self, command_tuple):
        self.commands.append(command_tuple)

    def run(self):
        while True:
            print("Supported commands: ")
            for i, command in enumerate(self.commands):
                print(f"{i}) {command[0]}")

            quit_idx = len(self.commands)
            print(f"{quit_idx}) quit")

            command_idx = int(input("Enter a command index: "))
            clear_screen();

            if command_idx < 0 or command_idx > quit_idx:
                print("Not a valid index, try again")
                continue

            if command_idx == quit_idx:
                break

            self.commands[command_idx][1]()

            _ = input("Press anything to continue!")

