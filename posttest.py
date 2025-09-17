class Main:
    def __init__(self):
        pass

    def main(self):
        pass

    def uLogin(self):
        pass

    def uMenu(self):
        pass

    def uHitungPembayaran(self):
        pass

    def uCetakStruk(self):
        pass


class HitungPembayaran:
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0, totalHarga=0.0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass

    def deleteDataPembayaran(self):
        pass

    def cariDataPembayaranByMenu(self):
        pass


class PembayaranTunai(HitungPembayaran):
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0, totalHarga=0.0):
        super().__init__(idMenu, namaMenu, harga, jumlah, totalHarga)

    def hitungTotalHarga(self):
        pass


class PembayaranByCard(HitungPembayaran):
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0, totalHarga=0.0):
        super().__init__(idMenu, namaMenu, harga, jumlah, totalHarga)

    def hitungTotalHarga(self):
        pass


class TabelHitungPembayaran:
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0, totalHarga=0.0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self, idMenu):
        pass

    def getIdMenu(self):
        pass

    def setNamaMenu(self, namaMenu):
        pass

    def getNamaMenu(self):
        pass

    def setHarga(self, harga):
        pass

    def getHarga(self):
        pass

    def setJumlah(self, jumlah):
        pass

    def getJumlah(self):
        pass

    def setTotalHarga(self, totalHarga):
        pass

    def getTotalHarga(self):
        pass


class TabelPembayaranByCard:
    def __init__(self, idCard="", jenisCard="", namaBank="", totalHarga=0.0):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self, idCard):
        pass

    def getIdCard(self):
        pass

    def setJenisCard(self, jenisCard):
        pass

    def getJenisCard(self):
        pass

    def setNamaBank(self, namaBank):
        pass

    def getNamaBank(self):
        pass

    def setTotalHarga(self, totalHarga):
        pass

    def getTotalHarga(self):
        pass


class CetakStruk:
    def __init__(self):
        pass

    def cetakStruk(self):
        pass


class TCetakStruk:
    def __init__(self, noStruk="", totalHarga=0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


class LoginKasir:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host="", database="", username="", password=""):
        self.host = host
        self.database = database
        self.username = username
        self.password = password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass

mainApp = Main()
hitung = HitungPembayaran("M01", "Nasi Padang", 20000, 2, 40000)
tunai = PembayaranTunai("M02", "Nasi Goreng", 25000, 1, 25000)
byCard = PembayaranByCard("M03", "Ayam Bakar", 30000, 3, 90000)
tabelHitung = TabelHitungPembayaran("M01", "Nasi Padang", 20000, 2, 40000)
tabelCard = TabelPembayaranByCard("C01", "Debit", "Bank BTN", 25000)
cetak = CetakStruk()
tCetak = TCetakStruk("STRK01", 100000)
kasir = LoginKasir("admin", "1234")
koneksi = KoneksiDatabase("localhost", "db_kasir", "root", "")