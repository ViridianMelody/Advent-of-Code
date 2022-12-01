def main():
    # Messy 1 liner go brrrrr
    elfSums = sorted([sum([int(x) for x in s.split("\n")]) for s in open("Day1Input.txt", "r").read().split("\n\n")])
    print(f'Max: {elfSums[-1]}')
    print(f'Top 3: {sum(elfSums[-3:])}')


if __name__ == "__main__":
    main()