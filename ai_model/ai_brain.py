"""
=============================================================================
DNA Storage AI - Deep Learning Brain (LSTM)
=============================================================================
"""

import torch
import torch.nn as nn
import numpy as np
import os

BASE_TO_IDX = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
IDX_TO_BASE = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

class DnaLSTMOptimizer(nn.Module):
    def __init__(self, vocab_size=4, embedding_dim=8, hidden_dim=16):
        super(DnaLSTMOptimizer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        out = self.fc(lstm_out)
        return self.sigmoid(out)

class DnaAIEngine:
    def __init__(self, model_path="dna_lstm_model.pth"):
        print("[AI Engine] 🧠 DNA-AI LSTM Motoru Başlatılıyor...")
        self.model = DnaLSTMOptimizer()
        
        # Eğitilmiş modeli yükleme
        if os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, weights_only=True))
            print(f"[AI Engine] 💾 Eğitilmiş uzman zeka ({model_path}) başarıyla yüklendi!")
        else:
            print("[AI Engine] ⚠️ Model bulunamadı! Rastgele ağırlıklarla çalışıyor.")
            
        self.model.eval()
        self.padding_indices = [] # Eklediğimiz yamaların koordinatlarını tutacağımız geçici hafıza

    def sequence_to_tensor(self, dna_seq):
        indices = [BASE_TO_IDX.get(base, 0) for base in dna_seq]
        return torch.tensor(indices, dtype=torch.long).unsqueeze(0)

    def optimize_sequence(self, dna_seq, threshold=0.5):
        tensor_data = self.sequence_to_tensor(dna_seq)
        
        with torch.no_grad(): 
            risk_scores = self.model(tensor_data)
        
        scores_flat = risk_scores.squeeze().numpy()
        
        optimized_seq = ""
        padding_count = 0
        self.padding_indices.clear()
        
        # Dizilimi harf harf analiz et
        for i, base in enumerate(dna_seq):
            optimized_seq += base
            
            # Model bu noktada biyolojik kopma riski görüyorsa
            if scores_flat[i] > threshold:
                # Oraya zıt bir baz ile biyolojik yama (padding) yap
                pad_base = 'C' if base in ['A', 'T'] else 'A'
                optimized_seq += pad_base
                padding_count += 1
                
                # Gelecekte geri çıkarabilmek için yamanın eklendiği adresi kaydet
                self.padding_indices.append(len(optimized_seq) - 1)
                
        print(f"[AI Engine] 🔍 Orijinal Uzunluk: {len(dna_seq)} baz")
        print(f"[AI Engine] 💉 Eklenen Biyolojik Yama Sayısı: {padding_count}")
        print(f"[AI Engine] 🛡️ Optimize Edilmiş Yeni Uzunluk: {len(optimized_seq)} baz")
        
        return optimized_seq

    def restore_sequence(self, optimized_seq):
        """
        Eklenen yamaları dizilimden çıkararak orijinal DNA'yı C++ motoruna verir.
        """
        restored_seq = list(optimized_seq)
        # İndekslerin kaymaması için listeyi sondan başa doğru siliyoruz
        for idx in reversed(self.padding_indices):
            if idx < len(restored_seq):
                del restored_seq[idx]
                
        self.padding_indices.clear()
        return "".join(restored_seq)