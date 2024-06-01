import re
import random
import string

teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', teks)

def mengacak(length=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for i in range(length))

for email in emails:
    username = email.split('@')[0]
    password = mengacak()
    print(f"{email} username: {username} , password: {password}")
