from getpass import getpass
from hangman_ascii import hangman_ascii


def split(word):
    return list(word)


def beautiful_print(list):
    print("".join(list))


hp = 6

print("choose a word")
word = str(getpass(""))
word = word.lower()
word_split = split(word)

final_word = []
for char in word:
    if char.isalpha():
        final_word.append("_")
    else:
        final_word.append(char)

len_of_word = len(word)
beautiful_print(final_word)


while True:

    print("choose one character")
    choose_char = str(input())
    choose_char = choose_char.lower()

    if len(choose_char) > 1:
        print("that's more than one character, dummy")

    for i, char in enumerate(word):
        if choose_char == char:
            final_word[i] = choose_char

    if final_word == word_split:
        beautiful_print(final_word)
        print(f"you won! The word was {word}!")
        break

    beautiful_print(final_word)

    if choose_char in word:
        print(f"yep          hp = {hp}")
    else:
        hp -= 1
        print(hangman_ascii[hp])
        print(f"nah g        hp = {hp}")

    if hp <= 0:
        print("you lost!")
        break
