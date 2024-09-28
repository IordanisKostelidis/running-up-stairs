def calculate(stairs: int) -> int:
    if stairs == 0:
        return 0
    if stairs == 1 or stairs == 2:
        return 1
    return calculate(stairs - 1) + calculate(stairs - 2)

def main():
    for test_case in range(int(input())):
        print(calculate(int(input())+1))

if __name__ == '__main__':
    main()