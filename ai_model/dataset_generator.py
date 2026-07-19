"""
=============================================================================
DNA Storage AI - Gelişmiş Sentetik Veri Seti Üretici (V2)
=============================================================================
Bu script, LSTM modelini eğitmek için hem kısa hem de çok uzun (300 baza kadar)
dizilimler ve devasa boyutlarda (100 baza kadar) biyolojik hatalar barındıran 
dinamik bir veri seti oluşturur.
=============================================================================
"""

import random
import json

def generate_synthetic_dna(num_samples=5000, max_seq_length=300):
    bases = ['A', 'C', 'G', 'T']
    dataset = []

    print(f"[Dataset] 🧬 Gelişmiş Sentetik DNA Veri Seti Üretiliyor ({num_samples} örnek)...")

    for _ in range(num_samples):
        # Gerçek dünya simülasyonu: 50 ile 300 baz arasında rastgele uzunlukta DNA
        seq_length = random.randint(50, max_seq_length)
        seq = "".join(random.choices(bases, k=seq_length))
        
        has_error = random.choice([True, False])
        labels = [0] * seq_length # Başlangıçta tüm bazlar "0" (Güvenli)
        
        if has_error:
            error_base = random.choice(bases)
            # Kritik Güncelleme: Artık 4 harften 100 harfe kadar devasa hatalar üretebiliyoruz!
            max_possible_error = min(100, seq_length // 2)
            error_length = random.randint(4, max(4, max_possible_error)) 
            
            insert_pos = random.randint(0, seq_length - error_length - 1)
            
            # Dizilime devasa hatayı zorla yerleştir
            seq = seq[:insert_pos] + (error_base * error_length) + seq[insert_pos + error_length:]
            
            # Hatalı bölgeleri etiketle (1: Riskli)
            for i in range(insert_pos, insert_pos + error_length):
                labels[i] = 1

        dataset.append({
            "sequence": seq,
            "labels": labels,
            "has_error": has_error
        })

    with open("dna_dataset.json", "w") as f:
        json.dump(dataset, f)
        
    print(f"[Dataset] ✅ Başarıyla 'dna_dataset.json' oluşturuldu!")
    print(f"          -> Maksimum Dizilim Uzunluğu: {max_seq_length} baz")
    print(f"          -> Maksimum Hata (Homopolimer) Boyutu: 100 baz")

if __name__ == "__main__":
    generate_synthetic_dna()