import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import math
from math import gcd

class MirasLib:
    def __init__(self):
        # Primorial Seviyeleri (MLn) - Matris Genişlikleri
        self.levels = {1: 1, 2: 2, 3: 6, 5: 30, 7: 210, 11: 2310, 13: 30030, 17: 510510}

    # --- 1. ÇEKİRDEK OPERATÖRLER ---
    def get_ritim_sabiti(self, p):
        return 2 * p if p % 6 == 5 else 4 * p
    
    def get_intensity(self, n):
        """I(n) Yoğunluğu: Sayı üzerindeki miras hatlarının (vuruşların) sayısı."""
        if n < 2: return 0
        count = 0
        if n % 2 == 0: count += 1
        if n % 3 == 0: count += 1
        limit = int(n**0.5)
        p = 5
        while p <= limit:
            r = self.get_ritim_sabiti(p)
            d = n - p**2
            if d >= 0 and ((d % (6 * p)) == 0 or (d % (6 * p)) == r):
                count += 1
            p += 2 if p % 6 == 5 else 4
        return count

    def is_prime_helical(self, n):
        """Ritmik Operatör: Sayının hiçbir miras hattına yakalanmadığını test eder."""
        if n < 2: return False
        if n in (2, 3): return True
        if n % 2 == 0 or n % 3 == 0: return False
        limit = int(n**0.5)
        p = 5
        while p <= limit:
            r = self.get_ritim_sabiti(p)
            d = n - p**2
            if d >= 0:
                if (d % (6 * p)) == 0 or (d % (6 * p)) == r:
                    return False
            p += 2 if p % 6 == 5 else 4
        return True
    
    def generate_primes(self, limit_count=50): # DÜZELTME: self eklendi
        primes = [2]
        while len(primes) < limit_count:
            p_n = primes[-1]
            n = p_n + 1
            while True:
                sqrt_n = math.sqrt(n)
                is_untouched = True
                for q in primes:
                    if q > sqrt_n: break
                    if n % q == 0:
                        is_untouched = False
                        break
                if is_untouched:
                    primes.append(n)
                    break
                n += 1
        return primes
   
  
    # --- 2. İSTATİSTİKSEL ANALİZ (goster.py'den eklenenler) ---
    def analyze_stats(self, N=50000, Mk=30):
        """Doktrin İstatistikleri: I(n) dağılımı, Kolon Yoğunluğu ve Gap Analizi."""
        I_values = [self.get_intensity(n) for n in range(N+1)]
        primes = [n for n in range(2, N+1) if self.is_prime_helical(n)]
        
        # Kolon Analizi
        colon_data = {r: [0, 0] for r in range(Mk) if gcd(r, Mk) == 1}
        for n in range(2, N+1):
            r = n % Mk
            if r in colon_data:
                colon_data[r][0] += 1 # Toplam sayı
                if self.is_prime_helical(n):
                    colon_data[r][1] += 1 # Asal sayısı

        # Görselleştirme
        plt.figure(figsize=(15, 10))
        
        # I(n) Histogramı
        plt.subplot(2, 2, 1)
        plt.hist(I_values[2:], bins=range(0, max(I_values)+2), color='skyblue', edgecolor='black')
        plt.title(f"I(n) Dağılımı (N={N})")
        
        # Kolon Yoğunluğu (Asal Dağılımı)
        plt.subplot(2, 2, 2)
        labels = [str(r) for r in sorted(colon_data)]
        densities = [data[1]/data[0] for r, data in colon_data.items()]
        plt.bar(labels, densities, color='orange')
        plt.title(f"Mod {Mk} Kolon Asal Yoğunluğu")

        # P(asal|I) Olasılık Analizi
        plt.subplot(2, 2, 3)
        bins = {}
        for n in range(2, N+1):
            I = I_values[n]
            if I not in bins: bins[I] = [0, 0]
            bins[I][0] += 1
            if self.is_prime_helical(n): bins[I][1] += 1
        
        I_bins = sorted(bins.keys())
        probs = [bins[I][1]/bins[I][0] for I in I_bins]
        plt.plot(I_bins, probs, 'o-', label="Empirik P(asal|I)")
        plt.title("I(n) Yoğunluğuna Göre Asal Olasılığı")
        plt.xlabel("I(n)")
        plt.legend()

        plt.tight_layout()
        plt.show()

    # --- 3. GÖRSELLEŞTİRME MODÜLLERİ ---
    def visualize_matrix_2d_blocks(self, level_p=7, rows=50, block_size=6, gap=1):
        ml_full = self.levels.get(level_p, 210)
        display_cols = min(ml_full, 500)
        start_n = level_p * level_p
        
        candidates = []
        curr = start_n
        while len(candidates) < (rows * ml_full):
            if curr % 2 != 0 and curr % 3 != 0: candidates.append(curr)
            curr += 1

        fig, ax = plt.subplots(figsize=(16, 10))
        ax.set_facecolor('#050505')
        ax.set_xlim(-gap, display_cols * (block_size + gap))
        ax.set_ylim(-gap, rows * (block_size + gap))
        ax.set_aspect('equal')
        ax.invert_yaxis()

        prev_primes = [p for p in [2, 3, 5, 7, 11, 13, 17, 19] if p < level_p]

        for r in range(rows):
            for c in range(display_cols):
                idx = r * ml_full + c
                if idx >= len(candidates): break
                val = candidates[idx]
                
                # SENİN DÜZELTTİĞİN RENK MANTIĞI
                if val % level_p == 0: color = '#FFFFFF' # BEYAZ (LAZER)
                elif any(val % p == 0 for p in prev_primes): color = '#FF0000' # KIRMIZI (MİRAS)
                elif self.is_prime_helical(val): color = '#00FF00' # YEŞİL (ASAL)
                else: color = '#4B0082' # MOR (BİLEŞİK)
                
                rect = patches.Rectangle((c*(block_size+gap), r*(block_size+gap)), 
                                        block_size, block_size, facecolor=color, linewidth=0)
                ax.add_patch(rect)
        plt.title(f"Miras Matrisi - Hedef P: {level_p}")
        plt.show()

    def visualize_helix_3d_vase(self, limit=1500, target_p=5):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        k, g, h = 0.5, 0.08, 0.05
        prev_primes = [p for p in [2, 3, 5, 7, 11, 13, 17, 19] if p < target_p]

        for n in range(5, limit):
            if n % 2 == 0 or n % 3 == 0: continue
            theta, r, z = n * k, n * g, n * h
            point_size, alpha = 6, 0.7
            
            if n == target_p: 
                color, point_size, alpha = '#FFFFFF', 30, 1.0
            elif any(n % p == 0 for p in prev_primes): color = '#FF0000'
            elif self.is_prime_helical(n): color = '#00FF00'
            else: color = '#4B0082'
            
            ax.scatter(r*np.cos(theta), r*np.sin(theta), z, c=color, s=point_size, alpha=alpha)
        plt.show()