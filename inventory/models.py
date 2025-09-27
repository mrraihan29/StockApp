from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # CharField adalah untuk teks dengan panjang terbatas. `max_length` wajib diisi.
    # `unique=True` memastikan tidak ada nama produk yang sama.
    nama_produk = models.CharField(max_length=100)
    
    # IntegerField untuk menyimpan angka bulat (lead time dalam hari).
    waktu_tunggu_hari = models.IntegerField()
    
    # DateTimeField menyimpan tanggal dan waktu. `auto_now_add=True` otomatis mengisi
    # waktu saat produk pertama kali dibuat dan tidak akan berubah.
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    # Ini adalah fungsi khusus agar nama objek lebih mudah dibaca (misal: di admin panel).
    def __str__(self):
        return self.nama_produk
      
class TransaksiStok(models.Model):
    # Kita membuat pilihan (choices) untuk jenis transaksi agar data konsisten.
    class Jenis(models.TextChoices):
      MASUK = 'MASUK', 'Masuk'
      KELUAR = 'KELUAR', 'Keluar'
    
    # ForeignKey adalah cara membuat relasi antar tabel.
    # `on_delete=models.CASCADE` berarti jika sebuah produk dihapus,
    # semua transaksinya juga akan ikut terhapus.
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Berelasi dengan model User bawaan Django untuk melacak siapa yang input.
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # Menggunakan pilihan yang kita definisikan di atas
    jenis_transaksi = models.CharField(max_length=10, choices=Jenis.choices)
    
    # Jumlah produk dalam transaksi ini
    jumlah = models.IntegerField()
    
    # `auto_now_add=TRUE` untuk mencatat waktu transaksi dibuat
    tanggal_transaksi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return f"{self.produk.nama_produk} - {self.jenis_transaksi} ({self.jumlah})"

# Model ini merepresentasikan tabel 'Laporan' kita.
class Laporan(models.Model):
  # Berelasi dengan User, siapa yang membuat laporan
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  
  # Relasi ke Produk, tapi bisa NULL (opsional)
  # `null=TRUE` menginzinkan nilai NULL di database
  # `blank=TRUE` menginzinkan field ini kosong di form
  produk = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
  
  judul_laporan = models.CharField(max_length=200)
  
  # Teks panjang untuk isi laporan yang tidak terbatas
  isi_laporan = models.TextField()
  
  tanggal_laporan = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.judul_laporan