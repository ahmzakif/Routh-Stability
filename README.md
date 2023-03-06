    MK      : SISTEM KENDALI
    Nama    : Ahmad Zaki Firdaus
    NIM     : 21/479669/PA/20795

Program tersebut adalah sebuah program Python yang dapat menghitung tabel Routh-Hurwitz dan mengevaluasi stabilitas sistem kontrol dengan mengambil nilai K dari pengguna. Berikut ini adalah penjelasan dari setiap fungsi yang ada di dalam program tersebut:

1. getExpr(raw_expr): Fungsi ini digunakan untuk mengubah ekspresi matematika dalam bentuk string menjadi ekspresi simbolik menggunakan fungsi parse_expr dari modul sympy.parsing.sympy_parser. Setelah itu, fungsi ini juga menyederhanakan ekspresi tersebut menggunakan fungsi simplify dari modul sympy.

2. determinant(r1c1, r1c2, r2c1, r2c2): Fungsi ini digunakan untuk menghitung determinan dari sebuah matriks 2x2 menggunakan rumus det = r1c1*r2c2 - r2c1*r1c2. Fungsi ini juga menggunakan fungsi simplify dari modul sympy untuk menyederhanakan hasil determinan.

3. printRouthArray(RouthArray): Fungsi ini digunakan untuk mencetak tabel Routh-Hurwitz yang telah dihitung menggunakan fungsi RouthHurwitz. Fungsi ini menerima argumen berupa matriks yang merepresentasikan tabel Routh-Hurwitz.

4. exprArrToStrArr(expr_arr): Fungsi ini digunakan untuk mengubah matriks yang merepresentasikan tabel Routh-Hurwitz dari bentuk simbolik menjadi bentuk string. Fungsi ini juga melakukan konversi tanda pangkat ** menjadi tanda pangkat ^.

5. ToLaTeX(str_arr): Fungsi ini digunakan untuk mengubah matriks yang merepresentasikan tabel Routh-Hurwitz dari bentuk string menjadi format LaTeX. Fungsi ini menambahkan tanda $$ di depan dan di belakang setiap elemen matriks untuk menunjukkan bahwa elemen tersebut akan ditulis dalam mode matematika di LaTeX.

6. RouthHurwitz(polynomial): Fungsi ini adalah inti dari program tersebut. Fungsi ini menerima argumen berupa sebuah list yang berisi koefisien polinomial dalam bentuk simbolik. Fungsi ini mengembalikan tabel Routh-Hurwitz dalam bentuk matriks.

7. inputPolynomial(polynomial): Fungsi ini digunakan untuk meminta pengguna memasukkan koefisien polinomial yang akan digunakan untuk menghitung tabel Routh-Hurwitz. Fungsi ini meminta pengguna untuk memasukkan orde polinomial terlebih dahulu, lalu meminta pengguna untuk memasukkan koefisien untuk masing-masing orde secara terurut dari orde tertinggi hingga orde nol. Fungsi ini juga mencetak polinomial yang telah dimasukkan oleh pengguna.

8. defineKvalue adalah sebuah fungsi yang menerima dua parameter, yaitu Kvalue dan polynomial. Fungsi ini bertujuan untuk mengevaluasi nilai K dari persamaan karakteristik dan menentukan apakah sistem stabil atau tidak. Pertama-tama, fungsi ini membuat sebuah list kosong bernama equation. Selanjutnya, fungsi ini melakukan loop pada setiap elemen dalam polynomial dan jika nilai dari elemen tersebut berupa sebuah persamaan yang mengandung variabel K, maka nilai persamaan tersebut dievaluasi dengan menggunakan nilai Kvalue. Setiap hasil evaluasi persamaan tersebut kemudian ditambahkan ke dalam list equation.

9. Setelah list equation terisi dengan hasil evaluasi dari persamaan karakteristik yang mengandung variabel K, maka fungsi ini melakukan loop pada setiap elemen dalam list equation. Jika terdapat setidaknya satu elemen yang bernilai negatif, maka sistem dikatakan tidak stabil dan program akan mencetak pesan "Sistem Tidak Stabil" dan mengubah nilai variabel Stabil menjadi False. Namun, jika semua nilai elemen dalam list equation non-negatif, maka sistem dikatakan stabil dan program akan mencetak pesan "Sistem Stabil".

10. Pada blok kode terakhir, program memanggil fungsi inputPolynomial untuk meminta input orde dan koefisien dari polinomial, kemudian mencetak Routh Table menggunakan fungsi RouthHurwitz dan printRouthArray. Setelah itu, program meminta input nilai K menggunakan fungsi input, dan mengevaluasi stabilitas sistem menggunakan fungsi defineKvalue.