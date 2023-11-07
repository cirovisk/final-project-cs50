import random
from art import text2art
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QInputDialog,
    QLineEdit,
    QTextEdit,
)


class RPGGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("RPG Game")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.startButton = QPushButton("Start Game", self)
        self.startButton.clicked.connect(self.startGame)

        self.restartButton = QPushButton(
            "Restart Game", self
        )  # Create the restart button
        self.restartButton.clicked.connect(
            self.restartGame
        )  # Connect the button to the restartGame method
        self.restartButton.setEnabled(
            False
        )  # Disable the button at the start of the game

        self.resultText = QTextEdit()  # Create the QTextEdit widget
        self.resultText.setReadOnly(True)  # Make the QTextEdit widget read-only
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(
            self.restartButton
        )  # Add the restart button to the layout
        self.layout.addWidget(self.resultText)  # Add the QTextEdit widget to the layout

    def startGame(self):
        class_choice, okPressed = QInputDialog.getItem(
            self, "Pick your class", "Class:", ["Fighter", "Rogue", "Mage"], 0, False
        )
        if okPressed:
            name, okPressed = QInputDialog.getText(
                self, "Get text", "Character name:", QLineEdit.Normal, ""
            )
            if okPressed and name != "":
                if class_choice == "Fighter":
                    character = Fighter(name)
                elif class_choice == "Rogue":
                    character = Rogue(name)
                elif class_choice == "Mage":
                    character = Mage(name)

                dragon = Dragon("Dragon")
                simulate_combat(
                    character, dragon, self.resultText
                )  # Pass the QTextEdit widget to the simulate_combat function
                self.restartButton.setEnabled(
                    True
                )  # Enable the restart button after the game is over

    def restartGame(self):
        # Code to restart the game
        self.resultText.clear()  # Clear the QTextEdit widget
        self.startGame()  # Start a new game


class RPGCharacter:
    def __init__(self, name, character_class, hp, armor, damage, hit_chance):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.hit_chance = hit_chance

    def attack(self, target):
        if (
            random.random() < self.hit_chance
        ):  # Compara um número aleatório com a chance de acerto
            damage_dealt = self.damage
            target.receive_damage(damage_dealt)
        else:
            print(f"{self.name} missed the attack.")

    def receive_damage(self, damage):
        if self.armor >= damage:
            print(f"{self.name} blocked the attack and took no damage.")
        else:
            damage_taken = damage - self.armor
            self.hp -= damage_taken
            print(
                f"{self.name} took {damage_taken} damage. Remaining Hit Points: {self.hp}"
            )

    def is_alive(self):
        return self.hp > 0


class Fighter(RPGCharacter):
    def __init__(self, name):
        random_damage = random.randint(1, 12)
        super().__init__(
            name, "fighter", 14, 3, random_damage, 0.8
        )  # 80% de chance de acerto

    def attack(self, target):
        random_damage = random.randint(1, 12)
        damage = random_damage
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage"


class Rogue(RPGCharacter):
    def __init__(self, name):
        random_damage = random.randint(1, 6) * 2
        super().__init__(name, "rogue", 10, 5, random_damage, 0.7)

    def attack(self, target):
        random_damage = random.randint(1, 6) * 2
        damage = random_damage
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage"


class Mage(RPGCharacter):
    def __init__(self, name):
        random_damage = random.randint(1, 4) * 3
        super().__init__(name, "mage", 6, 0, random_damage, 0.9)

    def attack(self, target):
        random_damage = random.randint(1, 4) * 3
        damage = random_damage
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage"


class Dragon(RPGCharacter):
    def __init__(self, name):
        random_damage = random.randint(1, 6)
        super().__init__(
            name, "dragon", 16, 0, random_damage, 0.5
        )  # 50% de chance de acerto

    def attack(self, target):
        random_damage = random.randint(1, 6)
        damage = random_damage
        target.hp -= damage
        return f"{self.name} attacks {target.name} for {damage} damage"


def main():
    # Cria um personagem
    character = create_character()

    # Cria um dragão
    dragon = Dragon("Dragon")

    # Simula o combate
    simulate_combat(character, dragon)


def create_character():
    print("Pick your class:")
    print("1. Fighter")
    print("2. Rogue")
    print("3. Mage")

    class_choice = input("Class: ")

    while class_choice not in ["1", "2", "3"]:
        print("Invalid class. Please choose a valid class.")
        class_choice = input("Class: ")

    name = input("Character name: ")

    while not name:
        print("Invalid name. Please choose a valid name.")
        name = input("Character name: ")

    if class_choice == "1":
        character = Fighter(name)
    elif class_choice == "2":
        character = Rogue(name)
    elif class_choice == "3":
        character = Mage(name)

    return character


def print_winner_art(winner):
    winner_art = text2art(winner)
    print(winner_art)


def simulate_combat(character, dragon, result_text):
    while character.is_alive() and dragon.is_alive():
        attack_details = character.attack(dragon)
        result_text.append(attack_details)
        if dragon.is_alive():  # The dragon only attacks if it's still alive
            attack_details = dragon.attack(character)
            result_text.append(attack_details)

    if character.is_alive():
        result_text.append(f"{character.name} won!")
        print_winner_art(character.name)
    else:
        result_text.append("The Dragon won!")
        print_winner_art("Dragon")


# Chama a função main
if __name__ == "__main__":
    app = QApplication([])
    ex = RPGGame()
    ex.show()
    app.exec_()
