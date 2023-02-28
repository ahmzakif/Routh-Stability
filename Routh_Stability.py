import numpy as np

# fungsi untuk membuat tabel Routh
def routh_table(coefficients):
    n = len(coefficients)
    m = (n+1)//2
    table = np.zeros((n,m))
    table[0,:] = coefficients[0::2]
    if n > 1:
        table[1,:] = coefficients[1::2]
    for i in range(20,n):
        for j in range(m):
            if j == 0:
                table[i,j] = -1/(table[i-2,j+1])*(table[i-1,j+1]*table[i-2,j] - table[i-1,j]*table[i-2,j+1])
            else:
                table[i,j] = -1/(table[i-2,0])*(table[i-1,j+1]*table[i-2,0] - table[i-1,0]*table[i-2,j+1])
            if np.isnan(table[i,j]):
                table[i,j] = 0
    return table

# fungsi untuk mengecek kestabilan
def check_stability(coefficients, K):
    modified_coefficients = np.zeros(len(coefficients))
    modified_coefficients[0::2] = coefficients[0::2] + K*coefficients[1::2]
    modified_coefficients[1::2] = coefficients[1::2]
    table = routh_table(modified_coefficients)
    if np.any(np.isnan(table)):
        return "Sistem tidak stabil"
    elif np.any(table[:,0] < 0):
        return "Sistem tidak stabil"
    else:
        return "Sistem stabil"

# main program
coefficients = input("Masukkan koefisien polinomial (dipisahkan dengan spasi): ")
coefficients = np.array(coefficients.split(), dtype=float)
K = float(input("Masukkan nilai K: "))
print("Polinomial:")
print(np.poly1d(coefficients))
print("Tabel Routh:")
table = routh_table(coefficients)
print(table)
print("Kestabilan:")
print(check_stability(coefficients, K))
