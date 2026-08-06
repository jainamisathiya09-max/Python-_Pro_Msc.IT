n = [1,2,2,3,4,4,4,5]

dup = []

for i in range(len(n)-1):
    if n[i] == n[i+1] and n[i] not in dup:
        dup.append(n[i])

print(dup)
