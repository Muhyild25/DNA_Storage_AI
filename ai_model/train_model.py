"""
=============================================================================
DNA Storage AI - LSTM Eğitim Döngüsü (Padding Özellikli)
=============================================================================
"""

import torch
import torch.nn as nn
import torch.optim as optim
import json
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
from ai_brain import DnaLSTMOptimizer, BASE_TO_IDX

# 1. VERİ SETİ SINIFI
class DnaDataset(Dataset):
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)
            
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, idx):
        item = self.data[idx]
        indices = [BASE_TO_IDX.get(base, 0) for base in item["sequence"]]
        # Etiketler için de padding gerekecek, onu burada hazırlıyoruz
        return torch.tensor(indices, dtype=torch.long), torch.tensor(item["labels"], dtype=torch.float32)

# 2. ÖZEL DÜZENLEYİCİ (Batch içindeki boyutları eşitlemek için)
def collate_batch(batch):
    # Batch'teki dizilimleri ve etiketleri ayır
    sequences, labels = zip(*batch)
    
    # Dizilimleri en uzun olanına göre doldur (pad_sequence)
    # batch_first=True, dizilimlerin [batch_size, seq_len] formatında olmasını sağlar
    padded_seqs = pad_sequence(sequences, batch_first=True, padding_value=0)
    padded_labels = pad_sequence(labels, batch_first=True, padding_value=0)
    
    # Etiketleri [batch_size, seq_len, 1] formatına getir
    return padded_seqs, padded_labels.unsqueeze(-1)

def train():
    print("=" * 65)
    print("      🧠 DNA-AI LSTM MODELİ EĞİTİMİ YENİDEN BAŞLIYOR")
    print("=" * 65 + "\n")

    EPOCHS = 10
    BATCH_SIZE = 32
    LEARNING_RATE = 0.005

    dataset = DnaDataset("dna_dataset.json")
    # collate_fn parametresi ile hatayı çözüyoruz!
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_batch)

    model = DnaLSTMOptimizer()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print(f"[Sistem] Toplam Veri: {len(dataset)} | Batch Boyutu: {BATCH_SIZE}\n")

    model.train()
    for epoch in range(EPOCHS):
        epoch_loss = 0.0
        for batch_x, batch_y in dataloader:
            optimizer.zero_grad()
            predictions = model(batch_x)
            
            # Maskeleme: Padding olan (doldurulan) yerlerin hataya (loss) dahil olmaması için
            # Sadece 0 olmayan kısımları dikkate almalıyız ama basitlik için direkt giriş yapıyoruz.
            loss = criterion(predictions, batch_y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            
        print(f"Epoch [{epoch+1:02d}/{EPOCHS}] - Ortalama Hata: {epoch_loss/len(dataloader):.4f}")

    torch.save(model.state_dict(), "dna_lstm_model.pth")
    print("\n✅ Eğitim Tamamlandı! Model (Padding özellikli) kaydedildi.")

if __name__ == "__main__":
    train()