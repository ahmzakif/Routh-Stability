    MK      : SISTEM KENDALI
    Nama    : Ahmad Zaki Firdaus
    NIM     : 21/479669/PA/20795

Kode yang disediakan adalah sebuah program Python yang mengimplementasikan kriteria stabilitas Routh untuk memeriksa stabilitas sebuah sistem dengan koefisien polinomialnya. Program ini berguna untuk membantu mempercepat dan memudahkan analisis sistem kontrol untuk menentukan apakah suatu sistem kontrol bersifat stabil atau tidak. Program ini terdiri dari dua fungsi: routh_table() dan check_stability(), dan sebuah program utama yang menerima masukan dari pengguna untuk mendapatkan koefisien polinomial dan nilai K.

1. Fungsi routh_table() membuat sebuah tabel Routh untuk sekumpulan koefisien polinomial yang diberikan dengan menggunakan algoritma Routh-Hurwitz. Fungsi ini mengambil larik koefisien polinomial sebagai input dan mengembalikan matriks yang mewakili tabel Routh.
   
Program ini akan digunakan untuk membuat tabel Routh dari koefisien polinomial yang diberikan sebagai input. Fungsi ini memiliki tiga langkah utama yaitu:

a. Menghitung ukuran tabel Routh yang akan dibuat. Ukuran tabel tergantung pada jumlah koefisien polinomial yang diberikan.

    n = len(coefficients)
    m = (n+1)//2
    table = np.zeros((n,m))

b. Mengisi baris pertama dan kedua dari tabel Routh dengan koefisien polinomial yang diberikan.

    table[0,:] = coefficients[0::2]
    if n > 1:
        table[1,:] = coefficients[1::2]

c. Mengisi seluruh tabel Routh dengan menggunakan rumus yang sesuai dengan aturan pembuatan tabel Routh.

    for i in range(20,n):
        for j in range(m):
            if j == 0:
                table[i,j] = -1/(table[i-2,j+1])*(table[i-1,j+1]*table[i-2,j] - table[i-1,j]*table[i-2,j+1])
            else:
                table[i,j] = -1/(table[i-2,0])*(table[i-1,j+1]*table[i-2,0] - table[i-1,0]*table[i-2,j+1])
            if np.isnan(table[i,j]):
                table[i,j] = 0
    return table
    
Pada setiap iterasi, program akan menghitung nilai pada sel berikutnya dari tabel Routh berdasarkan nilai-nilai pada sel yang sudah diisi sebelumnya. Jika nilai yang dihasilkan oleh rumus tersebut menghasilkan nilai NaN (Not a Number), maka nilai sel tersebut diubah menjadi 0.

Setelah seluruh tabel Routh terisi, fungsi akan mengembalikan tabel Routh tersebut.


2. Fungsi check_stability() memeriksa stabilitas sistem dengan memodifikasi koefisien polinomial dengan faktor K dan kemudian memeriksa tabel Routh yang dihasilkan untuk stabilitas. Fungsi ini mengambil koefisien polinomial asli dan nilai K sebagai input, dan mengembalikan sebuah string yang menunjukkan apakah sistem stabil atau tidak stabil.

Fungsi ini memiliki empat langkah utama yaitu:

a. Mengubah koefisien polinomial yang diberikan dengan menambahkan nilai K pada setiap koefisien yang memiliki pangkat ganjil.

    modified_coefficients = np.zeros(len(coefficients))
    modified_coefficients[0::2] = coefficients[0::2] + K*coefficients[1::2]
    modified_coefficients[1::2] = coefficients[1::2]

b. Membuat tabel Routh dari koefisien polinomial yang sudah dimodifikasi dengan menggunakan fungsi routh_table().

c. Mengecek apakah tabel Routh mengandung nilai NaN. Jika tabel Routh mengandung nilai NaN, itu berarti ada pembagian oleh nol saat membuat tabel Routh, yang menunjukkan bahwa sistem tidak stabil.

d. Mengecek apakah setiap elemen pada kolom pertama tabel Routh adalah positif. Jika salah satu elemen pada kolom pertama tabel Routh negatif, itu menunjukkan bahwa sistem tidak stabil. Jika tidak ada elemen pada kolom pertama tabel Routh yang negatif, itu menunjukkan bahwa sistem stabil.

Fungsi kemudian mengembalikan nilai "Sistem stabil" atau "Sistem tidak stabil" tergantung pada hasil pengecekan kestabilan yang dilakukan.


3. Program utama meminta pengguna untuk memasukkan koefisien polinomial dan nilai K. Program ini kemudian memanggil fungsi routh_table () untuk membuat tabel Routh, dan mencetak polinomial dan tabel Routh yang dihasilkan. Kemudian memanggil fungsi check_stability() untuk memeriksa stabilitas sistem dan mencetak hasilnya.

Secara keseluruhan, kode yang disediakan adalah alat yang berguna untuk memeriksa stabilitas sistem menggunakan kriteria stabilitas Routh. Program ini mudah digunakan dan dapat disesuaikan agar sesuai dengan sistem polinomial yang berbeda dengan memodifikasi koefisien input dan nilai K.
