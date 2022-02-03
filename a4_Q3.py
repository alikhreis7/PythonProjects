


def longest_run(num):
    longcount, count = 0, 1
    for i in range(1, len(num)):
        if num[i] != num[i - 1]:
            if count > longcount:
                longcount = count
            count = 1
        else:
            count += 1
    if len(num) > 0 and count > longcount:
        longcount = count
    return longcount


def main():
    enter = input("Please input a list of numbers separated by space: ").strip().split()
    num = []
    for string in enter:
        if string.strip() != "":
            num.append(float(string))
    print(longest_run(num))


main()
