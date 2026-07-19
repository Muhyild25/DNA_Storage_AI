import dnacore
import time

def test_cpp_ai_engine():
    print("=" * 65)
    print("     🚀 C++ YAPAY ZEKA MOTORU (DNA_CORE) TESTİ BAŞLIYOR")
    print("=" * 65 + "\n")

    # 1. Modeli C++ Çekirdeğinde Başlat
    model_yolu = "dna_ai_model.onnx"
    print(f"[*] ONNX modeli C++ belleğine yükleniyor: '{model_yolu}'")
    
    try:
        baslangic_zamani = time.time()
        # İşte sihir burada gerçekleşiyor: C++ sınıfımızı çağırıyoruz!
        ai_motoru = dnacore.DnaAiEngine(model_yolu)
        yukleme_suresi = time.time() - baslangic_zamani
        print(f"✅ Model C++ çekirdeğine başarıyla yüklendi! (Süre: {yukleme_suresi:.4f} saniye)\n")
    except Exception as e:
        print(f"❌ Model yüklenirken bir hata oluştu: {e}")
        return

    # 2. Orijinal Krizi Simüle Et (70 tane C harfi)
    korkunc_dizilim = "C" * 70
    print(f"[*] Analiz edilecek sorunlu biyolojik dizi oluşturuldu (70x 'C').")

    # 3. C++ Hızında Yapay Zeka Çıkarımı (Inference)
    print("[*] C++ motoru risk analizi yapıyor...")
    
    try:
        baslangic_zamani = time.time()
        # C++ fonksiyonumuzu tetikliyoruz
        risk_skoru = ai_motoru.analyze_risk(korkunc_dizilim)
        hesaplama_suresi = time.time() - baslangic_zamani
        
        print("\n--- 📊 C++ ANALİZ SONUCU ---")
        print(f"Ortalama Risk Skoru: {risk_skoru:.4f} (Eşik değer: 0.5)")
        print(f"İşlem Süresi (Saniye): {hesaplama_suresi:.6f}")
        
        if risk_skoru > 0.5:
            print("\n🎉 KUSURSUZ! C++ içindeki ONNX motoru biyolojik riski anında ve tam isabetle tespit etti.")
        else:
            print("\n⚠️ DİKKAT: Model riski algılayamadı. Sonuçlar beklenenden düşük.")
            
    except Exception as e:
         print(f"❌ Analiz sırasında bir hata oluştu: {e}")

if __name__ == "__main__":
    test_cpp_ai_engine()