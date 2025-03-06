**TUGAS PERTEMUAN 1 LOGIKA INFORMATIKA**

**Nama : Felix Amon Sitinjak**

**NIM : 312410063**

**Kelas : TI.24.A1**

1. Sebuah jasa pengiriman memiliki aturan biaya yang bergantung pada beberapa faktor. Biaya dasar pengiriman ditetapkan sebesar Rp 10.000.
Jika berat paket melebihi 5 kg, maka akan dikenakan tambahan biaya sebesar Rp 5.000. Selain itu, jika jarak pengiriman lebih dari 10 km, maka ada tambahan biaya sebesar Rp 8.000. 
Jika pelanggan memilih layanan pengiriman express, maka akan dikenakan tambahan biaya sebesar Rp 20.000. Namun, jika pelanggan merupakan member, mereka akan mendapatkan diskon 10% dari total biaya pengiriman yang dihitung sebelum diskon. 

Buatlah sebuah fungsi dalam Python yang dapat menghitung total biaya pengiriman berdasarkan aturan tersebut, dengan parameter berat paket, jarak pengiriman, jenis pengiriman (biasa atau express), serta status keanggotaan pelanggan (member atau non-member).

**Code**

<img width="959" alt="image" src="https://github.com/user-attachments/assets/35d49873-0b8b-4205-a4f6-8d3a591f69c8" />

```
def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, is_member):
    """
    Fungsi untuk menghitung total biaya pengiriman berdasarkan beberapa faktor.

    Parameter:
    - berat (float): Berat paket dalam kilogram.
    - jarak (float): Jarak pengiriman dalam kilometer.
    - jenis_pengiriman (str): Jenis pengiriman, bisa "biasa" atau "express".
    - is_member (bool): Status keanggotaan pelanggan, True jika member, False jika non-member.

    Output:
    - int: Total biaya pengiriman setelah mempertimbangkan semua faktor.
    """

    # 1. Biaya dasar pengiriman
    total_biaya = 10000

    # 2. Tambahan biaya jika berat melebihi 5 kg
    if berat > 5:
        total_biaya += 5000  # Tambahan Rp 5.000

    # 3. Tambahan biaya jika jarak lebih dari 10 km
    if jarak > 10:
        total_biaya += 8000  # Tambahan Rp 8.000

    # 4. Tambahan biaya jika menggunakan layanan express
    if jenis_pengiriman.lower() == "express":  # Konversi ke huruf kecil untuk menghindari kesalahan input
        total_biaya += 20000  # Tambahan Rp 20.000

    # 5. Diskon 10% jika pelanggan adalah member
    if is_member:
        total_biaya *= 0.9 # Potongan 10%

    return int(total_biaya)  # Mengembalikan nilai dalam bentuk integer agar tidak ada desimal

# =====================================================
# Program Utama (Meminta Input dari Pengguna)
# =====================================================
if __name__ == "__main__":
    print("=== Program Perhitungan Biaya Pengiriman ===")

    # 1. Memasukkan berat paket
    while True:
        try:
            berat_paket = float(input("Masukkan berat paket (kg): "))
            if berat_paket < 0:
                print("Berat paket tidak bisa negatif. Silakan masukkan kembali.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    # 2. Memasukkan jarak pengiriman
    while True:
        try:
            jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
            if jarak_pengiriman < 0:
                print("Jarak tidak bisa negatif. Silakan masukkan kembali.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    # 3. Memasukkan jenis pengiriman (biasa/express)
    while True:
        jenis_pengiriman = input("Masukkan jenis pengiriman (biasa/express): ").strip().lower()
        if jenis_pengiriman not in ["biasa", "express"]:
            print("Jenis pengiriman hanya bisa 'biasa' atau 'express'. Silakan masukkan kembali.")
        else:
            break

    # 4. Memasukkan status keanggotaan pelanggan (member atau bukan)
    while True:
        is_member_input = input("Apakah pelanggan member? (ya/tidak): ").strip().lower()
        if is_member_input in ["ya", "tidak"]:
            is_member = is_member_input == "ya"
            break
        else:
            print("Harap masukkan 'ya' atau 'tidak'.")

    # 5. Menghitung biaya pengiriman
    biaya = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, is_member)

    # 6. Menampilkan hasil
    print("\n=== Rincian Biaya Pengiriman ===")
    print(f"Berat paket         : {berat_paket} kg")
    print(f"Jarak pengiriman    : {jarak_pengiriman} km")
    print(f"Jenis pengiriman    : {jenis_pengiriman.capitalize()}")
    print(f"Status Member       : {'Ya' if is_member else 'Tidak'}")
    print(f"Total Biaya Pengiriman: Rp {biaya:,.0f}")

```


**Output**

<img width="786" alt="image" src="https://github.com/user-attachments/assets/a2f96ab4-4218-443f-a23e-336d94381059" />
