# Kombinasi Particle Swarm Optimization Dengan K-means Untuk Menghasilkan Nilai SSE Dan Silhouette Yang Lebih Optimal

## Tujuan
Kombinasi antara Particle Swarm Optimization (PSO) dengan K-Means digunakan untuk menghasilkan hasil clustering yang lebih baik dilihat dari jarak intercluster dan jarak intracluster dibandingkan dengan algoritma Particle Swarm Optimization (PSO) maupun algoritma K-Means saja.

## Latar Belakang
K-Means merupakan teknik mengelompokkan data dengan mempartisi data ke dalam beberapa cluster dengan menetapkan sejumlah objek data terdekatnya. Sedangkan Particle Swarm Optimization (PSO) merupakan algoritma pencarian berbasis populasi berdasarkan simulasi perilaku sosial burung dalam kawanan, Parameter dasar PSO dipengaruhi oleh sejumlah parameter kontrol, yaitu dimensi dari masalah, jumlah partikel, koefisien percepatan, berat inersia, ukuran lingkungan, jumlah iterasi, dan nilai-nilai acak yang mengukur kontribusi komponen kognitif dan selesai.

K-MEANS :
  * Hasil optimasi yang lebih rendah dibandingkan PSO
  * Proses yang lebih cepat dibandingkan PSO.

Particle Swarm Optimization :
 * Metode optimasi dengan hasil yang lebih baik dibandingkan dengan K-Means.
 * Perhitungan dan iterasi yang kompleks.

Berdasarkan dengan kelebihan dan kekurangan masing-masing algoritma, maka diperoleh sebuah ide tentang penggabungan antara K-Means dan PSO yang diharapkan mampu menghasilkan nilai yang lebih optimal dengan waktu yang lebih singkat.

## Deskripsi Dataset
Dataset yang digunakan adalah Credit Card Dataset for Clustering https://www.kaggle.com/arjunbhasin2013/ccdata  Dataset ini berisikan kebiasaan pemakaian kartu kredit dari sekitar 9000 pemegang kartu kredit. Dataset ini menunjukkan pengembangan segmentasi pelanggan untuk strategi pemasaran. Pada dataset credit card terdapat 18 variabel perilaku yang dicatat. Berikut adalah 18 variabel perilaku tersebut.

| Variabel | Deskripsi |
| --- | --- |
| CUSTID | Identitas pemegang kartu kredit |
| BALANCE | Sisa saldo di rekening mereka untuk melakukan pembelian |
| BALANCEFREQUENCY | Seberapa sering saldo diperbarui, skor antara 0 dan 1 (1 = sering diperbarui, 0 = tidak sering diperbarui) |
| PURCHASES | Jumlah pembelian yang dilakukan dari akun |
| ONEOFFPURCHASES | Jumlah pembelian maksimum yang dilakukan sekaligus |
| INSTALLMENTSPURCHASES | Jumlah pembelian yang dilakukan secara angsuran |
| CASHADVANCE | Uang muka yang diberikan oleh pengguna |
| PURCHASESFREQUENCY | Seberapa sering pembelian dilakukan, skor antara 0 dan 1 (1 = sering dibeli, 0 = tidak sering dibeli) |
| ONEOFFPURCHASESFREQUENCY | Seberapa sering pembelian terjadi dalam sekali jalan (1 = sering dibeli, 0 = tidak sering dibeli) |
| PURCHASESINSTALLMENTSFREQUENCY | Seberapa sering pembelian secara mencicil (1 = sering dilakukan, 0 = tidak sering dilakukan) |
| CASHADVANCEFREQUENCY | Seberapa sering pembayaran tunai di muka | 
| CASHADVANCETRX | Jumlah Transaksi yang dilakukan dengan |
| PURCHASESTRX | Jumlah transaksi pembelian dibuat |
| CREDITLIMIT | Batas Kartu Kredit untuk pengguna |
| PAYMENTS | Jumlah Pembayaran yang dilakukan oleh pengguna |
| MINIMUM_PAYMENTS | Jumlah pembayaran minimum yang dilakukan oleh pengguna | 
| PRCFULLPAYMENT | Persentase pembayaran penuh yang dibayarkan oleh pengguna |
| TENURE | Jangka waktu layanan kartu kredit untuk pengguna |

Terdapat beberapa kolom yang memiliki rentang nilai yang tinggi dan juga terdapat nilai NaN, sehingga perlu dilakukan normalisasi terlebih dahulu dan mengisi nilai NaN.

## Metode
Metode yang digunakan adalah kombinasi dari algoritma clustering K - means dengan algoritma optimasi Particle Swarm Optimization (PSO). 

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/57633103/146041158-4fc4982f-46f1-4f3c-b743-6514eea69f7b.png">
  <p align="center">Flowchart Algoritma Clustering K - Means</p>
</p>

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/57633103/146041153-16bf2cdc-1239-4d6b-85da-2cbd36a1d195.png">
  <p align="center">Flowchart Algoritma Optimasi Particle Swarm Optimization</p>
</p>

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/57633103/146041144-9c740efe-f32b-46ea-bc27-48aeaa77fe47.png">
  <p align="center">Flowchart Algoritma Hybrid PSO dan K - Means</p>
</p>

## Hasil dan Analisis Ujicoba
Sebelum melakukan perhitungan pada algoritma K-Means, PSO, dan Hybrid, perlu dilakukan pengolahan data untuk mengatasi rentang nilai yang tinggi dan nilai NaN. Cara ini dilakukan dengan menggunakan fungsi drop dan fillna. Kemudian dilakukan scaling

sehingga semua nilai pada data sekarang ada pada rentang 0 sampai 1 dan dataset sudah siap untuk dijadikan bahan perhitungan. Setelah dataset siap, maka dilakukan pencarian jumlah cluster dengan elbow method

dan diperoleh diagram seperti berikut:
<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/57633103/146044463-8eef2524-ad5d-4443-9ead-75168e3ea091.png">
</p>

Berdasarkan diagram tersebut, kami menyimpulkan bahwa jumlah cluster terbaik adalah 3. Sehingga pada perhitungan seterusnya kami menggunakan jumlah cluster (n_cluster)) adalah 3.

Hasil dari percobaan ini berupa nilai rata-rata dari silhouette, sse, dan quantization error pada algoritma K-Means, PSO, dan PSO hybrid. Dalam melakukan uji coba, kami melakukan beberapa jenis percobaan dengan perbedaan jumlah cluster dan max iterasi. Berikut adalah hasil-hasil dari uji coba yang telah kami lakukan.

Hasil uji coba pertama 
| Method | sse_mean | silhouette_mean | quantization_mean |
| :---: | :---: | :---: | :---: |
| K-Means | 2624.734878 | 0.349388 | 0.494564 |
| PSO | 3514.362230 | 0.233380 | 0.517694 |
| Hybrid | 2577.767544 | 0.369812 | 0.506792 |


Hasil uji coba kedua 
| Method | sse_mean | silhouette_mean | quantization_mean |
| :---: | :---: | :---: | :---: |
| K-Means | 2624.733750 | 0.349442 | 0.494586 |
| PSO | 3781.463981 | 0.219026 | 0.513557 |
| Hybrid | 2526.513200 | 0.382203 | 0.502800 |


Hasil uji coba ketiga
| Method | sse_mean | silhouette_mean | quantization_mean |
| :---: | :---: | :---: | :---: |
| K-Means | 2624.734878 | 0.349388 | 0.494564 |
| PSO | 3514.362230 | 0.233380 | 0.517694 |
| Hybrid | 2639.739567 | 0.360798 | 0.510013 |

Dari 3 kali uji coba dengan data yang sama dan metode yang sama diperoleh hasil untuk sse_mean terkadang mengalami optimasi dan terkadang justru mengalami hasil yang kurang baik sedangkan untuk silhoutte_mean mengalami optimasi yang cukup memuaskan. Dari hasil uji coba diatas juga dapat diperoleh hasil perhitungan yang tidak stabil.

## Kesimpulan dan Saran
Kesimpulan yang dapat diperoleh dari hasil analisis diatas adalah kombinasi antara k-means dan pso menghasilkan nilai silhouette dan sse yang lebih optimal dibandingkan algoritma K-Means dan PSO tanpa kombinasi. Akan tetapi hasil dari perhitungan algoritma K-Means dengan PSO tidak stabil yang berarti setiap menjalankan ulang perhitungan, hasil yang diperoleh mengalami perubahan. Saran yang dapat kami berikan adalah dengan memperbaiki algoritma kombinasi sehingga hasil perhitungan lebih stabil dengan jumlah iterasi yang beragam.

## Referensi 
https://sci-hub.se/https://ieeexplore.ieee.org/document/1299577 
https://towardsdatascience.com/data-normalization-with-pandas-and-scikit-learn-7c1cc6ed6475 
https://www.kaggle.com/arjunbhasin2013/ccdata
