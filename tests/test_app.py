'''Tests for exit and unknown command'''
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    '''Exit command test'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    '''Unknown command test'''
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
