def correct_sentence(text: str) -> str:
    """
    Function return correct sentence
    :param text: some sentence
    :return: correct sentence
    """

    # FIXME
    # TODO

    end_sentence = ['.', '!', '?']

    text_list = list(text)

    if text_list[0].islower():
        text_list[0] = text_list[0].upper()

    if text_list[-1] not in end_sentence:
        text_list.append('.')

    return ''.join(text_list)


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
