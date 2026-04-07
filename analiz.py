# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

N = 50000       # hesaplanacak sayı üst sınırı
Mk = 30
GAP_THRESHOLD = 20

# ---------------------------
# 1. ASAL SIEVE
# ---------------------------
is_prime = [True]*(N+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False
primes = [i for i in range(2,N+1) if is_prime[i]]

# ---------------------------
# 2. INTERFERENCE I(n)
# ---------------------------
I_values = [0]*(N+1)
for p in primes:
    for j in range(p, N+1, p):
        I_values[j] += 1

# ---------------------------
# 3. GAP ANALIZI
# ---------------------------
gap_lengths = []
current_gap = 0
for n in range(2, N+1):
    if is_prime[n]:
        gap_lengths.append(current_gap)
        current_gap = 0
    else:
        current_gap +=1
large_gaps = [g for g in gap_lengths if g>GAP_THRESHOLD]

# ---------------------------
# 4. KOLON ANALIZI
# ---------------------------
from math import gcd
colon_data = {}
for r in range(Mk):
    if gcd(r,Mk)==1:
        colon_data[r] = [0,0,0]  # [toplam sayı, asal sayısı, I toplam]

for n in range(2, N+1):
    r = n % Mk
    if r in colon_data:
        colon_data[r][0] += 1
        colon_data[r][2] += I_values[n]
        if is_prime[n]:
            colon_data[r][1] += 1

# ---------------------------
# 5. I(n) VS P(asal|I)
# ---------------------------
P_asal_I = {}
for n in range(2, N+1):
    I = I_values[n]
    prob = (1/math.log(n))*math.exp(-I)
    P_asal_I[n] = prob

# I bazlı tablo
bins = {}
for n in range(2,N+1):
    I = I_values[n]
    if I not in bins:
        bins[I] = [0,0]  # [toplam, asal]
    bins[I][0] += 1
    if is_prime[n]:
        bins[I][1] += 1

empirical_probs = []
estimated_probs = []
I_bins = []
for I in sorted(bins):
    total, prime = bins[I]
    empirical_probs.append(prime/total if total else 0)
    est_avg = sum([P_asal_I[n] for n in range(2,N+1) if I_values[n]==I])/total
    estimated_probs.append(est_avg)
    I_bins.append(I)

# ---------------------------
# 6. GRAFİKLER
# ---------------------------
plt.figure(figsize=(12,8))

# I(n) dağılımı histogramı
plt.subplot(2,2,1)
plt.hist(I_values[2:], bins=range(0,max(I_values)+2), color='skyblue', edgecolor='black')
plt.title("I(n) Dağılım Histogramı")
plt.xlabel("I(n)")
plt.ylabel("Sayı adedi")

# I(n) bazlı P(asal) karşılaştırması
plt.subplot(2,2,2)
plt.plot(I_bins, empirical_probs, 'o-', label="Empirik P(asal|I)")
plt.plot(I_bins, estimated_probs, 'x-', label="Tahmini P(asal|I)")
plt.title("I(n) Bazlı Asal Olasılığı")
plt.xlabel("I(n)")
plt.ylabel("P(asal|I)")
plt.legend()

# Kolon yoğunlukları histogramı
plt.subplot(2,2,3)
colon_labels = []
densities = []
for r in sorted(colon_data):
    total, prime, I_sum = colon_data[r]
    density = prime/total
    densities.append(density)
    colon_labels.append(str(r))
plt.bar(colon_labels, densities, color='orange', edgecolor='black')
plt.title("Kolon Yoğunluğu")
plt.xlabel("Kolon r mod %d"%Mk)
plt.ylabel("Asal Yoğunluğu")

# Büyük gap histogramı
plt.subplot(2,2,4)
plt.hist(large_gaps, bins=range(GAP_THRESHOLD, max(large_gaps)+2), color='lightgreen', edgecolor='black')
plt.title("Büyük Gap Histogramı (> %d)"%GAP_THRESHOLD)
plt.xlabel("Gap Uzunluğu")
plt.ylabel("Sayı adedi")

plt.tight_layout()
plt.show()