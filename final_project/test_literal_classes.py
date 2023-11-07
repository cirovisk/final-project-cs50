from unittest.mock import patch, MagicMock
from art import text2art
from literal_classes import create_character, simulate_combat, Fighter, Dragon, print_winner_art

def test_create_character():
    with patch('builtins.input', side_effect=["1", "Test Fighter"]):
        character = create_character()

    assert isinstance(character, Fighter), "create_character did not return a Fighter"
    assert character.name == "Test Fighter", "Character name is incorrect"

def test_simulate_combat():
    fighter = Fighter("Test Fighter")
    dragon = Dragon("Test Dragon")

    result_text = MagicMock()  # Create a mock QTextEdit widget

    simulate_combat(fighter, dragon, result_text)  # Pass the mock QTextEdit widget to the function

    assert not fighter.is_alive() or not dragon.is_alive(), "Both characters are still alive after combat"
    
def test_print_winner_art():
    with patch('builtins.print') as mock_print:
        print_winner_art("Test")

    mock_print.assert_called_once_with(text2art("Test"))