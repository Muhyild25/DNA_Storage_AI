#include <iostream>
#include "DnaCore.h"

using namespace std;

int main() {
    cout << "=====================================================" << endl;
    cout << "    DNA STORAGE C++ CORE ENGINE (KUTUPHANE MODU)     " << endl;
    cout << "=====================================================\n" << endl;

    // Dosya yolu tanımlamaları
    string inputFilename = "mesaj.txt";
    string dnaFilename = "depo.fasta";
    string outputFilename = "kurtarilan_mesaj.txt";

    // 1. Veri Okuma İşlemi
    cout << "[Adım 1] '" << inputFilename << "' dosyasi okunuyor..." << endl;
    vector<uint8_t> fileData = readFile(inputFilename);
    if (fileData.empty()) {
        cout << "-> Islem sonlandirildi. Lutfen girdi dosyasini kontrol edin." << endl;
        return 1;
    }

    // 2. DNA Sentezleme (Encoding) ve Biyolojik Analiz
    cout << "[Adım 2] Veri DNA bazlarina donusturuluyor..." << endl;
    string dnaData = encodeToDNA(fileData);
    writeFile(dnaFilename, dnaData);
    cout << "-> Sentezlenen DNA dizilimi '" << dnaFilename << "' dosyasina kaydedildi." << endl;

    analyzeBiologicalErrors(dnaData);

    // 3. DNA Çözümleme (Decoding) ve Veri Kurtarma
    cout << "[Adım 3] DNA verisi geri cozuluyor..." << endl;
    vector<uint8_t> restoredData = decodeFromDNA(dnaData);
    string restoredString(restoredData.begin(), restoredData.end());
    writeFile(outputFilename, restoredString);
    cout << "-> Kurtarilan veri '" << outputFilename << "' dosyasina basariyla kaydedildi." << endl;

    cout << "\n>>> BUTUN ISLEMLER BASARIYLA TAMAMLANDI! <<<" << endl;

    return 0;
}