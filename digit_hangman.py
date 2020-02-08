from hangman import Hangman


def check_input(number_set: str):
    """
    test input that on format should be or not
    """
    if len(number_set) != 23:
        return False
    else:
        for i in range(len(number_set)):
            if i % 2 == 0:
                if number_set[i] == " ":
                    return False
            elif i % 2 != 0:
                if number_set[i] != " ":
                    return False
    return True

def translate_number(number_set: str) -> dict:
    """
    change string set for number to list 
    """
    number_list = []
    for i in number_set:
            if i != " ":
                number_list.append(int(i))
    return number_list



number_set = input()

while check_input(number_set) != True:
    number_set: str = input()

number_lst: list = translate_number(number_set)
print(number_lst)
hangman = Hangman(number_lst)
hangman.play()
print(hangman.score)



