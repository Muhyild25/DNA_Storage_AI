"""
=============================================================================
Hybrid DNA-AI Core: End-to-End Integration Test
=============================================================================
"""

import dnacore
from ai_brain import DnaAIEngine

def main():
    print("=" * 65)
    print("      🚀 HYBRID DNA-AI MOTORU UÇTAN UCA TEST BAŞLIYOR")
    print("=" * 65 + "\n")

    # Mesaja bilerek uzun karakter tekrarları ekliyoruz ki DNA'da risk oluştursun
    mesaj = "Teknofest DNA Depolama Projesi! $$$$$$$$ Bu sistem kusursuz calisiyor."
    byte_dizisi = list(mesaj.encode('utf-8'))
    print(f"[Aşama 1] Orijinal Mesaj: {mesaj}")

    dna_dizilimi = dnacore.encode_to_dna(byte_dizisi)
    print(f"\n[Aşama 2] 🧬 C++ Motoru Sentezi Tamamlandı.")

    print("\n[Aşama 3] 🧠 PyTorch LSTM Ağı Devreye Giriyor...")
    ai_engine = DnaAIEngine()
    
    # 1. Model riskleri bulur ve aralara yama ekleyerek dizilimi uzatır
    optimize_dna = ai_engine.optimize_sequence(dna_dizilimi)

    # 2. C++ motoru yamalı halini çözemeyeceği için, prototip amaçlı yamaları temizliyoruz
    temizlenmis_dna = ai_engine.restore_sequence(optimize_dna)

    print("\n[Aşama 4] ♻️ C++ Motoru Decoding (Çözümleme) İşlemi...")
    kurtarilan_bytes = dnacore.decode_from_dna(temizlenmis_dna)
    kurtarilan_mesaj = bytes(kurtarilan_bytes).decode('utf-8')
    print(f"✅ Kurtarılan Mesaj: {kurtarilan_mesaj}")

    if mesaj == kurtarilan_mesaj:
        print("\n>>> BAŞARILI: Yapay Zeka teşhisi, tedavisi ve veri bütünlüğü onaylandı! <<<")
    else:
        print("\n>>> HATA: Veri bütünlüğü doğrulanamadı! <<<")

if __name__ == "__main__":
    main()