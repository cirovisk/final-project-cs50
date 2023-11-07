# RPG autobattler
#### Video Demo:  <URL HERE>
#### Description:
# `literal_classes.py` Description

This Python script defines a simple Role-Playing Game (RPG) with different character classes. The classes defined in this script are:

## `RPGCharacter`

This is the base class for all characters in the game. It defines the basic attributes and methods that all characters have, such as hit points (`hp`), armor, strength, and a method to check if the character is still alive (`is_alive()`).

## `Fighter`

This class represents a fighter character. It inherits from the `RPGCharacter` class and overrides the `attack()` method to provide a specific implementation for a fighter's attack. The damage for a fighter's attack is a random number between 1 and 12.

## `Rogue`

This class represents a rogue character. It also inherits from the `RPGCharacter` class and overrides the `attack()` method. The damage for a rogue's attack is twice a random number between 1 and 6.

## `Mage`

This class represents a mage character. It inherits from the `RPGCharacter` class and overrides the `attack()` method. The damage for a mage's attack is three times a random number between 1 and 4. This reflects the mage's ability to cast powerful spells, but with less physical strength compared to other classes.

## `Dragon`

The `Dragon` class represents a dragon character in the game. It also inherits from the `RPGCharacter` class. Dragons are typically powerful and tough opponents in RPGs, and this is reflected in the high hit points, armor, and strength values for the `Dragon` class.

Each character class has an `attack()` method that calculates the damage dealt to a target character and reduces the target's hit points. The method returns a string that describes the attack.

The script also includes a `simulate_combat()` function that simulates a combat between two characters until one of them is no longer alive. The results of the combat are displayed in a QTextEdit widget.

This script can be used as a starting point for a more complex RPG, with more character classes, different types of attacks, and more complex combat mechanics. For now it is only an autobattler script.    