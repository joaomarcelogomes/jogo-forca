import random


def play():
    print_welcome_message()

    hanged = False
    guessed_word = False
    missed_tries = 0
    secret_word = load_random_word()
    scores = initialize_score_list(secret_word)

    print(" ".join(scores))

    while not hanged and not guessed_word:
        chute = ask_try()

        if chute in secret_word:
            score(chute, scores, secret_word)
        else:
            missed_tries += 1
            print("{} tentativas restantes".format(6 - missed_tries))

        guessed_word = "_" not in scores
        hanged = missed_tries == 6
        print(" ".join(scores))

    finish_game(guessed_word, secret_word)


def print_welcome_message():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def load_random_word():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    indice_aleatorio = random.randrange(0, len(palavras))
    return palavras[indice_aleatorio].lower()


def initialize_score_list(secret_word: str):
    return ["_" for _ in secret_word]


def ask_try():
    return input("Qual letra deseja chutar? ").strip().lower()


def score(chute: str, scores: list, secret_word: str):
    index = 0
    for letra in secret_word:
        if chute == letra:
            scores[index] = letra
        index += 1


def finish_game(guessed_word: bool, secret_word: str):
    print("Fim do jogo")
    if guessed_word:
        print("Parabéns, você ganhou!")
        return

    print("Não foi dessa vez :(")
    print("A palavra secreta era: {}".format(secret_word))


if __name__ == '__main__':
    play()
