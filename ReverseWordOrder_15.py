def reverse_str():
    str = input('Enter a sentence --- ')
    if len(str) < 1: str = 'this is a sentence'
    return ' '.join(str.split()[::-1])
    # lastDigit = len(str)
    # print(str)
    # n = 0; reverse = []
    # while lastDigit > n:
    #     reverse.append(str[lastDigit - 1])
    #     lastDigit -= 1
    # return reverse

print(reverse_str())