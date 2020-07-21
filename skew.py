text = "CATTCCAGTACTTCATGATGGCGTGAAGA"


def Skew(Genome):
    skew = [0]

    for i in range(0, len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew
print(len(text))

ans = Skew(text)
for num in ans:
    print(num)