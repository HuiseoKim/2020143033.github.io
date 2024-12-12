def count_alphabet_occurrences(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()

    alphabet_count = {}
    for char in text:
        if char.isalpha():
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1

    sorted_alphabet_count = sorted(alphabet_count.items(), key=lambda item: item[1], reverse=True)
    sorted_alphabets = [item[0].upper() for item in sorted_alphabet_count]

    print(sorted_alphabets)

if __name__ == "__main__":
    count_alphabet_occurrences('input_7_2.txt')