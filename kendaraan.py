class Kendaraan(object):
    nama = None
    def __init__(self, nama):
        self.nama = nama
    def jalan(self):
        print('{} sedang melaju di jalan'.format(self.nama))
class KendaraanSport(Kendaraan):
    merek = None
    kecepatan = 0
    def __init__(self, nama, merek):
        self.nama = nama
        self.merek = merek
    def set_kecepatan(self, kecepatan):
        self.kecepatan = kecepatan
    def jalan(self):
        print('{} dengan merek {} melaju dengan kecepatan {} km/jam'.format(
            self.nama, self.merek, self.kecepatan))
# Contoh objek
mobil = KendaraanSport('Mobil', 'Pajero')
mobil.set_kecepatan(300)
mobil.jalan()
motor = KendaraanSport('Motor', 'Beat')
motor.set_kecepatan(100)
motor.jalan()