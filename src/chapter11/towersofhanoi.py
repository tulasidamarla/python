def move(towers, disks, fromPeg, toPeg):
    if disks > 0:
        other = 3 - fromPeg - toPeg
        move(towers, disks - 1, fromPeg, other)
        diskToMove = towers[fromPeg].pop()
        towers[toPeg].append(diskToMove)
        print(towers)
        move(towers, disks - 1, other, toPeg)


def main():
    NDISKS = 3
    disks = list(range(1, NDISKS + 1))
    disks.reverse()
    towers = [disks, [], []]
    print(towers)
    move(towers, NDISKS, 0, 2)


main()
