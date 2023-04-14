import sys, re

def main():
    last_line: str = ""
    for line in sys.stdin:
        last_line = line.strip()

    numbers = re.findall(r"\d+", last_line)
    failed, passed, skipped, xfailed, xpassed, error = map(int, numbers[:6])

    print(f'Failed: {failed}')
    print(f'Passed: {passed}')
    print(f'Skipped: {skipped}')
    print(f'XFailed: {xfailed}')
    print(f'XPassed: {xpassed}')
    print(f'Error: {error}')

    if __name__ == "__main__":
        main()