## LOGIKA INFORMATIKA

**Nama : RO'UF MUHAMMAD FAUZAN**

**NIM : 312410157**

**Kelas : TI.24.A1**

1. Sebuah jasa pengiriman memiliki aturan biaya yang bergantung pada beberapa faktor. Biaya dasar pengiriman ditetapkan sebesar Rp 10.000.
Jika berat paket melebihi 5 kg, maka akan dikenakan tambahan biaya sebesar Rp 5.000. Selain itu, jika jarak pengiriman lebih dari 10 km, maka ada tambahan biaya sebesar Rp 8.000. 
Jika pelanggan memilih layanan pengiriman express, maka akan dikenakan tambahan biaya sebesar Rp 20.000. Namun, jika pelanggan merupakan member, mereka akan mendapatkan diskon 10% dari total biaya pengiriman yang dihitung sebelum diskon. 

Buatlah sebuah fungsi dalam Python yang dapat menghitung total biaya pengiriman berdasarkan aturan tersebut, dengan parameter berat paket, jarak pengiriman, jenis pengiriman (biasa atau express), serta status keanggotaan pelanggan (member atau non-member).

### Code
```python
ef hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member):
    
    biaya_dasar = 10000 
    
    biaya_berat = 0
    if berat > 5:
        biaya_berat = 5000
    
    biaya_jarak = 0
    if jarak > 10:
        biaya_jarak = 8000
    
    biaya_express = 0
    if jenis_pengiriman == 'express':
        biaya_express = 20000
    
    total_biaya = biaya_dasar + biaya_berat + biaya_jarak + biaya_express
    
    if status_member == 'member':
        total_biaya *= 0.9
    
    return total_biaya

def input_pengguna():
    print("mesin paket")

    berat = float(input("Masukkan berat paket (kg): "))
    
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    
    print("Pilih jenis pengiriman:")
    print("1. Biasa")
    print("2. Express")
    pilihan_jenis = input("Masukkan pilihan (1 atau 2): ")
    jenis_pengiriman = 'express' if pilihan_jenis == '2' else 'biasa'
    
    print("Pilih status keanggotaan:")
    print("1. Member")
    print("2. Non-Member")
    pilihan_status = input("Masukkan pilihan (1 atau 2): ")
    status_member = 'member' if pilihan_status == '1' else 'non-member'
    
    total_biaya = hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member)
    print(f"Total biaya pengiriman: Rp {total_biaya:.2f}")

input_pengguna()
```
### Output
```
mesin paket
Masukkan berat paket (kg): 20
Masukkan jarak pengiriman (km): 30
Pilih jenis pengiriman:
1. Biasa
2. Express
Masukkan pilihan (1 atau 2): 2
Pilih status keanggotaan:
1. Member
2. Non-Member
Masukkan pilihan (1 atau 2): 1
Total biaya pengiriman: Rp 38700.00
```
