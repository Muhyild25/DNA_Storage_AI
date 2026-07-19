/**
 * @file wrapper.cpp
 * @brief DNA Storage C++ Motoru - Python (pybind11) Köprüsü
 *
 * Bu dosya, yüksek performanslı C++ çekirdek fonksiyonlarını Python
 * ortamına yerel bir kütüphane ('dnacore') olarak bağlamak için kullanılır.
 *
 * Not: Bu proje, DNA Storage araştırma ekibinin vizyonunu ve anısını
 * yaşatmak amacıyla geliştirilmiştir.
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // std::vector ve std::string dönüşümleri için
#include "DnaCore.h"

#include <onnxruntime_cxx_api.h>
#include <vector>
#include <numeric>
#include <string>

namespace py = pybind11;

// DNA harflerini modelin anlayacağı rakamlara çeviren yardımcı fonksiyon
int base_to_idx(char base) {
    switch (base) {
        case 'A': return 0;
        case 'C': return 1;
        case 'G': return 2;
        case 'T': return 3;
        default: return 0;
    }
}

// Yüksek Performanslı ONNX Yapay Zeka Motoru Sınıfı
class DnaAiEngine {
private:
    Ort::Env env;
    Ort::Session* session;
    Ort::MemoryInfo memory_info;

public:
    // Sınıf başlatıldığında ONNX modelini doğrudan RAM'e yükler
    DnaAiEngine(const std::string& model_path) 
        : env(ORT_LOGGING_LEVEL_WARNING, "DnaAiEngine"), 
          memory_info(Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault)) 
    {
        // Windows ortamı için dosya yolunu geniş karaktere çevirme
        std::wstring w_model_path(model_path.begin(), model_path.end());
        Ort::SessionOptions session_options;
        session_options.SetIntraOpNumThreads(1); // CPU optimizasyonu
        
        session = new Ort::Session(env, w_model_path.c_str(), session_options);
    }

    ~DnaAiEngine() {
        delete session;
    }

    // Gelen DNA diziliminin risk skorunu hesaplayan ana fonksiyon
    float analyze_risk(const std::string& dna_sequence) {
        size_t seq_length = dna_sequence.length();
        if (seq_length == 0) return 0.0f;

        std::vector<int64_t> input_tensor_values(seq_length);
        
        // 1. AŞAMA: Metni Tensöre Çevir
        for (size_t i = 0; i < seq_length; ++i) {
            input_tensor_values[i] = base_to_idx(dna_sequence[i]);
        }

        std::vector<int64_t> input_shape = {1, (int64_t)seq_length};
        
        Ort::Value input_tensor = Ort::Value::CreateTensor<int64_t>(
            memory_info, input_tensor_values.data(), input_tensor_values.size(),
            input_shape.data(), input_shape.size()
        );

        const char* input_names[] = {"input"};
        const char* output_names[] = {"output"};

        // 2. AŞAMA: Yapay Zeka Çıkarımı (Inference)
        auto output_tensors = session->Run(
            Ort::RunOptions{nullptr}, input_names, &input_tensor, 1, output_names, 1
        );

        // 3. AŞAMA: Sonuçları Okuma
        float* floatarr = output_tensors.front().GetTensorMutableData<float>();
        
        float total_risk = 0;
        for(size_t i = 0; i < seq_length; ++i){
            total_risk += floatarr[i];
        }
        
        // Ortalama risk skorunu döndür
        return total_risk / seq_length;
    }
};

// Python'a aktarılacak 'dnacore' modülünün tanımlanması
PYBIND11_MODULE(dnacore, m) {
    m.doc() = "DNA Storage C++ Core Engine - Yüksek Performanslı Python Köprüsü";

    // Orijinal C++ fonksiyonlarının Python'a tanıtılması (Senin Kodların)
    m.def("read_file", &readFile, "Dosyayi ikili (binary) formatta okur ve byte dizisi dondurur.");
    m.def("write_file", &writeFile, "String veya byte verisini hedef dosyaya yazar.");
    m.def("encode_to_dna", &encodeToDNA, "Ham byte dizisini biyolojik DNA bazlarina (A, T, C, G) sentezler.");
    m.def("decode_from_dna", &decodeFromDNA, "DNA dizilimini geri cozerek orijinal byte verisini kurtarir.");
    m.def("analyze_biological_errors", &analyzeBiologicalErrors, "Sentezlenen DNA'daki biyolojik riskleri (homopolimerleri) raporlar.");

    // YENİ: ONNX Yapay Zeka Motoru Bağlantısı
    py::class_<DnaAiEngine>(m, "DnaAiEngine")
        .def(py::init<const std::string &>())
        .def("analyze_risk", &DnaAiEngine::analyze_risk);
}