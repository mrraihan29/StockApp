# inventory/admin.py

from django.contrib import admin
from .models import Product, TransaksiStok, Laporan

# Kustomisasi untuk model Produk
@admin.register(Product)
class ProdukAdmin(admin.ModelAdmin):
    # Tampilkan kolom-kolom ini di daftar produk
    list_display = ('nama_produk', 'waktu_tunggu_hari', 'tanggal_dibuat')
    # Tambahkan kotak pencarian berdasarkan nama produk
    search_fields = ('nama_produk',)

# Kustomisasi untuk model TransaksiStok
@admin.register(TransaksiStok)
class TransaksiStokAdmin(admin.ModelAdmin):
    # Tampilkan kolom-kolom ini
    list_display = ('produk', 'jenis_transaksi', 'jumlah', 'user', 'tanggal_transaksi')
    # Tambahkan filter di sidebar kanan
    list_filter = ('jenis_transaksi', 'produk')
    # Cari berdasarkan nama produk (menggunakan relasi ForeignKey)
    search_fields = ('produk__nama_produk',)

# Kustomisasi untuk model Laporan
@admin.register(Laporan)
class LaporanAdmin(admin.ModelAdmin):
    list_display = ('judul_laporan', 'produk', 'user', 'tanggal_laporan')
    list_filter = ('produk', 'user')
    search_fields = ('judul_laporan', 'isi_laporan')