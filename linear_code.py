from math import log, ceil

def calculate_message_length(N):
	nd = int(log(N,2))
	return nd

def encode(message):
    nd = len(message)
    nr = ceil(log(nd + 1 + ceil(log((nd + 1),2)),2))
    matrix_data = []
    for i in range(nd):
        matrix_data.append("0" * i + "1" + "0" * (nd - i - 1))
    
    d0 = 3 - 1
    matrix_redundant = []
    matrix_redundant.append("1" * nr)
    k = 1

    while k <= d0:
        max_i = nr - k + 1
        i = 0
        while i < max_i:
            if len(matrix_redundant) == nd:
                break
            matrix_redundant.append("1" * i + "0" * k + "1" * (nr-k-i))
            i += 1
        k += 1
    
    if len(matrix_redundant) < nd:
        matrix_redundant.append("0" * (nr - 3) + "1" * (k-1) + "0")

    print("Порождающая матрица:")
    for i in range(nd):
        print(matrix_data[i], "|", matrix_redundant[i])

    code = message
    summ_elements = []
    for i in range(nd):
        if message[i] == "1":
            summ_elements.append(matrix_redundant[i])

    for k in range(nr):
        summa = 0
        summa_string = ""
        for i in range(len(summ_elements)):
            summa += int(summ_elements[i][k])
            summa_string = summa_string + "+ " + summ_elements[i][k] + " "
        if summa % 2 == 0:
            summa_string += "= 0"
            code += "0"
        else:
            summa_string += "= 1"
            code += "1"

        print("Вычисление контрольного бита", k+1,":", summa_string[2:])
    
    print("Закодированное сообщение",code)
    return matrix_redundant

def detect_error(matrix_redundant, code):
    rows = len(matrix_redundant)
    cols = len(matrix_redundant[0])
    transposed = ["" for _ in range(cols)]
    for j in range(cols):
        for i in range(rows):
            transposed[j] += matrix_redundant[i][j]
    
    for i in range(cols):
        transposed[i] += "0" * i + "1" + "0" * (cols - i - 1)

    print("Контрольная матрица: ")
    for i in range(cols):
        print(transposed[i])

    s_vector = ""
    for i in range(cols):
        odd = False
        summa_string = ""
        for j in range(len(code)):
            if transposed[i][j] == "1":
                if code[j] == "1":
                    odd = not odd
                    summa_string += "+ 1 "
                else:
                    summa_string += "+ 0 "
        if odd:
            s_vector += "1"
            summa_string += "= 1"
        else:
            s_vector += "0"
            summa_string += "= 0"
        print("Вычисление ошибки в",i+1,"строке:",summa_string[2:])
    
    print("Вектор ошибки:", s_vector)
    if "1" not in s_vector:
        print("В переданном сообщении нет ошибок.")
    else:
        transposed_back = ["" for _ in range(len(transposed[0]))]
        for i in range(len(transposed)):
            for j in range(len(transposed[0])):
                transposed_back[j] += transposed[i][j]
        for i in range(len(transposed_back)):
            if transposed_back[i] == s_vector:
                print("В переданном сообщении содержится ошибка в",i+1, "бите")

n = calculate_message_length(512)
print("Длина сообщения:", n) 
message = "110000001"
print("Длина введённого сообщения:", len(message))
print("Сообщение:",message)
matrix = encode(message)
print()

error = "1100100010001"
print("Сообщение с ошибкой:", error)
detect_error(matrix, error)