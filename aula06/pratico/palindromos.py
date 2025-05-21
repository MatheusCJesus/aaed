# Este codigo verifica se uma palavra é um palíndromo.
# Esse codigo foi escrito com base no artigo do site https://www.geeksforgeeks.org/palindrome-string/


def is_palimdrome(word):
    """
    Check if a word is a palindrome.
    """
    return word == word[::-1]

def is_palimdrome_recursive(word):
    """
    Check if a word is a palindrome using recursion.
    """
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palimdrome_recursive(word[1:-1])

def is_palimdrome_iterative(word):
    """
    Check if a word is a palindrome using iteration.
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True

if __name__ == "__main__":

    print(is_palimdrome("arara"))
    list = ["arara", "banana", "civic", "deified", "level", "madam", "racecar", "radar", "refer", "rotor", "sagas", "solos", "tenet", "wow"]
    for word in list:
        print(f"{word} is a palindrome: {is_palimdrome(word)}")