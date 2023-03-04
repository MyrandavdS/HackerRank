import textwrap


def wrap(string, max_width):
    # This is where the set the width value for the text wrap
    wrapper = textwrap.TextWrapper(width=max_width)
    #print(wrapper)
    # This is the text that will be wrapped with the variable that has the width value. Will be into a list
    word_list = wrapper.wrap(text=string)
    #print(word_list)

    # We have a variable with an empty string to fill with the word_list
    # Here we go through the list each wrap text with the right width
    # what is in the variable string won't be replaced by i but it adds up with the + and will be seperated by the \n on the right width
    answer = ""
    for i in word_list:
        answer = answer + i + "\n"
    return answer


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)