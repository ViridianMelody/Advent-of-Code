def main():
    print(max([sum([int(x) for x in s.split("\n")]) for s in open("Day1Input.txt", "r").read().split("\n\n")]))

if __name__ == "__main__":
    main()