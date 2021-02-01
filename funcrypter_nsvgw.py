import sys
import random
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class FunCrypterUi(QMainWindow):
    """Program's view (GUI)"""

    def __init__(self, model):
        """View initializer"""
        super().__init__()
        self._model = model
        # Set main window properties
        self.setWindowTitle("FunCrypter - Nethasha Vithana G.W.")
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create labels, sections, buttons
        self._create_top_labels()
        self._create_keygen()
        self._encrypt_messages()
        self._encrypt_user_input()
        self._decrypt_messages()
        self._decrypt_user_input()
        # Put PyQT Window to top left
        qt_rectangle = self.frameGeometry()
        self.move(qt_rectangle.topLeft())

    def _create_top_labels(self):
        """Creating top labels"""
        # Creating first label
        self.toplabel = QLabel()
        self.toplabel.setText("Honors Content - Further Implementation - Task 3.304 \n"
                              "Mathematics for Computer Science \n"
                              "University of London - Coursera.org \n")
        self.toplabel.setFont(QtGui.QFont("Sanserif", 11, weight=QtGui.QFont.Bold))
        self.toplabel.setAlignment(Qt.AlignCenter)

        # Creating second label
        self.secondlabel = QLabel()
        self.secondlabel.setText('C ≡ Mᵉ (mod p) \nM ≡ Cᵈ (mod p)')
        self.secondlabel.setFont(QtGui.QFont("Sanserif", 11))
        self.secondlabel.setAlignment(Qt.AlignCenter)

        # Add labels to general layout
        self.generalLayout.addWidget(self.toplabel)
        self.generalLayout.addWidget(self.secondlabel)

    def _create_keygen(self):
        """Keygen section"""
        self.keygen_label = QLabel()
        self.keygen_label.setText('Keygen')
        self.keygen_label.setFont(QtGui.QFont("Sanserif", 12, weight=QtGui.QFont.ExtraBold))
        self.keygen_label.setStyleSheet("color: blue; padding: 0 0 0 0px")

        # Public key label
        self.public_key_label = QLabel()
        self.public_key_label.setText(f'Public key (e): {self._model.public_key}')
        self.public_key_label.setFont(QtGui.QFont("Sanserif", 11))

        # Private key label
        self.private_key_label = QLabel()
        self.private_key_label.setText(f'Private key (d): {self._model.private_key}')
        self.private_key_label.setFont(QtGui.QFont("Sanserif", 11))

        # Modulus label
        self.modulus_label = QLabel()
        self.modulus_label.setText(f'Modulus (mod p): {self._model.modulus}')
        self.modulus_label.setFont(QtGui.QFont("Sanserif", 11))

        # Info label
        self.save_keys_label = QLabel()
        self.save_keys_label.setText('*Save these keys to decrypt your encrypted messages later')
        self.save_keys_label.setFont(QtGui.QFont("Sanserif", 8))

        # Add generate keys button
        self.generate_keys_button = QPushButton('Generate new keys')
        self.generate_keys_button.setFont(QtGui.QFont("Sanserif", 11))
        self.generate_keys_button.setStyleSheet("background-color : rgb(207,225,255)")
        self.generate_keys_button.clicked.connect(self._generate_keys)

        # Add section to general layout
        self.generalLayout.addWidget(self.keygen_label)
        self.generalLayout.addWidget(self.public_key_label)
        self.generalLayout.addWidget(self.modulus_label)
        self.generalLayout.addWidget(self.private_key_label)
        self.generalLayout.addWidget(self.save_keys_label)
        self.generalLayout.addWidget(self.generate_keys_button)

    def _generate_keys(self):
        """Function for the generate keys button"""
        self._model.generate_new_keys()
        self.modulus_label.setText(f'Modulus (mod p): {self._model.modulus}')
        self.public_key_label.setText(f'Public key (e): {self._model.public_key}')
        self.private_key_label.setText(f'Private key (d): {self._model.private_key}')
        self.encryption_key.setText(f'Encryption key (e): {self._model.public_key}, Modulus p: {self._model.modulus}')

    def _encrypt_messages(self):
        """Section for message encryption"""
        # General labels
        self.encrypt_label = QLabel()
        self.encrypt_label.setText('Encrypt messages')
        self.encrypt_label.setFont(QtGui.QFont("Sanserif", 12, weight=QtGui.QFont.ExtraBold))
        self.encrypt_label.setStyleSheet("color: blue; padding: 20 0 0 0px")

        self.info_label = QLabel()
        self.info_label.setText('*Numbers to be encrypted must be smaller than the modulus')
        self.info_label.setFont(QtGui.QFont("Sanserif", 8))

        # Encryption key label
        self.encryption_key = QLabel()
        self.encryption_key.setText(f'Encryption key (e): {self._model.public_key}, Modulus p: {self._model.modulus}')
        self.encryption_key.setFont(QtGui.QFont("Sanserif", 10))

        self.text_box_label = QLabel()
        self.text_box_label.setText('Enter message to encrypt')
        self.text_box_label.setFont(QtGui.QFont("Sanserif", 11))

        # Message input/ textbox
        self.input_message = QLineEdit()
        self.input_message.setText("Hello World! deep thought 7.5")
        self.input_message.setFont(QtGui.QFont("Sanserif", 11))
        self.input_message.setFixedHeight(30)

        # Add encrypt message button
        self.encrypt_button = QPushButton('Encrypt message')
        self.encrypt_button.setFont(QtGui.QFont("Sanserif", 11))
        self.encrypt_button.setStyleSheet("background-color : rgb(207,225,255)")
        self.encrypt_button.clicked.connect(self._encrypt_user_input)

        # Display encrypted message
        self.encrypted_message_label = QLabel()
        self.encrypted_message_label.setText(f'Encrypted message: ')
        self.encrypted_message_label.setFont(QtGui.QFont("Sanserif", 11))
        self.encrypted_message_display = QLineEdit()
        self.encrypted_message_display.setReadOnly(True)
        self.encrypted_message_display.setFixedHeight(30)

        # Add section to general layout
        self.generalLayout.addWidget(self.encrypt_label)
        self.generalLayout.addWidget(self.info_label)
        self.generalLayout.addWidget(self.encryption_key)
        self.generalLayout.addWidget(self.text_box_label)
        self.generalLayout.addWidget(self.input_message)
        self.generalLayout.addWidget(self.encrypt_button)
        self.generalLayout.addWidget(self.encrypted_message_label)
        self.generalLayout.addWidget(self.encrypted_message_display)

    def _encrypt_user_input(self):
        """Function for the encrypt message button"""
        user_input = self.input_message.text().upper()
        self.encrypted_message = self._model.encrypt_text(user_input)
        self.encrypted_message_display.setText(self.encrypted_message)

    def _decrypt_messages(self):
        """Section for message decryption"""
        self.decrypt_label = QLabel()
        self.decrypt_label.setText('Decrypt messages')
        self.decrypt_label.setFont(QtGui.QFont("Sanserif", 12, weight=QtGui.QFont.ExtraBold))
        self.decrypt_label.setStyleSheet("color: blue; padding: 20 0 0 0px")

        # Choose keys label
        self.choose_keys_label = QLabel()
        self.choose_keys_label.setText('Select your saved keys')
        self.choose_keys_label.setFont(QtGui.QFont("Sanserif", 11))

        # Pick modulus
        self.pick_modulus_label = QLabel()
        self.pick_modulus_label.setText('Select modulus')
        self.pick_modulus_label.setFont(QtGui.QFont("Sanserif", 11))
        self.pick_modulus = QComboBox()
        self.pick_modulus.setFont(QtGui.QFont("Sanserif", 11))
        self.pick_modulus.addItems(self._model.primes_list)

        # Pick decryption key
        self.pick_decryption_key_label = QLabel()
        self.pick_decryption_key_label.setText('Select your private/decryption key')
        self.pick_decryption_key_label.setFont(QtGui.QFont("Sanserif", 11))
        self.pick_d_key = QComboBox()
        self.pick_d_key.setFont(QtGui.QFont("Sanserif", 11))
        d_keys_list = [str(key) for key in self._model.decryption_keys_combobox(self.pick_modulus.currentText())]
        self.pick_d_key.addItems(d_keys_list)

        # Change decryption key dropdown with modulus combobox
        self.pick_modulus.currentTextChanged.connect(self._on_modulus_combobox_changed)

        # Message decryption textbox
        self.code_box_label = QLabel()
        self.code_box_label.setText('Enter encrypted message to decrypt')
        self.code_box_label.setFont(QtGui.QFont("Sanserif", 11))
        self.input_to_decrypt = QLineEdit()
        self.input_to_decrypt.setText("8 36 8 26 1 36 1 28 28 21 28 26 21 8 8 8 1 28 28 26 21 26 26 8 8 26 21 21 1 28 26 36 21 1 1 28 28 21 28 26 1 1 26 8 1 21 28 26 1 28 21 21 1 28 26 36 28 1 21 8 8 8 8 26 26 8 8 1 37 36 28 26 36 28 36 26")
        self.input_to_decrypt.setFont(QtGui.QFont("Sanserif", 11))
        self.input_to_decrypt.setFixedHeight(30)

        # Add decrypt message button
        self.decrypt_button = QPushButton('Decrypt message')
        self.decrypt_button.setFont(QtGui.QFont("Sanserif", 11))
        self.decrypt_button.setStyleSheet("background-color : rgb(207,225,255)")
        self.decrypt_button.clicked.connect(self._decrypt_user_input)

        # Display decrypted message
        self.decrypted_message_label = QLabel()
        self.decrypted_message_label.setText('Decrypted message: ')
        self.decrypted_message_label.setFont(QtGui.QFont("Sanserif", 11))
        self.decrypted_message_display = QLineEdit()
        self.decrypted_message_display.setReadOnly(True)
        self.decrypted_message_display.setFixedHeight(30)

        # Add section to general layout
        self.generalLayout.addWidget(self.decrypt_label)
        self.generalLayout.addWidget(self.choose_keys_label)
        self.generalLayout.addWidget(self.pick_modulus_label)
        self.generalLayout.addWidget(self.pick_modulus)
        self.generalLayout.addWidget(self.pick_decryption_key_label)
        self.generalLayout.addWidget(self.pick_d_key)
        self.generalLayout.addWidget(self.code_box_label)
        self.generalLayout.addWidget(self.input_to_decrypt)
        self.generalLayout.addWidget(self.decrypt_button)
        self.generalLayout.addWidget(self.decrypted_message_label)
        self.generalLayout.addWidget(self.decrypted_message_display)

    def _on_modulus_combobox_changed(self):
        """Function to change decryption key values to match chosen modulus"""
        d_keys_list = [str(key) for key in self._model.decryption_keys_combobox(self.pick_modulus.currentText())]
        self.pick_d_key.clear()
        self.pick_d_key.addItems(d_keys_list)

    def _decrypt_user_input(self):
        """Function for the decrypt message button"""
        user_coded_input = self.input_to_decrypt.text()
        self.decrypted_message = self._model.decrypt_code(user_coded_input, self.pick_d_key.currentText(),
                                                          self.pick_modulus.currentText())
        self.decrypted_message_display.setText(self.decrypted_message)


class FunCrypterModel:
    """Program's model to handle operations"""
    def __init__(self):
        self.letter_code = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16,
                            'G': 21, 'H': 22, 'I': 23, 'J': 24, 'K': 25, 'L': 26,
                            'M': 31, 'N': 32, 'O': 33, 'P': 34, 'Q': 35, 'R': 36,
                            'S': 41, 'T': 42, 'U': 43, 'V': 44, 'W': 45, 'X': 46,
                            'Y': 51, 'Z': 52, ' ': 53, ',': 54, '.': 55, '?': 56,
                            '0': 61, '1': 62, '2': 63, '3': 64, '4': 65, '5': 66,
                            '6': 71, '7': 72, '8': 73, '9': 74, '!': 75, ':': 76}
        self.primes_list = self._modulus_list()
        self.modulus = random.choice(self.primes_list)  # string
        self.special_power = self._calculate_special_power(int(self.modulus))
        self.public_private_keys = self._calculate_keys(int(self.modulus), self.special_power)  # integer
        self.public_key, self.private_key = random.choice(list(self.public_private_keys.items()))

    @staticmethod
    def _check_if_prime(number):
        """Function to check if a number is a prime"""
        div = [x for x in range(2, number) if number % x == 0]
        return len(div) == 0

    def _modulus_list(self):
        """Function to create list of prime numbers"""
        primes = [str(x) for x in range(43, 2000) if self._check_if_prime(x)]
        return primes

    @staticmethod
    def _calculate_special_power(mod):
        """Returns the special power in mod p-1 which produces 1"""
        mod_p_minus_one = mod - 1
        factors = [x for x in range(2, mod_p_minus_one) if mod_p_minus_one % x == 0]
        relative_primes = [x for x in range(1, mod_p_minus_one)]
        for n in range(1, mod_p_minus_one):
            i = 0
            while i <= len(factors) - 1:
                if n % factors[i] == 0:
                    relative_primes.remove(n)
                    break
                i += 1
        return len(relative_primes)

    @staticmethod
    def _calculate_keys(mod, power):
        """Function to calculate public, private keys"""
        encryption_keys = []
        for x in range(2, mod - 2):
            if (x ** power) % (mod - 1) == 1:
                encryption_keys.append(x)
        encryption_decryption_keys = {x: ((x**(power-1)) % (mod - 1)) for x in encryption_keys
                                      if x != ((x**(power-1)) % (mod - 1))}
        return encryption_decryption_keys

    def generate_new_keys(self):
        """Function for generating new keys"""
        self.modulus = random.choice(self.primes_list)  # string
        self.special_power = self._calculate_special_power(int(self.modulus))  # integer
        self.public_private_keys = self._calculate_keys(int(self.modulus), self.special_power)  # integer:integer
        self.public_key, self.private_key = random.choice(list(self.public_private_keys.items()))

    def _encrypt(self, number):
        """Returns a number as an encrypted number"""
        encrypted_num = (number ** self.public_key) % int(self.modulus)
        return encrypted_num

    def encrypt_text(self, text):
        """Returns text as encrypted numbers"""
        encrypted_word = []
        for i in text:
            encrypted_word.append(str(self._encrypt(self.letter_code[i] // 10)))
            encrypted_word.append(str(self._encrypt(self.letter_code[i] % 10)))
        return " ".join(encrypted_word)

    def decryption_keys_combobox(self, decrypt_modulus):
        """Function to return list of decryption keys for modulus selected by user"""
        d_special_power = self._calculate_special_power(int(decrypt_modulus))  # integer
        e_d_keys = self._calculate_keys(int(decrypt_modulus), d_special_power)  # integer:integer
        decrypt_keys = list(e_d_keys.values())
        decrypt_keys.sort()
        return decrypt_keys

    @staticmethod
    def _decrypt(encrypted_number, private_k, mod):
        """Returns a number as a decrypted number"""
        decrypted_num = (int(encrypted_number) ** int(private_k)) % int(mod)
        return decrypted_num

    def decrypt_code(self, num_string, private_k, mod):
        """Returns coded numbers (a string) as decrypted text"""
        final_num = ""
        for i in num_string.split():
            final_num += str(self._decrypt(i, private_k, mod))

        result_word = ""
        code_string = final_num
        x = 0
        while x < len(code_string):
            for letter, number in self.letter_code.items():
                if int(code_string[0:2]) == number:
                    result_word += letter
            code_string = code_string[2:]
        return result_word


def main():
    """Main function"""
    # Creating instance of QApplication
    funcrypter = QApplication(sys.argv)
    # Creating instance of model
    model = FunCrypterModel()
    # Show the program's GUI
    view = FunCrypterUi(model)
    view.show()
    # Execute the program's main loop
    sys.exit(funcrypter.exec_())


if __name__ == '__main__':
    main()
