

def two_length_run(num):
    for x in range(1, len(num)):
        if num[x] == num[x - 1]:
            return True
    return False


def main():
    enternum = input("Please input a list of numbers separated by space: ").strip().split()
    num = []
    for string in enternum:
        if string.strip() != "":
            num.append(float(string))
    print(two_length_run(num))


main()

