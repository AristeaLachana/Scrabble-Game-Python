#!/usr/bin/env python
# coding: utf-8

import random
from itertools import permutations


# σακουλάκι
class SakClass:
    def __init__(self):
        # δομή δεδομένων για τα γράμματα
        self.lets = {}
        self.lettersNum = 104

    def __repr__(self):
        return f'Class: {self.__class__}, lets: {self.lets}, lettersNum: {self.lettersNum}'

    def getletters(self, n):  # βγάζει από το σακουλάκι για τον παίκτη Ν γράμματα
        completed = False
        letters = []
        while not completed:
            # κρατάω την lets όπως είναι τώρα, σε περίπτωση που χρειαστεί να αλλάξει
            # η λίστα με τα γράμματα που επιλέχθηκαν τυχαία
            temp = self.lets
            temp_num = self.lettersNum
            letters = [random.choice(list(self.lets)) for i in range(int(n))]  # τυχαία επιλογή
            for key in letters:
                if key in self.lets:
                    count = self.lets[key][0]
                    # ανανέωση πλήθους γραμμάτων
                    if count > 0:
                        count -= 1
                        self.lettersNum -= 1
                        # η νέα λίστα - τιμή του key
                        value_list = [count, self.lets[key][1]]
                        self.lets[key] = value_list
                        completed = True  # όσο το πλήθος είναι όπως πρέπει, διατηρώ τη τιμή True
                    else:
                        # αν κάποιο γράμμα έχει πλήθος 0, πρέπει να γίνει από την αρχή η τυχαία επιλογή
                        self.lets = temp
                        self.lettersNum = temp_num
                        completed = False

                if not completed:
                    break
        return letters

    # γράμματα που επιστρέφονται στο σακουλάκι από τον παίκτη
    def putbackletters(self, remained_letters):
        for key in remained_letters:
            if key in self.lets:
                count = self.lets[key][0]
                count += 1
                self.lettersNum += 1
                value_list = [count, self.lets[key][1]]
                self.lets[key] = value_list
        null_list = []
        return null_list

    # τα γράμματα που θα έχει το σακουλάκι, με την αξία και το πλήθος τους
    def randomize_sak(self):
        # πρώτη τιμή : πλήθος γραμμάτων στο παιχνίδι
        # δεύτερη τιμή : αξία γράμματος στο παιχνίδι
        self.lets = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1], 'Ζ': [1, 10],
                     'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2], 'Λ': [3, 3], 'Μ': [3, 3],
                     'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1], 'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1],
                     'Τ': [8, 1], 'Υ': [4, 2], 'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}


# παίκτης
class Player:
    def __init__(self):
        self.name = ""
        self.letters = []
        self.score = 0

    def __repr__(self):
        return f'Class: {self.__class__}, name: {self.name}, letters: {self.letters}, score: {self.score}'

    def setletters(self, letters):
        self.letters = letters

    # μέθοδος που υπολογίζει την αξία της σχηματισμένης λέξης στο scrabble
    def word_value(self, word, sak):
        sum_value = 0
        for letter in word:  # για κάθε γράμμα της λέξης που δίνεται
            if letter in sak.lets:  # όταν βρεθεί το γράμμα στη δομή
                sum_value += sak.lets[letter][1]
        return sum_value

    # μέθοδος που ελέγχει αν η λέξη που δίνεται είναι αποδεκτή - DONE
    def word_accept(self, word, accepted):
        if word == 'Q':
            return False
        search_key = word[0]  # το κλειδί της λέξης που ψάχνω - πρώτο γράμμα λέξης
        with open("greek7.txt", 'r', encoding="utf8"):

            value_list = accepted[search_key]  # τιμή κλειδιού - λίστα με λέξεις που ξεκινάνε από το ίδιο γράμμα

            if word in value_list:
                print("Αποδεκτή Λέξη\n")
                return True
            else:
                print("Μη Αποδεκτή Λέξη\n")
                return False


# χρήστης - παίκτης
class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'Class: {self.__class__}, name: {self.name}, letters: {self.letters}, score: {self.score}'

    def play(self, accepted_words, sak):
        print("\nΣτο σακουλάκι: " + str(sak.lettersNum) + " γράμματα.\n")
        print("Παίζεις - Σκορ: " + str(self.score) + "\n")
        print("Διαθέσιμα γράμματα: ")
        self.print_available_letters(sak)

        # καταχώρηση λέξης και έλεγχος αν είναι από τα γράμματα που δίνονται
        word = self.input_right_word()

        # ο χρήστης επιθυμεί να σταματήσει το παιχνίδι
        if word == 'q':
            sak.lettersNum = 0
            return sak

        # p σημαίνει pass
        if word != "p":

            word_upper = word.upper()

            # έλεγχος αν η λέξη περιλαμβάνεται στον κατάλογο αποδεκτών λέξεων
            if self.word_accept(word_upper, accepted_words):
                value = self.word_value(word_upper, sak)  # υπολογισμός αξίας της λέξης
                print("Πόντοι λέξης " + word + ": " + str(value))
                self.score += value
                print("Σκορ: " + str(self.score))

                # αφαίρεση γραμμάτων που χρησιμοποιήθηκαν
                for letter in self.letters:
                    if str(letter) in word_upper:
                        # διαγραφή γράμματος που χρησιμοποιήθηκε από τη λίστα letters του παίκτη
                        self.letters.remove(letter)
                        # διαγραφή του letter από τη λέξη ΜΙΑ ΦΟΡΑ - αποφυγή διαγραφής επιπλέον
                        # γραμμάτων που δεν χρησιμοποιήθηκαν
                        word_upper.replace(letter, '', 1)

                # συμπλήρωση γραμμάτων παίκτη - πρέπει να είναι πάντα 7 γράμματα
                remained_letters_num = len(self.letters)
                if 7 - remained_letters_num > 0:
                    add = sak.getletters(7 - remained_letters_num)
                    self.letters.extend(add)

            else:
                print("Χάνεις τη σειρά σου - για αλλαγή γραμμάτων θυμήσου να πληκτρολογήσεις p")

        # ο παίκτης ζητάει καινούρια γράμματα - χάνει τη σειρά του
        else:
            # επιστροφή προηγούμενων γραμμάτων στο σακουλάκι
            self.letters = sak.putbackletters(self.letters)
            # κλήρωση νέων γραμμάτων για τον παίκτη
            self.letters = sak.getletters(7)
            print("Χάνεις τη σειρά σου...")

        return sak

    # σωστό format εμφάνισης των διαθέσιμων γραμμάτων του κάθε παίκτη
    def print_available_letters(self, sak):
        for letter in self.letters:
            if letter in sak.lets:
                value = sak.lets[letter][1]
                print("Γράμμα: " + letter + " - Αξία: " + str(value))

    # ελέγχει αν η λέξη που έδωσε ο χρήστης αποτελείται από τα γράμματα που διαθέτει
    def input_right_word(self):
        while True:
            word = input("ΛΕΞΗ: ")
            word_upper = word.upper()
            accept = True
            if word != 'q' and word != 'p':
                for letter in word_upper:
                    if letter not in self.letters:
                        accept = False
                        print("Χρησιμοποίησες γράμμα που δεν διαθέτεις.")
                        print("Δώσε άλλη λέξη")
                        break
            if accept:
                break

        # επιστρέφεται η lowercase λέξη, για τη περίπτωση που έδωσε q ή p
        return word

    def getScore(self):
        return self.score


# υπολογιστής - παίκτης
class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def __repr__(self):
        return f'Class: {self.__class__}, name: {self.name}, letters: {self.letters}, score: {self.score}'

    # επιλογή αλγορίθμου με τον οποίο παίζει ο υπολογιστής
    def play(self, accepted_words, sak, choice):
        word = ""
        print("\nΣτο σακουλάκι: " + str(sak.lettersNum) + " γράμματα.\n")
        print("Παίζει ο Η/Υ - Σκορ: " + str(self.score))
        print("Διαθέσιμα γράμματα: ")
        self.print_available_letters(sak)
        # ανάλογα την ρύθμιση, επιλογή κατάλληλου αλγορίθμου
        if choice == "min":
            word = self.min_choice(accepted_words)
        elif choice == "max":
            print("min")
            word = self.max_choice(accepted_words)
        else:
            word = self.smart_choice(accepted_words, sak)
        if word != "Δεν βρέθηκε λέξη":
            sum_value = self.word_value(word, sak)
            self.score += sum_value
            print("Πόντοι λέξης " + word + ": " + str(sum_value))
            print("Σκορ: " + str(self.score))
            # αφαίρεση γραμμάτων που χρησιμοποιήθηκαν
            for letter in self.letters:
                if str(letter) in word:
                    # διαγραφή γράμματος που χρησιμοποιήθηκε από τη λίστα letters του παίκτη
                    self.letters.remove(letter)
                    # διαγραφή του letter από τη λέξη ΜΙΑ ΦΟΡΑ - αποφυγή διαγραφής επιπλέον
                    # γραμμάτων που δεν χρησιμοποιήθηκαν
                    word.replace(letter, '', 1)

            # συμπλήρωση γραμμάτων παίκτη - πρέπει να είναι πάντα 7 γράμματα
            remained_letters_num = len(self.letters)
            if 7 - remained_letters_num > 0:
                add = sak.getletters(7 - remained_letters_num)
                self.letters.extend(add)
        else:
            # επιστροφή προηγούμενων γραμμάτων στο σακουλάκι
            self.letters = sak.putbackletters(self.letters)
            # κλήρωση νέων γραμμάτων για τον παίκτη
            self.letters = sak.getletters(7)

        return sak

    # σωστό format εμφάνισης των διαθέσιμων γραμμάτων του κάθε παίκτη
    def print_available_letters(self, sak):
        for letter in self.letters:
            if letter in sak.lets:
                value = sak.lets[letter][1]
                print("Γράμμα: " + letter + " - Αξία: " + str(value))

    # δημιουργεί όλες τις δυνατές μεταθέσεις των γραμμάτων που διαθέτει ο Η/Υ ξεκινώντας από 2 και
    # ανεβαίνοντας μέχρι τα 7 γράμματα. Για κάθε μετάθεση ελέγχει αν είναι
    # αποδεκτή λέξη και επιστρέφει την πρώτη αποδεκτή λέξη που θα εντοπίσει
    # και αν δεν βρει λέξη, επιστρέφει "Δεν βρέθηκε λέξη"
    def min_choice(self, accepted_words):
        found = False
        final_word = "Δεν βρέθηκε λέξη"
        for i in range(2, len(self.letters) + 1):
            possible_words = list(permutations(self.letters, i))
            for pw in possible_words:
                word = "".join((str(e) for e in pw))
                if found:
                    break
                if word in accepted_words[word[0]]:
                    found = True
                    final_word = word
            if found:
                break

        print(final_word)
        return final_word

    # ίδια λειτουργία με το min_choice, με τη διαφορά ότι το πρόγραμμα ξεκινά από τις
    # μεταθέσεις των γραμμάτων ανά 7 και κατεβαίνει προς το 2
    # αν δεν βρει λέξη, επιστρέφει "Δεν βρέθηκε λέξη"
    def max_choice(self, accepted_words):
        found = False
        final_word = "Δεν βρέθηκε λέξη"
        for i in range(len(self.letters), 1, -1):
            possible_words = list(permutations(self.letters, i))
            for pw in possible_words:
                word = "".join((str(e) for e in pw))
                if found:
                    break
                if word in accepted_words[word[0]]:
                    found = True
                    final_word = word
            if found:
                break

        print(final_word)
        return final_word

    # υλοποιούνται όλες οι μεταθέσεις και η λέξη που επιλέγει ο Η/Υ είναι αυτή
    # (ή μία από αυτές τις λέξεις) που έχει τη μεγαλύτερη αξία
    # αν δεν βρει λέξη, επιστρέφει "Δεν βρέθηκε λέξη"
    def smart_choice(self, accepted_words, sak):
        words = []
        for i in range(2, 8):
            possible_words = list(permutations(self.letters, i))
            for pw in possible_words:
                word = "".join((str(e) for e in pw))
                if word in accepted_words[word[0]]:
                    words.append(word)

        words_and_values = {}
        for word in words:
            value = self.word_value(word, sak)
            words_and_values[word] = value

        max_value = max(words_and_values.values())
        final_word = self.get_key(max_value, words_and_values)
        print(final_word)
        return final_word

    # παίρνει το κλειδί του λεξικού με βάση τη τιμή
    def get_key(self, val, my_dict):
        for key, value in my_dict.items():
            if val == value:
                return key

        return "Δεν βρέθηκε λέξη"

    def getScore(self):
        return self.score


# παρτίδα
class Game:
    human_player = None
    pc_player = None
    sak = None

    def __init__(self):
        self.accepted_words = None
        self.round = 1

    def __repr__(self):
        return f'Class: {self.__class__}, accepted_words: {self.accepted_words}, round: {self.round}'

    def setup(self):
        # αρχικοποίηση αντικειμένων των κλάσεων - ονόματα και σακουλάκι
        print('Γράψε το όνομά σου: ')
        human_name = input()
        Game.human_player = Human(human_name)
        Game.pc_player = Computer()
        Game.sak = SakClass()
        # προετοιμασία της δομής δεδομένων με τα γράμματα στο σακουλάκι
        Game.sak.randomize_sak()
        # λεξικό με τις αποδεκτές λέξεις
        self.accepted_words = self.words_dictionary()

    # μέθοδος που "τρέχει" το παιχνίδι
    def run(self, algorithm):
        print("\nΣτο σακουλάκι: " + str(Game.sak.lettersNum) + " γράμματα.\n")
        n = 7
        while True:
            if Game.sak.lettersNum < 7:
                self.end()
                break
            print("\nΠαρτίδα " + str(self.round) + "\n")
            if self.round % 2 == 1:
                if not Game.human_player.letters:
                    Game.human_player.setletters(Game.sak.getletters(n))
                Game.sak = Game.human_player.play(self.accepted_words, Game.sak)
                # αν ο παίκτης αποφασίσει να τερματίσει το παιχνίδι
                if Game.sak == 0:
                    self.end()
                    break
            else:
                if not Game.pc_player.letters:
                    Game.pc_player.setletters(Game.sak.getletters(n))
                Game.sak = Game.pc_player.play(self.accepted_words, Game.sak, algorithm)
            self.round += 1
            input("Πάτα Enter για να συνεχιστεί το παιχνίδι.")

    # το τέλος του παιχνιδιού
    def end(self):
        print('Τέλος Παιχνιδιού!')
        self.insert_data()
        # Ανακοινώνει τις βαθμολογίες Παίκτη και Η/Υ ανακηρύσσοντας τον νικητή
        # άνοιγμα αρχείου για εγγραφή

    # δημιουργία δομής λεξικού (με τιμές λίστα) από το αρχείο greek7.txt
    def words_dictionary(self):
        words_d = {}
        f = open("greek7.txt", encoding="utf8")
        for line in f:
            key = line[0]
            value = line
            if key in words_d:
                words_d[key] += value
            else:
                words_d[key] = value
        for x in words_d:
            words_d[x] = words_d[x].split("\n")
        return words_d

    # καταχώρηση δεδομένων στο αρχείο scrabble_data.txt - ΒΕΛΤΙΩΣΗ
    def insert_data(self):
        with open('scrabble_data.json', 'w', encoding="utf8") as f:
            pc_score = Game.pc_player.score
            human_score = Game.human_player.score
            line = "Παίκτης Η/Υ - Σκορ: " + str(pc_score) + '\n'
            f.write(line)
            print(line)
            line = "Παίκτης " + Game.human_player.name + " - Σκορ: " + str(human_score) + '\n'
            f.write(line)
            print(line)
            max_score = pc_score
            max_name = human_score
            if human_score > max_score:
                max_score = human_score
                max_name = Game.human_player.name
            line = "Νικητής: " + max_name + " με σκορ " + str(max_score) + "\n"
            f.write(line)
            print(line)
        f.close()
