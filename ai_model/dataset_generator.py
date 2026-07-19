"""
=============================================================================
DNA Storage AI - Sentetik Veri Seti Üretici
=============================================================================
Bu script, LSTM modelini eğitmek için içinde rastgele biyolojik hatalar
(homopolimerler) barındıran sentetik DNA dizilimleri oluşturur.
=============================================================================
"""

import random
import json

def generate_synthetic_dna(num_samples=2000, seq_length=50):
    bases = ['A', 'C', 'G', 'T']
    dataset = []

    print("[Dataset] 🧬 Sentetik DNA Veri Seti Üretiliyor...")

    for _ in range(num_samples):
        # Rastgele temiz bir dizilim oluştur
        seq = "".join(random.choices(bases, k=seq_length))
        
        # %50 ihtimalle dizilimin içine riskli bir homopolimer (hata) enjekte et
        has_error = random.choice([True, False])
        labels = [0] * seq_length # Başlangıçta tüm bazlar "0" (Güvenli)
        
        if has_error:
            error_base = random.choice(bases)
            error_length = random.randint(4, 7) # 4, 5, 6 veya 7'li tekrar
            insert_pos = random.randint(0, seq_length - error_length - 1)
            
            # Dizilime hatayı zorla yerleştir
            seq = seq[:insert_pos] + (error_base * error_length) + seq[insert_pos + error_length:]
            
            # Hatalı bölgeleri etiketle (1: Riskli) -> Yapay zekadan bulmasını isteyeceğimiz yerler
            for i in range(insert_pos, insert_pos + error_length):
                labels[i] = 1

        dataset.append({
            "sequence": seq,
            "labels": labels,
            "has_error": has_error
        })

    # Veri setini modelin okuyabileceği JSON formatında kaydet
    with open("dna_dataset.json", "w") as f:
        json.dump(dataset, f)
        
    print(f"[Dataset] ✅ {num_samples} adet dizilim başarıyla 'dna_dataset.json' dosyasına kaydedildi!")

if __name__ == "__main__":
    generate_synthetic_dna()