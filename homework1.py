def chocolate_piles(n):
    even_or_odd = n % 2
    piles = [n]
    current = n
    for i in range(1, n):
        next_chocolate = current - 2
        if next_chocolate <= 0:
            break
        piles += [next_chocolate]
        current = next_chocolate
    print(piles)

n = int(input("Enter the number of chocolates in the first pile: "))

chocolate_piles(n)