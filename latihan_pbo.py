class manusia(object):
    nama = None
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print('{} makan nasi'.format(self.nama))

class manusiamilenial(manusia):
    nama = None
    email = None
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print('{} makan nasi'.format(self.nama))
    def set_email(self, email):
        self.email = email
programmer = manusiamilenial('eka')
programmer.set_email('eka@test.com')
programmer.makan()
petani = manusiamilenial('putra')
petani.set_email('putrs@test.com')
petani.makan()                          