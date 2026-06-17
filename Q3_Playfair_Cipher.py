def generate_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used = ""
    for ch in key.upper():
        if ch not in used and ch != 'J':
            used += ch
    for ch in alphabet:
        if ch not in used:
            used += ch
    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))
    return matrix

key = input("Enter Key: ")
matrix = generate_matrix(key)

for row in matrix:
    print(row)
