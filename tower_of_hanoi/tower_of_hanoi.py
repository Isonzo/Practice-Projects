

def pm(start, end):
    print(start, "-->", end)


def hanoi(n, start, end):
    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        pm(start, end)
        hanoi(n - 1, other, end)


rings = int(input("Number of rings: "))
start_rod = int(input("Starting rod (1 - 3)"))
end_rod = int(input("Destination rod (1 - 3)"))

hanoi(rings, start_rod, end_rod)
input("\nPress anything to exit ")
