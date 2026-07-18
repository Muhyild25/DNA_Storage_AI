"""
=============================================================================
Hybrid DNA-AI Core: End-to-End Integration Test
=============================================================================
Bu script, C++ (dnacore) ve Python (PyTorch LSTM) katmanlarının
birbiriyle olan uçtan uca veri iletişimini test etmek için tasarlanmıştır.
=============================================================================
"""

import dnacore
from ai_brain import DnaAIEngine

def main():
    print("=" * 65)
    print("      🚀 HYBRID DNA-AI MOTORU UÇTAN UCA TEST BAŞLIYOR")
    print("=" * 65 + "\n")

    # 1. ORİJİNAL VERİ HAZIRLIĞI
    mesaj = "Teknofest DNA Depolama Projesi! Bu sistem cok hizli calisiyor."
    byte_dizisi = list(mesaj.encode('utf-8'))
    print(f"[Aşama 1] Orijinal Mesaj: {mesaj}")

    # 2. C++ KAS GÜCÜ (ENCODING)
    dna_dizilimi = dnacore.encode_to_dna(byte_dizisi)
    print(f"\n[Aşama 2] 🧬 C++ Motoru Sentezi Tamamlandı. (Uzunluk: {len(dna_dizilimi)} baz)")

    # 3. PYTORCH YAPAY ZEKA BEYNİ (ANALİZ & OPTİMİZASYON)
    print("\n[Aşama 3] 🧠 PyTorch LSTM Ağı Devreye Giriyor...")
    ai_engine = DnaAIEngine()
    optimize_dna = ai_engine.optimize_sequence(dna_dizilimi)

    # 4. C++ KAS GÜCÜ (DECODING & KURTARMA)
    kurtarilan_bytes = dnacore.decode_from_dna(optimize_dna)
    kurtarilan_mesaj = bytes(kurtarilan_bytes).decode('utf-8')
    print(f"\n[Aşama 4] ✅ C++ Motoru Kurtarılan Mesaj: {kurtarilan_mesaj}")

    # 5. SİSTEM DOĞRULAMASI
    if mesaj == kurtarilan_mesaj:
        print("\n>>> BAŞARILI: Sistem kusursuz çalışıyor! Bütün boru hattı aktif. <<<")
    else:
        print("\n>>> HATA: Veri bütünlüğü doğrulanamadı! <<<")

if __name__ == "__main__":
    main()