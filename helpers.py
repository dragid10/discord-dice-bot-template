import random
import re


def is_empty(input_str: str) -> bool:
    """Check if the input string is empty or contains only whitespace

    Args:
        input_str (str): The input string to check

    Returns:
        bool: True if the input string is empty or contains only whitespace, False otherwise
    """
    if input_str is None or input_str.isspace() or input_str.strip() == "":
        return True
    else:
        return False


def is_valid_roll(user_input: str) -> bool:
    """Determine if the user's input is a valid roll. A valid roll should contain the letter 'd' and be like "1d12"

    Args:
        user_input (str): The user's input

    Returns:
        bool: True if the user's input is a valid roll, False otherwise
    """

    # Check if the roll is empty
    if is_empty(user_input):
        return False

    # A valid text roll should contain the letter 'd'. E.g. 1d20 OR d20, 2d6, 3d8
    if "d" not in user_input.casefold():
        return False

    # Regex to ensure that this format is matched: <number>d<number>
    die_roll_regex = r"\d+[dD]{1}\d+"
    if not re.fullmatch(die_roll_regex, user_input):
        return False

    return True


def _calculate_roll(dice_quantity: int, die_face: int) -> list[int]:
    """Calculate the dice rolls for the user

    Args:
        dice_quantity (int): The number of dice to roll
        die_face (int): The face of the die to roll

    Returns:
        list[int]: The list of dice rolls
    """

    dice_rolls = []

    # Roll the dice and store the result
    for i in range(0, dice_quantity):
        dice_rolls.append(random.randint(1, die_face))

    return dice_rolls


def roll_dice(roll: str) -> list[int]:
    """ Roll the dice for the user

    Args:
        roll (str): The user's intended roll. E.g. 1d20, 2d6, 3d8

    Returns:
        list[int]: The result of dice roll(s) as a list

    """
    # Split user text into individual parts: 1d20 -> ["1", "20"]
    roll_parts: list[str] = roll.split("d")

    # Activate the random Number Generator!
    rolls: list[int] = _calculate_roll(int(roll_parts[0]), int(roll_parts[1]))

    return rolls
