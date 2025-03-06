def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member):
    
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
    print("mesin paket shopee1212")

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
