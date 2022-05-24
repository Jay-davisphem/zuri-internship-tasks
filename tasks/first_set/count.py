"""Simple function to count the number of word in a given text"""


def count(text: str) -> int:
    """
    arg: text -> str
    return: count_num -> int
    """
    count_num = 0
    for _ in text.split():
        count_num += 1
    return count_num


if __name__ == "__main__":
    TEXT = input("Enter a sentence: ")
    print(count(TEXT), '\n')
