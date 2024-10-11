from app.commands import Command
from calculator.operations import subtract

class SubtractCommand(Command):
    def execute(self):
        print()