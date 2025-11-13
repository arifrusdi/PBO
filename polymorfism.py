class Pegawai:
    """Kelas dasar untuk semua pegawai."""
    def __init__(self, nama):
        self.nama = nama

    def hitung_gaji(self):
        """
        Metode ini harus diimplementasikan oleh setiap subkelas.
        Ini adalah antarmuka polimorfik.
        """
        raise NotImplementedError("Subkelas harus mengimplementasikan metode abstrak 'hitung_gaji'")

    def tampilkan_info(self):
        return f"Nama: {self.nama}"

class PegawaiPenuhWaktu(Pegawai):
    """Kelas untuk pegawai penuh waktu dengan gaji bulanan."""
    def __init__(self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        """Menghitung gaji (bulanan) untuk pegawai penuh waktu."""
        return self.gaji_bulanan

class Kontraktor(Pegawai):
    """Kelas untuk kontraktor yang dibayar per jam."""
    def __init__(self, nama, tarif_per_jam, jam_kerja):
        super().__init__(nama)
        self.tarif_per_jam = tarif_per_jam
        self.jam_kerja = jam_kerja

    def hitung_gaji(self):
        """Menghitung gaji (total) untuk kontraktor."""
        return self.tarif_per_jam * self.jam_kerja

# --- Demonstrasi Polimorfisme ---

# Membuat daftar objek dari kelas yang berbeda
daftar_pegawai = [
    PegawaiPenuhWaktu("Budi Santoso", 8000000),
    Kontraktor("Ani Permata", 150000, 160), # 150 ribu per jam, 160 jam kerja
    PegawaiPenuhWaktu("Citra Dewi", 12000000)
]

print("--- Daftar Gaji Pegawai ---")
for pegawai in daftar_pegawai:
    # Karena semua objek (PegawaiPenuhWaktu dan Kontraktor)
    # adalah turunan dari Pegawai dan mengimplementasikan hitung_gaji(),
    # kita dapat memanggil metode hitung_gaji() pada setiap objek
    # secara seragam, meskipun implementasinya berbeda (polimorfisme).
    gaji = pegawai.hitung_gaji()

    # Menggunakan metode umum dan metode spesifik
    print(f"{pegawai.tampilkan_info()} - Jenis Pegawai: {type(pegawai).__name__}")
    print(f"Gaji Dihitung: Rp {gaji:,.2f}\n")
