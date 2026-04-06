# 🌌 Doğal Sayıların Matrisi (Level 1 - 67)


## Tüm Çarpanlar Büyük Matris ve Ardışık Miras Kuralı

---
|--- Level ---|--- Çarpanlar ---|= Matris | Kolon Sayısı |
| --- | --- | --- | --- |
|Level  1 |(1) | 1 | 1 (Doğal Sayılar)|
|Level  2 |(1x2) |= 2 | 1 (Tek, Çift Sayılar)|
|Level  3 |(1x2x3) |= 6 | 2 (6n±1)|
|Level  5 |(1x2x3x5) |= 30 | 6 |
|Level  7 |(1x2x3x5x7) |= 210 | 30  |
|Level 11 |(1x2x3..x7x11) |= 2.310 | 210 |
|Level 13 |(1x2x3..x11x13) |= 30.030 | 2.310 |
|Level 17 |(1x2x3..x13x17) |= 510.510 | 30.030 |
|Level 19 |(1x2x3..x17x19) |= 9.699.690 | 510.510|
|Level 23 |(1x2x3..x19x23) |= 223.092.870 | 9.699.690 |
|Level 29 |(1x2x3..x23x29) |= 6.469.693.230 | 223.092.870 |
|Level 31 |(1x2x3..x29x31) |= 200.560.490.130 | 6.469.693.230 |
|Level 37 |(1x2x3..x31x37) |= 7.420.738.134.810 | 200.560.490.130 |
|Level 41 |(1x2x3..x37x41) |= 304.250.263.527.210 | 7.420.738.134.810 |
|Level 43 |(1x2x3..x41x43) |= 13.082.761.331.670.030n | 304.250.263.527.210n |
|Level 47 |(1x2x3..x43x47) |= 614.889.782.588.491.410n | 13.082.761.331.670.030n |
|Level 53 |(1x2x3..x47x53) |= 32.589.158.477.190.044.730n | 614.889.782.588.491.410n |
|Level 59 |(1x2x3..x53x59) |= 1.922.760.350.154.212.639.070n | 32.589.158.477.190.044.730n |
|Level 61 |(1x2x3..x59x61) |= 117.288.381.359.406.970.983.270n | 1.922.760.350.154.212.639.070n |
|Level 67 |(1x2x3..x61x67) |= 7.858.321.551.080.267.055.879.090n | 117.288.381.359.406.970.983.270n |
---

* Bir önceki matrisi, hedefin bulunduğu Kolon sayısı olarak miras alıyor. Ayrıca toplam matris iki satır arasındaki sayıların farkıdır.
* Örnek: 7 katlarının toplam matrisi, 11 matrisi kurulduğunda 11'in katlarının bulunacağı tüm kolonların sayısıdır.
* Matris eleme yapılmadan tüm çarpanları ile kurulursa hizalama aynı şekilde gerçekleşir ve öncekiler de karışık olarak birleşik dikey hizalarını oluştururlar. 
* Eleme (önceki bileşiklerin) yapılmadığında dahi bu dikey düzenin korunması, kuralın kendisinden önceki bileşiklerin elenmesinden bağımsız, sayı doğrusunun kendi "katlanma noktaları" ile ilgili olduğunu kanıtlar.
* Ayrıca hizalanma şekilleri : 1-1 , 1-2, 2-1 şeklindedir. örnek ilk kolon her zaman hedefin bileişiğidir ilk sıra modla taranır. ilk bulunan hedef bileşiği, ile ikinci bulanması gereken arasındaki kaç sayı olduğuna bakılır. 1-1 ise arada 10 sayı varsa 3. kolon +10 ileridedir, bulmazsa +10 daha gider bukez oran 1-2 olmuş olur. Patern bu şekilde devam eder. Örnek resimdeki level 29 1-2 oranlıdır, nadirde olsa 1-2.1 civarı çıkma ihtimali vardır, genelde +1 -1 yapılarak bulunabilir. Bu patern yapısı en küçük matris yapısını belirler.
* Örnek : 5,7,11,13 leri eleyip tekrar 17ler için matris kurulduğunda aynı şekilde bir Kolon olarak hizalanırlar. Sadece iki Kolon arasında boşluk elemeden dolayı sürekli azalır ve Alsallar diğer sütunlarda artmaya ve hizalanmaya başlarlar.
* Sonuç: Bir n sayısının $\sqrt{n}$ Tüm Çarpanlar Matrisi kurulabilirse o ve ondan öncekiler tamamen hizlanır. Bu aynı zzmanda asalların matrisi olur.

![Miras Matrisi](./ilk500-L29.png)

## Tek Çarpan Temel Matris

1. Mikro Yapı: > Oluşturulabilecek en küçük matris p7 ve üzerindeki sayılar için $Px3-1$ formundadır. Burada her bir $P$ birimi, 3 kolonluk bir alt uzay $(3*p)$ yaratır, ama 3 kolonluk matrisde son p modu katlanıp bir sonraki satırın ilki olur. Katları yani $6xp-1$  olursa sadce son p modu katlanır her zaman. Yani 6xp matrisinde $5p$ kolon oluşur..
Bu, "Genişlik - Hedef Kolon" dengesini kuran en temel hizalamadır.

2. "Katlanabilir Mod0" Kuralı:
Eğer $C$ (genişlik) sayısı $p$ sayısına tam bölünüyorsa 
($C = k \cdot p$);
O zaman $C$'nin her tam katı ($2C, 3C, 4C...$) de $p$ sayısına tam bölünmek zorundadır.

Sonuç: Hedef p'nin sütunları arasındaki boşluk genişler ama o sütunların dikey hattı asla bozulmaz. Hepsi Mod0 stabilizasyonuna sahiptir. 3p katları devamlılığı mod 0 dır.

---

## Ritmik Operatör
$6n \pm 1$ sisteminde bir $p$ asalı, $p^2$ noktasından itibaren $\{2p, 4p, 2p, 4p \dots\}$ adımlarıyla ilerler. 
Bu iki adımlık döngünün toplam periyodu **$6p$**'dir. Yani her $6p$ mesafede bir, ritim başa döner.

İşte bu ritmi tek bir matematiksel sorguya indiren **"Ritmik Vuruş Testi"** formülü:

### **1. Ritmik Operatör Formülü**
Bir $n$ sayısının, bir $p$ asalı tarafından vurulup vurulmadığını (yani $n$'nin $p$'nin bir katı olup olmadığını) şu kontrolle anlarız:

Önce mesafeyi hesapla: $d = n - p^2$

Eğer $d < 0$ ise zaten vurulmamıştır. $d \ge 0$ ise şu şartı kontrol et:
$$\text{Vuruş}(n, p) \iff (d \pmod{6p} == 0) \quad \text{veya} \quad (d \pmod{6p} == \text{Ritim}(p))$$

---

### **2. Ritim Sabitinin Belirlenmesi**
Buradaki "Ritim" değeri, $p$'nin hangi sütunda olduğuna ($6k-1$ mi yoksa $6k+1$ mi) göre değişir:

* **Eğer $p = 6k-1$ ise (5, 11, 17... gibi):**
    İlk adım $2p$'dir.
    $$\text{Ritim}(p) = 2p$$
    *(Yani $d \pmod{6p}$ sonucu $0$ veya $2p$ ise $n$ bileşiktir.)*

* **Eğer $p = 6k+1$ ise (7, 13, 19... gibi):**
    İlk adım $4p$'dir.
    $$\text{Ritim}(p) = 4p$$
    *(Yani $d \pmod{6p}$ sonucu $0$ veya $4p$ ise $n$ bileşiktir.)*

---

### **3. Uygulama Örneği (Neden Çalışıyor?)**

Diyelim ki $n = 35$ sayısını test ediyoruz ve $p = 5$ için bakıyoruz:
1.  $d = 35 - 5^2 = 10$
2.  Periyot: $6p = 6 \times 5 = 30$
3.  $p=5$ bir $6k-1$ sayısıdır, dolayısıyla **Ritim = 2p = 10**.
4.  Kontrol: $10 \pmod{30}$ sonucu **10**'dur.
5.  **Sonuç:** Ritimle eşleşti! $35$, $5$ tarafından vurulmuştur (Bileşiktir).

Diyelim ki $n = 49$ ve $p = 7$:
1.  $d = 49 - 7^2 = 0$
2.  $0 \pmod{42} = 0$. 
3.  **Sonuç:** Tam vuruş! (Bileşiktir).

---

### **4. Algoritmik Özet (Asal mıdır?)**

Bir $n$ sayısının asal olduğunu anlamak için:
1. $n$ sayısı $6k \pm 1$ formunda mı? (Değilse elendi).
2. $p = 5$’ten başlayarak $\sqrt{n}$’e kadar olan her $p \in \{6k \pm 1\}$ için:
   * $d = n - p^2$
   * `Eğer (d % (6*p) == 0) veya (d % (6*p) == Ritim):` **BİLEŞİKTİR.**
3. Hiçbir $p$ için bu şart sağlanmazsa: **ASALDIR.**




---

### **1. Değişken Tanımları**
* **$n$:** Test etmek istediğin aday sayı (Örn: $35, 49, 127 \dots$).
* **$p$:** $5$’ten başlayarak $\sqrt{n}$’e kadar giden $6k \pm 1$ formundaki asallar.
* **$d$:** $n$ ile $p^2$ arasındaki mesafe ($n - p^2$).
* **$R(p)$:** $p$ asalı için belirlenen **Ritim Sabiti**.

---

### **2. Ritim Sabiti Fonksiyonu ($R(p)$)**
$p$ sayısının $6n \pm 1$ serisindeki konumuna göre vuruş karakteri belirlenir:

$$R(p) = \begin{cases} 2p, & \text{eğer } p \equiv 5 \pmod 6 \\ 4p, & \text{eğer } p \equiv 1 \pmod 6 \end{cases}$$

---

### **3. Genel Bileşiklik Operatörü (Vuruş Testi)**
Bir $n$ sayısı, bir $p$ asalı tarafından ancak ve ancak şu şartlardan biri sağlanıyorsa **vuruş alır (bileşiktir)**:

$$\boxed{(n - p^2) \pmod{6p} \in \{0, R(p)\}}$$

*Bu formülün meali şudur:*
1.  **$(n - p^2) \pmod{6p} = 0$** ise; $n$ sayısı, $p$ asalının tam karesidir veya tam bir periyot ($6p, 12p \dots$) sonrasına denk gelmiştir.
2.  **$(n - p^2) \pmod{6p} = R(p)$** ise; $n$ sayısı, ritmin ilk sıçrama noktasına ($2p$ veya $4p$) denk gelmiştir.

---

### **4. Tam Algoritmik Karar Şeması**

Bir $n$ sayısının asallığını bu formülle kontrol etmek için şu adımları izle:

1.  **Ön Eleme:** $n \pmod 2 \neq 0$ ve $n \pmod 3 \neq 0$ olmalı.
2.  **Formül Uygulama:** $5 \le p \le \sqrt{n}$ aralığındaki tüm $p \in \{6k \pm 1\}$ sayıları için:
    * $R = (p \pmod 6 == 5) ? (2p) : (4p)$
    * $Kalan = (n - p^2) \pmod{6p}$
    * **Eğer** $Kalan == 0$ veya $Kalan == R$ ise: **BİLEŞİKTİR.**
3.  **Final:** Eğer hiçbir $p$ değeri için yukarıdaki vuruş gerçekleşmezse: **$n$ ASALDIR.**

---

### **5. Örnek Sağlama (Neden Kusursuz Çalışıyor?)**

**Örnek: $n = 91$ sayısı asal mı?** ($\sqrt{91} \approx 9.5$, yani sadece $p=5$ ve $p=7$ kontrol edilecek.)

* **$p = 5$ için ($6k-1$):**
    * $R(5) = 2 \times 5 = 10$
    * $Kalan = (91 - 5^2) \pmod{30} \implies 66 \pmod{30} = 6$
    * $6 \notin \{0, 10\}$ (5 vuramadı).
* **$p = 7$ için ($6k+1$):**
    * $R(7) = 4 \times 7 = 28$
    * $Kalan = (91 - 7^2) \pmod{42} \implies 42 \pmod{42} = 0$
    * $0 \in \{0, 28\}$ (**VURULDU!**)
* **Sonuç:** $91$ bileşik bir sayıdır ($7 \times 13$).

---
```
def is_hit(n, p):
    # p'nin konumuna göre Ritim Sabiti (R)
    r = 2*p if p % 6 == 5 else 4*p
    
    # Mesafe ve Periyot Kontrolü
    d = n - p**2
    if d < 0: return False
    
    # 6p periyodundaki vuruş noktaları: 0 veya R
    return (d % (6*p)) in [0, r]
```
### **Neden Bu Formül "Büyük Matris" İhtiyacını Bitirir?**
Çünkü $(n - p^2) \pmod{6p}$ işlemi, sayının büyüklüğünden bağımsız olarak onu $6p$ uzunluğundaki tek bir **"ritim hücresine"** hapseder. Sen matrisin trilyonuncu satırına da baksan, o satırın o hücre içindeki pozisyonu her zaman bu modüler sonuçla aynıdır. 



---
# 🌌 Doğal Sayıların Mimari DNA'sı: Helezonik Miras Doktrini

Bu doküman, statik **Doğal Sayılar Matrisi** ile dinamik **Ters Konik Helezon** modelinin birleşimidir. Temel ilke: "Küçük olan her zaman büyüğün üzerinde dikey bir mühür sahibidir."

---

## 🏗️ 1. Matrisel Yapı ve Ardışık Miras (Statik Katman)

Sayı doğrusu, Primorial $p_n $\#  seviyelerine göre katmanlara ayrılır. Her yeni Level, bir önceki Level'ın tüm dikey kolonlarını ve boşluklarını "miras" alır.

| Level | Çarpanlar ($p_n$) | Matris Genişliği ($M_L$) | Mimari Durum |
| :--- | :--- | :--- | :--- |
| **Level 2** | (2) | 2 | Tek/Çift Simetrisi |
| **Level 3** | (2x3) | 6 | 6n±1 Temel Filtresi |
| **Level 5** | (2x3x5) | 30 | 6 kolonluk ilk derin yapı |
| **Level 7** | (...x7) | 210 | 30 dikey hatlı mühür sistemi |
| **Level 11**| (...x11) | 2.310 | Karmaşık dikey hizalanma |

**Dikey Hat Kuralı:** Eğer bir genişlik $C$, bir asal $p$'ye tam bölünüyorsa ($C = k \cdot p$), o sütunun dikey hattı sonsuza kadar **Mod 0** stabilizasyonuna sahip olur.

---

## 🌀 2. Konik Helezon (Dinamik Katman)

Sayı doğrusu 360 derecelik bir döngüye sokulduğunda, matrisin "kolonları" merkezden dışa doğru açılan **Dikey Lazer Hatlarına** dönüşür.

### 📐 A. Konum ve Genişleme Formülü
Sayı doğrusu büyüdükçe helezonun çapı $\sqrt{n}$ oranında genişler:
1.  **Açı ($\theta$):** $\theta(n) = n \times k$
2.  **Yarıçap ($R$):** $R(n) = \sqrt{n} \times g$
3.  **Yükseklik ($Z$):** $Z(n) = n \times h$

### 📐 B. Açısal Hizalama (Mühürleme)
Herhangi bir $X$ sayısının helezon üzerindeki açısı, matristeki dikey kolon yerini belirler:
$$\theta(X) = \left( \frac{X \pmod{M_L}}{M_L} \right) \times 360^\circ$$

---

## 🏹 3. Miras Lazerleri ve Asal Sızma

Helezon üzerindeki her küçük asal ($p$), kendi katlarını vuran bir **Dikey Hat** oluşturur.

1.  **Lazer Kaynakları:** $5, 7, 11, 13...$ gibi küçük asallar, helezonun merkezinde konumlanmış yeşil "Mermi Fabrikaları"dır.
2.  **Miras Hattı:** Bir asal $p$, helezonun her turunda aynı açısal koordinata ($\theta$) denk gelen katlarını ($2p, 3p...$) mühürler.
3.  **Dikey Lazerler:** Bu hatlar helezon boyunca bükülse de, üstten bakıldığında dikey ve sarsılmaz bir **"Sayısal Kafes"** oluştururlar.

![Helezonik Miras](./helezonikmiras.png)


### 📋 Sonuç
Sayı ne kadar büyürse büyüsün, küçük asalların dikey hatları o devasa sayıların üzerinden geçer. Bir sayının **ASAL** kalabilmesi için, merkezden yükselen hiçbir **"Beyaz Miras Lazeri"**ne çarpmaması gerekir. 
### 1. Ters Koni Helezonu – Parametrik Denklemler (Cartesian Koordinatlar)

Her doğal sayı **n** için (veya sadece asallar için) koordinatlar şöyle tanımlanır:

$$[
\begin{align}
\theta(n) &= n \cdot k && \text{(açısal adım, radyan cinsinden)} \\
R(n) &= n \cdot g && \text{(yarıçap – koni genişlemesi)} \\
Z(n) &= Z_0 - n \cdot h && \text{(yükseklik – ters yön için negatif)} \\
x(n) &= R(n) \cdot \cos(\theta(n)) \\
y(n) &= R(n) \cdot \sin(\theta(n)) \\
z(n) &= Z(n)\\
\end{align}
]$$

- **\(k\)**: Açısal yoğunluk katsayısı (örnek: $$\(k = 0.1\)$$ veya $$\(k = \frac{2\pi}{ML}\)$$ ile matrise bağlı).  
- **\(g\)**: Genişleme katsayısı (koninin açısını belirler, örneğin \(g = 0.05\)).  
- **\(h\)**: Yükselme (veya alçalma) katsayısı (örneğin $$\(h = 0.03\)$$ ).  
- **\(Z_0\)**: Başlangıç yüksekliği (koninin tepe noktasını ayarlar, örneğin $$\(Z_0 = 10\)$$ ).  

**Ters koni etkisi** tam olarak ** $$\(Z(n) = Z_0 - n \cdot h\)$$ ** satırından gelir.  
n büyüdükçe Z **azalırken** R büyür → koni **yukarıdan aşağıya** daralır (senin görselindeki gibi).

### 2. Matris + Dikey Lazer Hatları Entegrasyonu (En Önemli Kısım)

Sadece düzgün spiral değil, **matristeki dikey kolonlar** (senin beyaz lazer hatların) helezon üzerinde **sabit açısal radyal ışınlar** olur. Bunun için θ’yı **n** yerine **kolon numarası** ile bağla:

Her sayı \(X\) için:

$$[
\theta(X) = 2\pi \times \frac{c}{ML_k}
\]$$

burada  
- $$(c = X \mod ML_k\)$$ (matristeki sütun / kolon)  
- $$(ML_k =\)$$ mevcut primorial matris genişliği  

Sonra koordinatlar:

$$\[
\begin{align}
R(X) &= X \cdot g \\
Z(X) &= Z_0 - X \cdot h \\
x(X) &= R(X) \cdot \cos\bigl(\theta(X)\bigr) \\
y(X) &= R(X) \cdot \sin\bigl(\theta(X)\bigr) \\
z(X) &= Z(X)
\end{align}
\]$$

Bu sayede:
- Aynı sütundaki tüm sayılar (**Mod 0** kuralına uyanlar) **aynı θ** değerinde kalır → **dikey lazer hattı** 3D’de radyal ışın olur.
- Senin minimum matris (6p) ve 1-2 paternin bu θ değerlerini otomatik belirler.

### 3. Sadece Asallar İçin “Asal İmza Helisi”

Görselindeki gibi sadece asalları çizmek için:
- n yerine **asal p**’leri al,
- Renk: p’nin büyüklüğüne göre (örneğin log(p) veya doğrudan p ile renk skalası – senin görselindeki gibi sarıdan mora).

Parametrik denklemler aynı kalır, sadece n → p olarak değiştirilir.

### 4. Pratik Örnek Parametreler (Senin Görseline Yakın)

| Parametre | Önerilen Değer          | Açıklama                              |
|-----------|-------------------------|---------------------------------------|
| \(k\)     | \(0.08\) veya \(2\pi / ML\) | Spiral yoğunluğu                      |
| \(g\)     | \(0.04\)                | Koni açısı (genişleme)                |
| \(h\)     | \(0.025\)               | Yükseklik adımı                       |
| \(Z_0\)   | \(12\)                  | Koninin üst başlangıç yüksekliği      |
| \(ML_k\)  | 210 veya 2310           | Mevcut primorial seviyesi             |

---

# 🟢 KONİK HELİKS TABANLI ASAL MATRİS & p→p+1

## 1️⃣ Temel Kavramlar

* Sayılar, bir **konik heliks** üzerinde geometrik olarak sıralanır.
* Her küçük asal (p), heliks üzerinde bir **dolu kolon** olarak temsil edilir.
* Bu kolonlar, (p)’nin katı olan sayıları işaretler (**bileşik kolonlar**).
* Boş kolonlar, potansiyel asalları gösterir.
* Bu sistem, klasik “mod tablosu” veya “primorial matris” sisteminin geometrik karşılığıdır.

---

## 2️⃣ Kolon Matrisi ve Primorial

* Primorial $$(P_n \# = 2 \cdot 3 \cdot 5 \cdots p_n)$$
* Tüm küçük asal kolonlar kurulur $$((p \le \sqrt{N}))$$
* İlk satır: $$([1, 2, …, P_n \#])$$
* İlk satır taramasıyla **tüm bileşik kolonlar** tespit edilebilir:

$$[
\text{Occupied}(k) = \bigvee_{q \le p_n} (k \bmod q = 0)
]$$

* Boş kolonlar = potansiyel asallar

> Not: Bu, deterministik olarak p→p+1 bulmayı sağlar.

---

## 3️⃣ p→p+1 Mantığı (Deterministik)

1. Bilinen asal (p) seçilir.
2. Potansiyel asallar aralığı oluşturulur: $$([p+1, …, p+G])$$
3. Küçük asal kolonlar kurulur $$((q \le \sqrt{p+G}))$$
4. İlk boş kolon → sonraki asal $$(p_{n+1})$$
5. Paternler: 1-1, 1-2, 2-1 şeklinde tekrar eder

$$[
p_{n+1} = \min { n \in [p+1, …, p+G] \mid n \bmod q \neq 0, \forall q \le \sqrt{p+G} }
]$$

---

## 4️⃣ Heliks Üzerinde Asallık Testi

* Sayı (N) heliks üzerinde koordinata yerleştirilir.
* Küçük asal kolonlar sırayla kontrol edilir:

  1. Eğer **bir kolon çarpıyorsa**, sayı **bileşik**, test biter.
  2. Eğer **hiçbir kolon çarpmazsa**, sayı **asal**.
* Bu yöntem klasik kolon sisteminden daha hızlıdır:

  * Çünkü ilk çarpanda durulur → gereksiz kontroller yapılmaz.

### Pseudocode

```text
Input: sayı N
Heliks kolonları = küçük asal çarpan kolonları

for kolon in heliks:
    if N mod kolon == 0:
        return "Bileşik"  # test biter
return "Asal"            # hiç çarpan bulunmadı
```

---

## 5️⃣ Gap ve Patern

* Kolon boşlukları ile iki ardışık asal arasındaki gap belirlenir.
* Paternler: 1-1, 1-2, 2-1 → bu oranlar heliks üzerinde sabittir.
* Örnek:

```
103, 107, 109, 113, 127, 131, 137, 139, 149, 151
Küçük asal kolonlar: 2,3,5,7,11
```

* Her sayı kolonlarda test edilip ilk boş kolon belirlenir → deterministik olarak sonraki asal bulunur.

---

## 6️⃣ Avantajlar

* Deterministik ve geometrik → tüm bileşikler eleme ile tespit edilir.
* İlk çarpanda durma → büyük sayılar için hız kazanımı.
* Patern tabanlı → ardışık asalların gap’ları tahmin edilebilir.
* Küçük asal kolon sayısı = $$(\sqrt{N})$$ → bellek ve işlem sınırlı.

---

## 7️⃣ Özet Formül

1. **Kolon kurulumu:** tüm $$(q \le \sqrt{N})$$ küçük asal kolonlar
2. **Eleme:** ilk satır veya heliks üzerinden her sayı test edilir
3. **İlk boş kolon:** sonraki asal
4. **Gap ve patern:** kolon boşlukları üzerinden tahmin edilir

$$[
\boxed{
p_{n+1} = \min { n > p_n \mid n \bmod q \neq 0, \forall q \le \sqrt{p_{n+1}} }
}
]$$

> Bu formül hem teorik hem algoritmik olarak kolon tabanlı heliks sistemi ile p→p+1 bulmayı garanti eder.

---

**Bu çalışma, asalların dağılımındaki düzensizliği reddedip, onları çok boyutlu bir matrisin dikey sütunlarına hapseden radikal ve tutarlı bir yaklaşımdır.**

**"Karmaşa aslında mükemmel bir dokumadır; biz sadece o dokudaki boşlukları (asalları) takip ediyoruz."**
