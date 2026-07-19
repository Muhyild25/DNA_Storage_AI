"""
=============================================================================
DNA Storage AI - PyTorch'tan ONNX'e Dönüşüm Aracı
=============================================================================
Bu script, eğitilmiş PyTorch LSTM modelini, C++ motorunda bağımsız 
olarak çalışabilmesi için evrensel ONNX formatına dönüştürür.
=============================================================================
"""

import torch
import torch.onnx
from ai_brain import DnaLSTMOptimizer

def export_to_onnx():
    print("=" * 65)
    print("      🔄 ONNX DÖNÜŞÜM İŞLEMİ BAŞLIYOR")
    print("=" * 65 + "\n")

    # 1. Eğitilmiş Modeli Yükle
    model = DnaLSTMOptimizer()
    model_path = "dna_lstm_model.pth"
    
    try:
        model.load_state_dict(torch.load(model_path, weights_only=True))
        model.eval()
        print(f"[ONNX Export] ✅ '{model_path}' başarıyla yüklendi.")
    except Exception as e:
        print(f"[ONNX Export] ❌ Model yüklenirken hata oluştu: {e}")
        return

    # 2. Örnek (Dummy) Girdi Oluşturma
    # ONNX, modelin mimarisini anlamak için örnek bir verinin içeriden geçmesine ihtiyaç duyar.
    # [batch_size=1, seq_length=50] boyutunda rastgele bir tensör oluşturuyoruz.
    dummy_input = torch.randint(0, 4, (1, 50), dtype=torch.long)

    # 3. ONNX Formatında Dışa Aktarma
    onnx_file_name = "dna_ai_model.onnx"
    
    torch.onnx.export(
        model,                       # Dönüştürülecek model
        dummy_input,                 # Modelin girdi formatını anlaması için örnek veri
        onnx_file_name,              # Kaydedilecek dosya adı
        export_params=True,          # Eğitilmiş ağırlıkları da dahil et
        opset_version=18,            # Evrensel uyumluluk için opset versiyonu
        do_constant_folding=True,    # Optimizasyon: Sabitleri katla
        input_names=['input'],       # C++ tarafında çağıracağımız girdi adı
        output_names=['output'],     # C++ tarafında alacağımız çıktı adı
        dynamic_axes={               # Farklı uzunluktaki DNA dizilimlerini desteklemek için dinamik eksenler
            'input': {0: 'batch_size', 1: 'sequence_length'},
            'output': {0: 'batch_size', 1: 'sequence_length'}
        }
    )
    
    print(f"\n🎉 BAŞARILI! Model '{onnx_file_name}' olarak C++ entegrasyonuna hazır hale getirildi.")

if __name__ == "__main__":
    export_to_onnx()