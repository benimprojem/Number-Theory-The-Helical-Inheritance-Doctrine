
# **Sayıların Primorial Mimari ve Konik Miras Doktrini: Formül ve Simülasyon**

## **1. Konsept ve Temel İdealar**

* Sayılar doğrusal değil, **genişleyen bir ters koni** üzerinde hiyerarşik katmanlarla yerleşir.
* **Zirve (tepe):** küçük asallar (2,3,5…) bulunur, en dar ve yoğun bölge.
* **Dikey miras hattı (Mod0):** koninin tepesinden tabana uzanan koordinat çizgileri. Bir sayı bu hattı takip ediyorsa “mirasçısı” olur.
* **Gap ve rezonans:** Küçük asalların miras hattı üst üste geldiğinde yeni asal için “temiz koordinat” azalır, büyük gapler oluşur.

---

## **2. Matematiksel Formülizasyon**

### 2.1 Miras Başlangıcı

[
M_0(p) = p^2
]

### 2.2 Zıplama Ritimleri

[
M_i(p) = p^2 + \sum_{j=1}^{i} \Delta_j(p), \quad
\Delta_j(p) =
\begin{cases}
2p & j \text{ tek} \
4p & j \text{ çift}
\end{cases}
]

### 2.3 Kolon İndeksi

[
c(n) = n \bmod ML_n, \quad ML_n = \prod_{k=1}^{n} p_k
]

* Kolon stabilizasyonu: Eğer (ML_n \equiv 0 \pmod{p}), dikey hat bozulmaz.

### 2.4 Bileşik Kolon Fonksiyonu

[
B(n) =
\begin{cases}
1 & \exists p \le \sqrt{n}: n \in {M_i(p)} \
0 & \text{aksi halde}
\end{cases}
]

### 2.5 I(n) Yoğunluğu

[
I(n) = \sum_{p \le \sqrt{n}} \mathbf{1}_{{n \in \text{mirashattı}(p)}}
]

* Asallık olasılığı tahmini:
  [
  \mathbb{P}(\text{asal } n) \approx f(I(n)) = e^{-I(n)}
  ]

### 2.6 Kolon Boşlukları

[
ML_{n+1} = p_{n+1} \cdot ML_n
]
[
c_{n+1} = c_n + k \cdot p_{n+1} \pmod{ML_{n+1}}
]

---

## **3. Python Simülasyonu**

Aşağıdaki kod:

* Primorial matrisini oluşturur
* Miras hatlarını (I(n)) hesaplar
* Bileşik kolonları belirler
* Asal olasılığı tahmini çıkarır
* Gap ve kolon yoğunluk tablolarını üretir

```python
import math

# Parametreler
N = 50000        # hesaplanacak sayı üst sınırı
primes = [2,3,5,7,11,13,17,19,23,29]  # Primorial katları
ML_n = math.prod(primes)  # Primorial matrisi
I_values = [0]*(N+1)
is_prime = [True]*(N+1)
is_prime[0] = is_prime[1] = False

# 1. Sieve ile asal belirle
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False

# 2. Miras hesaplama (I(n))
for p in primes:
    p2 = p*p
    i = 0
    while p2 + i*2*p <= N:
        idx = p2 + i*2*p
        if idx <= N:
            I_values[idx] += 1
        idx2 = p2 + i*4*p
        if idx2 <= N:
            I_values[idx2] += 1
        i += 1

# 3. Bileşik kolon tespiti
B = [0]*(N+1)
for n in range(2, N+1):
    for p in primes:
        if n >= p*p and (n - p*p) % p == 0:
            B[n] = 1
            break

# 4. Asallık olasılığı tahmini
P_asal = [0]*(N+1)
for n in range(2, N+1):
    P_asal[n] = math.exp(-I_values[n])

# 5. Gap ve kolon yoğunluğu tabloları
gap_lengths = []
current_gap = 0
for n in range(2, N+1):
    if is_prime[n]:
        gap_lengths.append(current_gap)
        current_gap = 0
    else:
        current_gap += 1

# Kolon yoğunluğu
Mk = 30
from math import gcd
colon_data = {}
for r in range(Mk):
    if gcd(r,Mk)==1:
        colon_data[r] = [0,0,0]  # toplam, asal, I toplam

for n in range(2,N+1):
    r = n % Mk
    if r in colon_data:
        colon_data[r][0] +=1
        colon_data[r][2] += I_values[n]
        if is_prime[n]:
            colon_data[r][1] +=1

# Örnek çıktı
print("n\tI(n)\tBileşik\tP(asal)")
for n in range(2,51):
    print(f"{n}\t{I_values[n]}\t{B[n]}\t{P_asal[n]:.5f}")

print("\nKolon yoğunluğu örnek:")
for r in sorted(colon_data):
    total, prime, I_sum = colon_data[r]
    print(f"Kolon {r}: yoğunluk={prime/total:.4f}, avg I={I_sum/total:.3f}")

print("\nBüyük gap (>20) örnek:", [g for g in gap_lengths if g>20][:10])

input("Kapat")
```

---
