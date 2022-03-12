
def main():
    minInterval = -100
    maxInterval = 100

    rezultat = []

    for x in range(minInterval, maxInterval):
        for y in range(minInterval, maxInterval):
            for z in range(minInterval, maxInterval):
                if((x + y != 0) and (x + z != 0) and (y + z != 0)):
                    if (z / (x + y)) + (y / (z + x)) + (x / (z + y)) == 4:
                        rezultat.append((x, y, z))

    print(rezultat)


main()