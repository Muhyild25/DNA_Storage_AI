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

namespace py = pybind11;

// Python'a aktarılacak 'dnacore' modülünün tanımlanması
PYBIND11_MODULE(dnacore, m) {
    m.doc() = "DNA Storage C++ Core Engine - Yüksek Performanslı Python Köprüsü";

    // C++ fonksiyonlarının Python'a tanıtılması ve docstring'lerinin eklenmesi
    m.def("read_file", &readFile, "Dosyayi ikili (binary) formatta okur ve byte dizisi dondurur.");
    m.def("write_file", &writeFile, "String veya byte verisini hedef dosyaya yazar.");
    m.def("encode_to_dna", &encodeToDNA, "Ham byte dizisini biyolojik DNA bazlarina (A, T, C, G) sentezler.");
    m.def("decode_from_dna", &decodeFromDNA, "DNA dizilimini geri cozerek orijinal byte verisini kurtarir.");
    m.def("analyze_biological_errors", &analyzeBiologicalErrors, "Sentezlenen DNA'daki biyolojik riskleri (homopolimerleri) raporlar.");
}