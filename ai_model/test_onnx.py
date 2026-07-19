"""
=============================================================================
DNA Storage AI - ONNX Zeka Testi
=============================================================================
Bu script, C++'a gömülecek olan ONNX modelinin hala aynı zekaya
sahip olup olmadığını test eder.
=============================================================================
"""

import onnxruntime as ort
import numpy as np

def test_onnx_brain():
    print("=" * 65)
    print("      🧠 ONNX ÇALIŞMA ZAMANI (RUNTIME) TESTİ")
    print("=" * 65 + "\n")

    # 1. Modeli Yükle
    onnx_path = "dna_ai_model.onnx"
    try:
        session = ort.InferenceSession(onnx_path)
        print(f"✅ ONNX Modeli ('{onnx_path}') başarıyla yüklendi!")
    except Exception as e:
        print(f"❌ Model yüklenemedi: {e}")
        return

    # 2. Orijinal Krizi Simüle Et (70 tane C harfi)
    korkunc_dizilim = "C" * 70
    BASE_TO_IDX = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    # Harfleri sayılara çevir (C -> 1) ve Numpy Matrisine dönüştür
    indices = [BASE_TO_IDX.get(base, 0) for base in korkunc_dizilim]
    # Boyut: [batch_size=1, sequence_length=70]
    input_data = np.array([indices], dtype=np.int64) 

    # 3. Modelin beklediği girdi adını al
    input_name = session.get_inputs()[0].name

    # 4. Tahmini Yap (Inference)
    print("🔍 ONNX Beyni dizilimi analiz ediyor...")
    outputs = session.run(None, {input_name: input_data})
    predictions = outputs[0] # Risk skorları

    # 5. Sonuçları Değerlendir
    # Eğer skorlar 0.5'in üzerindeyse model riski başarıyla tespit etmiştir.
    ortalama_risk = np.mean(predictions)
    
    print("\n--- ANALİZ SONUCU ---")
    print(f"Ortalama Risk Skoru: {ortalama_risk:.4f} (Eşik değer: 0.5)")
    
    if ortalama_risk > 0.5:
        print("🎉 BAŞARILI: ONNX modeli riski gördü! C++ entegrasyonu için tamamen hazırız.")
    else:
        print("⚠️ DİKKAT: ONNX modeli riski algılayamadı. Dönüşümde zeka kaybı yaşanmış olabilir.")

if __name__ == "__main__":
    test_onnx_brain()