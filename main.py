# Dice sum probability calculator
# Författare: Dmytro Malanchuk
# Datum:2024-08-21

def main():
    # Läs in input från användaren
    input_str = input("Ange antalet sidor på de två tärningarna, separerade med ett mellanslag: ")
    N, M = map(int, input_str.split())

    # Skapa en dictionary för att räkna hur många gånger varje summa förekommer
    sum_counts = {}

    # Loopar över alla möjliga tärningskast
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            current_sum = i + j
            if current_sum in sum_counts:
                sum_counts[current_sum] += 1
            else:
                sum_counts[current_sum] = 1

    # Hitta den högsta frekvensen
    max_frequency = max(sum_counts.values())

    # Hitta alla summor med den högsta frekvensen
    most_likely_sums = [s for s in sum_counts if sum_counts[s] == max_frequency]

    # Skriv ut summorna i fallande ordning
    for sum_value in sorted(most_likely_sums, reverse=True):
        print(sum_value)

if __name__ == "__main__":
    main()
