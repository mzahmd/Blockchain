# xi+1 = (a * xi + b) mod m
# x0 (= seed)

def lin_kon(seed, a, b, m, n):
    for i in range(n):
        print(seed)
        seed = (a * seed + b) % m


def lin_kon_period(seed, a, b, m):
    seed_list = []
    while seed not in seed_list:
        seed_list.append(seed)
        seed = (a * seed + b) % m
    print(seed_list)
    print(len(seed_list))


lin_kon(3, 7, 4, 9, 9)
print()
lin_kon_period(5, 7, 12, 212)
