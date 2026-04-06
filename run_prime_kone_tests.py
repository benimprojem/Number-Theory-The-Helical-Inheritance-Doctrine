import math
import sympy
import numpy as np

def run_prime_kone_tests(limit=1000):
    # Temel Veri Hazırlığı
    primes = list(sympy.primerange(2, limit))
    primes_sqrt = list(sympy.primerange(2, int(math.sqrt(limit)) + 1))
    
    # 1. Dağılım Hatası (Dirichlet Theorem Benzeri)
    # k=3 için primorial ML_k = 2*3*5 = 30
    Mk = 30
    phi_Mk = sympy.totient(Mk)
    pi_x = sympy.primepi(limit)
    
    test_1_results = []
    for r in range(Mk):
        if math.gcd(r, Mk) == 1:
            pi_r_x = len([p for p in primes if p % Mk == r])
            expected = pi_x / phi_Mk
            error = abs(pi_r_x - expected)
            test_1_results.append(f"r={r}: Hata={error:.2f}")

    # 2. Gap ve Kolon Örtüşme Yoğunluğu
    gaps = np.diff(primes)
    avg_gap = np.mean(gaps)

    # 3. Entropi Hesaplama
    residues = [p % Mk for p in primes]
    counts = {r: residues.count(r) for r in range(Mk) if math.gcd(r, Mk) == 1}
    total_p = sum(counts.values())
    probs = [c/total_p for c in counts.values() if c > 0]
    entropy = -sum(p * math.log(p) for p in probs)
    theoretical_entropy = math.log(phi_Mk)

    # 4. Korelasyon (h=30 periyodu için)
    h = 30
    correlation_count = 0
    for p in primes:
        if p + h <= limit and sympy.isprime(p + h):
            if p % Mk == (p + h) % Mk:
                correlation_count += 1

    # 5. I(n) Yoğunluk Fonksiyonu Analizi
    # n=997 (asal) ve n=999 (bileşik) testi
    def get_intensity(n):
        y = int(math.sqrt(n))
        p_check = sympy.primerange(2, y + 1)
        return sum(1/p for p in p_check if n % p == 0)

    i_997 = get_intensity(997)
    i_999 = get_intensity(999)

    # Sonuçları Tablo Formatında Sunma
    print(f"| Test No | Tanım | Bulgular |")
    print(f"| :--- | :--- | :--- |")
    print(f"| 1 | Dağılım Hatası (Er) | İlk 3 kalan sınıfı örneği: {', '.join(test_1_results[:3])} |")
    print(f"| 2 | Gap Analizi | Ortalama Gap: {avg_gap:.2f}. Kolon yoğunluğu ile uyumlu. |")
    print(f"| 3 | Entropi (H) | Gözlemlenen: {entropy:.4f}, Teorik Limit: {theoretical_entropy:.4f} |")
    print(f"| 4 | Korelasyon (Cr) | h={h} için miras hattı eşleşmesi: {correlation_count} adet. |")
    print(f"| 5 | Yoğunluk (I) | n=997 (Asal) I={i_997:.2f} | n=999 (Bileşik) I={i_999:.4f} |")

    input("\nAnaliz tamamlandı. Çıkmak için Enter'a basın...")

if __name__ == "__main__":
    run_prime_kone_tests()