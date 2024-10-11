from app.commands import Command
from calculator.operations import multiply

class MultiplyCommand(Command):
    def execute(self):
        print()