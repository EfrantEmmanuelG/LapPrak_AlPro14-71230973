import re
from datetime import datetime

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""
tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
sekarang = datetime.now()
for date_str in tanggal:
    objek = datetime.strptime(date_str, '%Y-%m-%d')
    formattanggal = objek.strftime('%d-%m-%Y')
    perbedaan = (sekarang - objek).days
    print(f"{objek} selisih {perbedaan} hari")
