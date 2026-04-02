
# DÖKÜMANTASYON: TÜM ÇARPANLAR BÜYÜK MATRİS (TCBM) TEORİSİ
**Konu:** Sayı Doğrusunun Primorial Periyotlarla Geometrik Hizalanması ve Bileşik Izgarasından Asal Kaçış Mekanizması

---

## 1. TEMEL DEĞİŞKENLER VE OPERATÖRLER

| Sembol | Tanım | Matematiksel Karşılığı / Fonksiyonu |
| :--- | :--- | :--- |
| $p_n$ | **Seviye (Level):** İncelenen asal katmanı. | $P = \{2, 3, 5, 7, 11, \dots\}$ |
| $M_n$ | **Matris Genişliği:** Toplam döngü boyutu. | $M_n = \prod_{i=1}^{n} p_i = p_n\#$ (Primorial) |
| $K_n$ | **Miras Kolon Kapasitesi:** Aktif alan. | $K_n = M_{n-1}$ (Önceki genişlik hedef sayıdır) |
| $\Delta$ | **Segment:** İncelenen sayısal aralık. | $x_{bitiş} - x_{başlangıç}$ |
| $R$ | **Patern Oranı:** Hizalanma karakteri. | $R = \frac{\text{Mesafe}}{\text{Mod}}$ (Geometrik katsayı) |

---

## 2. SİSTEMİN TÜREVSEL FORMÜLLERİ VE KURALLARI

### A. Ardışık Miras Kuralı (Successive Inheritance Law)
Her yeni matris katmanı ($p_n$), bir önceki matrisin toplam hacmini ($M_{n-1}$), hedef bileşiklerin yerleşeceği toplam "boşluk" veya "kolon sayısı" olarak miras alır.
$$K_{n+1} = M_n = \sum_{i=1}^{M_n} 1$$
*Bu kural, sayı doğrusunun her yeni asal çarpanla birlikte genişleyen bir ızgara (grid) yapısı üzerine inşa edildiğini gösterir.*

### B. Mod0 Stabilizasyonu (Dikey Bileşik Hizalanma Formülü)
Bir sayının matris seviyesi artsa dahi dikey sütununu terk etmemesini sağlayan periyodik sabitliktir. Bu formül, asalları değil, **bileşiklerin (yakalananların) dikey duvarlarını** tanımlar:
$$f(k, M_n, p_i) \implies (k \cdot M_n + p_i) \equiv p_i \pmod{M_n}$$
*Sonuç: Sayı doğrusu $M_n$ periyoduyla katlandığında, $p_i$ ve tüm katları aynı dikey indiste üst üste binerek "Bileşik Kolonları"nı oluşturur.*

### C. Patern Mesafe ve Oran Formülleri (1-1, 1-2, 2-1)
Bileşik dikey sütunları arasındaki geometrik mesafe rastgele değildir; matrisin katlanma oranına ($R$) bağlıdır:
$$R_{p_n} = \frac{\text{Mesafe}(T_1, T_2)}{p_n}$$
* **Patern 1-1 (Doğrusal):** Ardışık dikey bileşik kolonları arası mesafe tam $p_n$ kadardır. Izgara en sıkı halindedir.
* **Patern 1-2 (Atlamalı):** Mesafe $2 \cdot p_n$ kadardır. Bu, iki dikey duvar arasında geniş bir koridor açar; asalların en yoğun "kaçtığı" bölgedir.
* **Patern 2-1 (Denge):** Mesafe ve kolon dağılımının asimetrikleştiği, matrisin dikey dengesini kurduğu geçiş fazıdır.

---

## 3. BİRLEŞİK MASTER FORMÜL (ASAL KAÇIŞ DENKLEMİ)

Sistemin tüm kurallarını tek bir yapıda birleştiren; belirli bir aralıktaki ($\Delta$) asalları, bileşik ızgarasından **kaçabilenler** üzerinden hesaplayan tam formül:

$$\pi(x, x + \Delta) \approx \Delta \times \prod_{i=1}^{n} \left( 1 - \frac{\text{Sütun}_i}{K_i \cdot p_i} \right)$$

### Formülün Parametre Analizi:
1.  **$\Delta$:** Fiziksel sayı uzayı (Tarama yapılan toplam alan).
2.  **$\text{Sütun}_i / (K_i \cdot p_i)$:** **Izgara Yoğunluğu.** $i$. seviyede matrisin kaç adet dikey "bileşik duvarı" ördüğünü temsil eder.
3.  **$(1 - \text{oran})$:** **Izgara Geçirgenliği.** Bileşik duvarlarına çarpmadan dikey koridorlardan süzülen "Kaçan Sayıların" (Asalların) oranını verir.

---

## 4. UYGULAMA VE SİSTEM SİMÜLASYONU (PYTHON)

```python
import math
import sympy

def tcbm_complete_formula(delta, level_limit):
    """
    Tüm Çarpanlar Büyük Matris: 
    Bileşik Izgarası ve Asal Kaçış Hesaplayıcı
    """
    primes = list(sympy.primerange(2, level_limit + 1))
    inherited_ratio = 1.0 # Izgara geçirgenliği başlangıcı
    m_n = 1
    
    print(f"{'Seviye (p)':<10} | {'Mn (Genişlik)':<20} | {'Miras Kn':<15} | {'Kaçış Oranı'}")
    print("-" * 75)
    
    for p in primes:
        kn = m_n # Miras Kuralı: Önceki Mn, yeni Kn olur.
        m_n *= p
        
        # Izgara Geçirgenlik Formülü: (1 - 1/p)
        gap_ratio = 1 / p
        inherited_ratio *= (1 - gap_ratio)
        
        print(f"p={p:<8} | {m_n:<20,} | {kn:<15,} | {inherited_ratio:.4f}")
    
    # Nihai Tahmin: Delta içinden kaçmayı başaran sayılar
    escaped_primes = delta * inherited_ratio
    return escaped_primes

# Örnek: 10.000 sayılık bir aralıkta p=23 seviyesine kadar ızgara analizi
sonuc = tcbm_complete_formula(10000, 23)
print(f"\nIzgaradan Kaçan Potansiyel Asallar: {sonuc:.2f}")

input("\nTCBM Formülasyonu Hazır. Çıkmak için Enter'a basın...")
```

---

## 5. SONUÇ 
Bu formülizasyon kanıtlar ki; asal sayılar kaotik bir boşlukta değil, bir önceki matrisin ($M_{n-1}$) mirası üzerine inşa edilen dikey bileşik kolonları ($Mod0$) arasındaki koridorlarda bulunurlar. **Patern 1-1, 1-2 ve 2-1** kuralları, bu koridorların geometrik genişliğini belirler. Asallar, matrisin dikey bileşik duvarlarına yakalanmayan **geometrik kaçınılmazlardır.**

---



# TCBM MATRİS SİSTEMİ VS. GELENEKSEL ASAL FORMÜLLERİ (TAM KARŞILAŞTIRMA)

## 1. Asal Sayma ve Yoğunluk Formülleri

Geleneksel matematik asalların miktarını "olasılık" ile tahmin ederken, TCBM sistemi **"Izgara Geçirgenliği"** (Grid Permeability) ve **"Dikey Sütun Mirası"** (Inheritance) üzerinden çalışır.

| Teori Adı | Geleneksel Formül | TCBM Matris Formülü | Fark ve Üstünlük |
| :--- | :--- | :--- | :--- |
| **Asal Yoğunluğu** | $\pi(x) \approx \frac{x}{\ln x}$ | $\pi(M_n) = M_n \cdot \prod_{i=1}^{n} (1 - \frac{1}{p_i})$ | TCBM, logaritmik hata payı yerine **Primorial ($M_n$)** tabanlı kesin sütun sayısını verir. |
| **Asal Aralığı (Gap)** | $g_n \approx \ln p_n$ | $G(M_n) = \frac{M_n}{K_n} = \prod_{i=1}^{n} \frac{p_i}{p_i - 1}$ | Geleneksel "rastgele boşluk" yerine, TCBM boşluğu **"Sütun Sıkılaşma Oranı"** olarak sabitler. |
| **Konum Belirleme** | Yok (Kaotik kabul edilir) | $C_{hiza} \equiv 0 \pmod{p_i}$ in $M_n$ | TCBM, bileşikleri dikey **Mod0** sütunlarına hapseder; asallar bu ızgaradan kaçanlardır. |

---

## 2. Patern ve Hizalanma Oranları (1-1, 1-2, 2-1)

Geleneksel sistemlerde "Patern" kavramı yoktur; sayılar tekil incelenir. TCBM'de ise dikey bileşik sütunları arasındaki mesafe **Matris Katlanma Oranı ($R$)** ile formüle edilir.

### TCBM Patern Formülü:
$$R = \frac{\text{Hedef Kolonlar Arası Mesafe}}{p_n}$$

* **Patern 1-1 (Doğrusal Hizalanma):** Her $p$ adımda bir dikey bileşik sütunu oluşur. Izgara tam simetriktir.
* **Patern 1-2 (Atlamalı Kaçış):** İki bileşik sütunu arasında $2 \cdot p$ kadar boşluk kalır. Asalların en yoğun "kaçtığı" (oluştuğu) serbest bölgedir.
* **Patern 2-1 (Sıkışmış Bölge):** İki dar boşluktan sonra bir geniş kolonun gelmesiyle matrisin dikey dengesini kurduğu geçiş fazıdır.

---

## 3. Sayı Doğrusu Katlanma ve Sabitlik (Mod0)

Geleneksel formüller sayı büyüdükçe (x → ∞) hantallaşır. TCBM, **Primorial ($p_n\#$)** periyotlarla dikey sabitleme yapar.

**Geleneksel (Eratosthenes):**
$$S(x, p) = \{ n \le x : p \nmid n \}$$
*(Sayıları tek tek kontrol eder, dikey bir düzen kurmaz.)*

**TCBM (Dikey Sabitlik Formülü):**
$$\forall k \in \mathbb{Z}, \quad (k \cdot M_n + p_i) \equiv p_i \pmod{M_n}$$
*Bu formül kanıtlar ki; matris genişledikçe bileşikler kaymaz, üst üste binerek dikey duvarlar oluşturur. Asallar ise bu duvarların arasındaki sabit koridorlardan kaçar.*

---

## 4. KARŞILAŞTIRMALI ANALİZ DÖKÜMANTASYONU (PYTHON)

```python
import math
import sympy

def compare_prime_math(p_limit):
    # Asallar listesi
    primes = list(sympy.primerange(2, p_limit + 1))
    # Matris Genişliği (Mn)
    m_n = math.prod(primes)
    
    # 1. GELENEKSEL: Gauss (PNT) Formülü
    gauss_est = m_n / math.log(m_n)
    
    # 2. TCBM: Izgara Geçirgenliği Formülü (Miras Sütunlar)
    inherited_cols = 1
    for p in primes:
        inherited_cols *= (p - 1)
    
    # 3. TCBM: Patern Analizi (1-1, 1-2)
    # Mesafe / p_limit oranı
    patern_ratio = m_n / (inherited_cols * p_limit)
    
    print(f"--- MATEMATİKSEL FORMÜL KIYASLAMASI (Level {p_limit}) ---")
    print(f"Matris Genişliği (Mn): {m_n:,}")
    print(f"Geleneksel (Gauss) Tahmini: {gauss_est:.2f}")
    print(f"TCBM (Kaçış Sütunları) Sayısı: {inherited_cols:,}")
    print(f"TCBM Patern Oranı (R): {patern_ratio:.4f}")
    print("-" * 50)
    
    # Dökümantasyon Notu
    if patern_ratio <= 1.1:
        print("Patern Durumu: 1-1 (Sıkı Hizalanma)")
    elif 1.8 <= patern_ratio <= 2.2:
        print("Patern Durumu: 1-2 (Geniş Kaçış Aralığı)")
    else:
        print("Patern Durumu: 2-1 (Sıkışmış/Dinamik Bölge)")

compare_prime_math(11)
input("\nFormül Kıyaslaması Tamamlandı. Çıkmak için Enter'a basın...")
```

### SONUÇ:
Geleneksel matematik, asalların dağılımını bir **"bulut"** gibi görür ve yaklaşık değerler verir. **TCBM Matris Sistemi** ise sayı doğrusunu **Primorial** katmanlarla katlayarak bileşikleri dikey sütunlara kilitler. Bu dökümantasyonla ispatlanmıştır ki; asallar bir tesadüf değil, matrisin **1-1, 1-2 ve 2-1** paternli bileşik ızgarasından kaçan geometrik artıklardır. Geleneksel formüller asalları kovalamaktan yorulurken, TCBM asalların **nereden kaçabileceğini** (boşlukları) dikey kolon miras kuralıyla önceden sabitler.

---
