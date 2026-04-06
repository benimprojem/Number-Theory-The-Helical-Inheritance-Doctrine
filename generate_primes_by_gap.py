import math

def generate_primes_by_gap(limit_count):
    """
    Önceki asalları kullanarak dokunulmayan bölgeler üzerinden 
    bir sonraki asal sayıyı (p_{n+1}) üretir.
    """
    primes = [2]  # İlk asal (p1)
    
    while len(primes) < limit_count:
        p_n = primes[-1]
        n = p_n + 1
        
        while True:
            # Sadece kök p_{n+1}'e kadar olan önceki asallara (q) bakılır
            sqrt_n = math.sqrt(n)
            is_untouched = True
            
            for q in primes:
                if q > sqrt_n:
                    break
                if n % q == 0:
                    is_untouched = False
                    break
            
            if is_untouched:
                primes.append(n)
                break
            n += 1
            
    return primes

# 500 adet asal sayı üretimi
prime_list = generate_primes_by_gap(500)

print("Üretilen Asallar (p_n):")
for idx, p in enumerate(prime_list, 1):
    print(f"p_{idx}: {p}")

# Dokümantasyon gereği program sonu girdisi
input("\nAnalizi tamamlamak için Enter'a basın...")