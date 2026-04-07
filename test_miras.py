import MirasLib as ml
import time

def tam_protokol_testi():
    try:
        doktrin = ml.MirasLib()
        print("✅ MirasLib Doktrin Motoru Hazır.\n")
    except Exception as e:
        print(f"❌ Yükleme Hatası: {e}")
        return
    # Ritmik Operatör Doğrulama
    sayilar = [25, 35, 49, 91, 121, 1031]
    for s in sayilar:
        print(f"Sayı: {s} | Miras Testi: {'ASAL' if doktrin.is_prime_helical(s) else 'BİLEŞİK'}")
        
    # --- TEST 1: Asal Üretimi ---
    print("\n\n3.--- Asal Sayı Üretimi (p_n) ---")
    prime_list = doktrin.generate_primes(50)
    for idx, p in enumerate(prime_list, 1):
        print(f"p{idx}: {p}", end=" | " if idx % 5 != 0 else "\n")

    # Bilimsel İstatistik Analizi 
    print("\n\n3.--- Asal Sayı Analiz  ---")
    doktrin.analyze_stats(N=30000, Mk=30)

    # --- TEST 2: 2D Matris ---
    print("\n\n3. Görsel: Level 7 Matrisi (210 Sütun)")
    doktrin.visualize_matrix_2d_blocks(level_p=7, rows=50)

    # --- TEST 3: 3D Ters Koni ---
    print("\n5. Görsel: 3D Ters Koni (Vazo Modeli)")
    doktrin.visualize_helix_3d_vase(limit=1500, target_p=7)

if __name__ == "__main__":
    start_time = time.time()
    try:
        tam_protokol_testi()
        print(f"\n✅ İşlemler {time.time() - start_time:.2f} saniyede tamamlandı.")
    except Exception as e:
        print(f"\n❌ KRİTİK HATA: {e}")
    input("\nKapatmak için Enter'a basın...")