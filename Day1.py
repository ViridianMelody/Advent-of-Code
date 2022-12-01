def main():
    elfSums = sorted([sum([int(x) for x in s.split("\n")]) for s in open("Day1Input.txt", "r").read().split("\n\n")])
    print(f'{elfSums[:-4:-1]}')

if __name__ == "__main__":
    main()