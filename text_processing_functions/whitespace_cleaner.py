def SpaceRemover(word):
    process_word = ""

    for i in word:
        if i == " ":
            continue
        else:
            process_word += i

    return process_word


"""
if __name__ == "__main__":
    SpaceRemover("Hello world")
"""
