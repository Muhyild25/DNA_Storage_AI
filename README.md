# 🧬 DNA Storage AI

**Yüksek Performanslı C++ Motoru ve ONNX Yapay Zeka Destekli Biyolojik Veri Depolama Sistemi**

Bu proje, artan küresel veri hacmine karşılık doğanın en kusursuz bilgi saklama molekülü olan DNA'yı kullanarak dijital verileri moleküler düzeyde kodlamak, analiz etmek ve geri kazanmak amacıyla geliştirilmiş otonom bir altyapıdır. Proje, **TÜBİTAK 2209 Araştırma Programı** ve **Teknofest** hedefleri doğrultusunda Eskişehir Osmangazi Üniversitesi bünyesinde hayata geçirilmiştir.

---

## 🚀 Projenin Öne Çıkan Özellikleri

Geleneksel Python tabanlı yavaş veri işleme yöntemleri yerine, bu projede saf C++ performansından ve Microsoft'un ONNX yapay zeka çalışma zamanından (runtime) faydalanılmıştır.

*   **⚡ Saf C++ Çekirdeği:** dnacore kütüphanesi, PyBind11 köprüsü ile doğrudan bellekte (RAM) çalışarak maksimum donanım hızına ulaşır.
*   **🧠 Dinamik ONNX Yapay Zeka Ağı:** Biyolojik risk taşıyan (homopolimer vb.) DNA dizilimleri, dinamik boyutlandırma destekli yapay zeka modeliyle tespit edilir.
*   **📊 Profesyonel Görselleştirme:** Cihaz üzerinde çalışan Streamlit ve Plotly destekli web arayüzü sayesinde veri şifreleme ve risk analizi anlık olarak izlenir.

### ⏱️ Stres Testi ve Performans Rekorları
Geliştirilen hibrit mimari, devasa veri yığınları altında olağanüstü bir performans sergilemektedir:
*   **12.648 Bazlık DNA Sentezi (C++):** 0.0001 saniye
*   **Yapay Zeka Risk Analizi (ONNX):** 0.0166 saniye
*   *(Test donanım limitleri dahilinde dinamik esneme kabiliyeti kanıtlanmıştır.)*

---

## 🏗️ Sistem Mimarisi

1.  **Aşama (C++ Encoding):** Dijital metin veya dosyalar byte dizilerine çevrilir ve yüksek hızlı C++ algoritmalarıyla A, T, C, G nükleotitlerine dönüştürülür.
2.  **Aşama (ONNX Risk Analizi):** Sentezlenen ham DNA, yapay zeka motoruna beslenir. Ortalama risk skoru hesaplanır (Eşik: 0.5) ve biyolojik sentezde hataya yol açabilecek bloklara otomatik yama (padding) uygulanır.
3.  **Aşama (Decoding & Kurtarma):** Güvenli DNA dizilimi, biyolojik yamalardan arındırılır ve tersine çeviri algoritmasıyla kayıpsız bir şekilde orijinal byte verisine dönüştürülür.

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda veya sunucunuzda çalıştırmak için aşağıdaki komutları sırasıyla terminalinize yapıştırabilirsiniz:

```bash
git clone https://github.com/Muhyild25/DNA_Storage_AI.git
cd DNA_Storage_AI
pip install -r ai_model/requirements.txt
cd ai_model
python setup.py build_ext --inplace
streamlit run app.py

👨‍💻 Geliştirici
Muhammed Yıldırım - Eskişehir Osmangazi Üniversitesi, Bilgisayar Mühendisliği