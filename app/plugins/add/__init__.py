from app.commands import Command
from calculator.operations import add

class AddCommand(Command):
    def execute(self):
        print()