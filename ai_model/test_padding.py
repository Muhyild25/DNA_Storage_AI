"""
=============================================================================
DNA Storage AI - Biyolojik Yama (Padding) Stres Testi
=============================================================================
"""

from ai_brain import DnaAIEngine

def test_padding():
    print("=" * 65)
    print("      🧪 YAPAY ZEKA BİYOLOJİK YAMA (STRES) TESTİ")
    print("=" * 65 + "\n")

    ai_engine = DnaAIEngine()

    # Bilerek laboratuvarda kesinlikle sentezlenemeyecek, 
    # kimyasal reaksiyonu bozacak korkunç bir dizilim oluşturuyoruz:
    # 15 tane A, 10 tane G ve 12 tane C yan yana!
    korkunc_dizilim = ("A" * 15) + ("G" * 10) + ("C" * 12)
    
    print("\n[Aşama 1] 🧬 Laboratuvar İçin İntihar Niteliğinde Dizilim Üretildi:")
    print(f"Orijinal DNA: {korkunc_dizilim}")

    print("\n[Aşama 2] 🧠 LSTM Ağı Dizilimi Analiz Ediyor ve Yamalıyor...")
    # Model bu tekrarları görüp aralara zıt harfler sıkıştıracak
    optimize_edilmis_dna = ai_engine.optimize_sequence(korkunc_dizilim)

    print("\n[Aşama 3] ✅ Optimize Edilmiş (Güvenli) Yeni Dizilim:")
    print(optimize_edilmis_dna)

    # Temizlik (Yamaları çıkarma) testi
    print("\n[Aşama 4] ♻️ Yamalar Çıkarılıp Orijinal Veri Kurtarılıyor...")
    temizlenmis_dna = ai_engine.restore_sequence(optimize_edilmis_dna)
    
    if temizlenmis_dna == korkunc_dizilim:
        print(">>> BAŞARILI: Yamalar atıldı ve kusursuzca geri temizlendi! <<<")

if __name__ == "__main__":
    test_padding()