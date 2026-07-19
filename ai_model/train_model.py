"""
=============================================================================
DNA Storage AI - LSTM Eğitim Döngüsü (Training Loop)
=============================================================================
Bu script, sentetik DNA veri setini kullanarak PyTorch LSTM modelini eğitir.
Model, dizilimler içerisindeki homopolimer risklerini (0-1 arası) tespit 
etmeyi öğrenir ve eğitilmiş ağırlıklarını kaydeder.
=============================================================================
"""

import torch
import torch.nn as nn
import torch.optim as optim
import json
from torch.utils.data import Dataset, DataLoader

# Yazdığımız beyni (modeli) ve harf-sayı sözlüğünü içe aktarıyoruz
from ai_brain import DnaLSTMOptimizer, BASE_TO_IDX

# 1. VERİ SETİ SINIFI (PyTorch Dataset)
class DnaDataset(Dataset):
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)
            
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, idx):
        item = self.data[idx]
        seq = item["sequence"]
        labels = item["labels"]
        
        # Harfleri modelin anlayacağı sayılara (Tensörlere) çevir
        indices = [BASE_TO_IDX.get(base, 0) for base in seq]
        
        x = torch.tensor(indices, dtype=torch.long)
        # Etiketlerin boyutunu model çıktısıyla eşleşecek şekilde [seq_len, 1] yap
        y = torch.tensor(labels, dtype=torch.float32).unsqueeze(1) 
        return x, y

def train():
    print("=" * 65)
    print("      🧠 DNA-AI LSTM MODELİ EĞİTİMİ BAŞLIYOR")
    print("=" * 65 + "\n")

    # 2. HİPERPARAMETRELER
    EPOCHS = 10              # Modelin tüm veri setini kaç kez okuyacağı
    BATCH_SIZE = 32          # Verilerin kaçarlı gruplar halinde modele gireceği
    LEARNING_RATE = 0.005    # Modelin öğrenme hızı (Adım büyüklüğü)

    # Verileri yükle ve DataLoader ile karıştırarak (shuffle) hazırla
    dataset = DnaDataset("dna_dataset.json")
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    # Modeli başlat
    model = DnaLSTMOptimizer()
    
    # Kayıp (Loss) Fonksiyonu: İkili sınıflandırma (0 veya 1) olduğu için BCELoss kullanıyoruz
    criterion = nn.BCELoss() 
    # Optimizasyon Algoritması: Ağırlıkları güncelleyecek olan Adam Optimizer
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print(f"[Sistem] Toplam Veri: {len(dataset)} | Batch Boyutu: {BATCH_SIZE} | Tur (Epoch): {EPOCHS}\n")

    # 3. EĞİTİM DÖNGÜSÜ
    model.train() # Modeli resmi olarak "Eğitim" moduna al
    
    for epoch in range(EPOCHS):
        epoch_loss = 0.0
        
        for batch_x, batch_y in dataloader:
            # a) Geçmiş adımdan kalan eski gradyanları (hesaplamaları) sıfırla
            optimizer.zero_grad()
            
            # b) İleri Yayılım (Forward Pass): Modelden tahminleri al
            predictions = model(batch_x)
            
            # c) Kayıp Hesaplama (Loss): Tahminler gerçek cevaplardan ne kadar uzak?
            loss = criterion(predictions, batch_y)
            
            # d) Geri Yayılım (Backpropagation): Hatayı geriye doğru ilet
            loss.backward()
            
            # e) Optimizasyon: Hataları azaltmak için nöron ağırlıklarını güncelle
            optimizer.step()
            
            epoch_loss += loss.item()
            
        # O turdaki ortalama hatayı ekrana yazdır
        ortalama_loss = epoch_loss / len(dataloader)
        print(f"Epoch [{epoch+1:02d}/{EPOCHS}] Tamamlandı - Ortalama Hata (Loss): {ortalama_loss:.4f}")

    print("\n✅ Eğitim Tamamlandı! Model artık biyolojik hataları tanıyor.")
    
    # 4. EĞİTİLMİŞ MODELİ KAYDET
    # Modelin öğrendiği tüm zekayı (ağırlıkları) bir dosyaya kaydediyoruz
    torch.save(model.state_dict(), "dna_lstm_model.pth")
    print("💾 Eğitilmiş model zekası 'dna_lstm_model.pth' olarak kaydedildi.")

if __name__ == "__main__":
    train()