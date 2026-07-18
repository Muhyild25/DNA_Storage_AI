#include "DnaCore.h"
#include <iostream>
#include <fstream>

using namespace std;

// --- ÝÇ YARDIMCI FONKSÝYONLAR ---

// 2-bitlik veriyi (0b00 - 0b11 arasý) karþýlýk gelen DNA bazýna eþler
char bitsToBase(uint8_t bits) {
    switch (bits) {
    case 0b00: return 'A';
    case 0b01: return 'C';
    case 0b10: return 'G';
    case 0b11: return 'T';
    default: return 'N';
    }
}

// DNA bazýný tekrar 2-bitlik sayýsal veriye dönüþtürür
uint8_t baseToBits(char base) {
    switch (base) {
    case 'A': return 0b00;
    case 'C': return 0b01;
    case 'G': return 0b10;
    case 'T': return 0b11;
    default: return 0b00;
    }
}

// --- ANA MOTOR FONKSÝYONLARI ---

vector<uint8_t> readFile(const string& filename) {
    ifstream file(filename, ios::binary);
    if (!file) {
        cerr << "HATA: '" << filename << "' dosyasi bulunamadi!" << endl;
        return {};
    }
    return vector<uint8_t>((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
}

void writeFile(const string& filename, const string& data) {
    ofstream file(filename, ios::binary);
    file << data;
    file.close();
}

string encodeToDNA(const vector<uint8_t>& data) {
    string dnaSequence = "";
    // Performans optimizasyonu: Bellek tahsisini baþtan yap (1 Byte = 4 DNA bazý)
    dnaSequence.reserve(data.size() * 4);

    for (uint8_t byte : data) {
        // Bitwise maskeleme ile 2-bitlik parçalarýn çýkarýlmasý
        dnaSequence += bitsToBase((byte >> 6) & 0b11);
        dnaSequence += bitsToBase((byte >> 4) & 0b11);
        dnaSequence += bitsToBase((byte >> 2) & 0b11);
        dnaSequence += bitsToBase(byte & 0b11);
    }
    return dnaSequence;
}

vector<uint8_t> decodeFromDNA(const string& dnaSequence) {
    vector<uint8_t> decodedData;
    decodedData.reserve(dnaSequence.length() / 4);

    for (size_t i = 0; i < dnaSequence.length(); i += 4) {
        uint8_t bits1 = baseToBits(dnaSequence[i]);
        uint8_t bits2 = baseToBits(dnaSequence[i + 1]);
        uint8_t bits3 = baseToBits(dnaSequence[i + 2]);
        uint8_t bits4 = baseToBits(dnaSequence[i + 3]);

        // Sola kaydýrma ve OR operatörü ile byte'ýn yeniden inþasý
        decodedData.push_back((bits1 << 6) | (bits2 << 4) | (bits3 << 2) | bits4);
    }
    return decodedData;
}

void analyzeBiologicalErrors(const string& dnaSequence) {
    int maxRepeat = 4; // Biyolojik risk eþiði (4 ve üzeri homopolimer)
    int currentRepeat = 1;
    int totalErrors = 0;

    cout << "\n--- Biyolojik Hata Analizi (Homopolimer Taramasi) ---" << endl;

    for (size_t i = 1; i < dnaSequence.length(); ++i) {
        if (dnaSequence[i] == dnaSequence[i - 1]) {
            currentRepeat++;
        }
        else {
            if (currentRepeat >= maxRepeat) {
                cout << "-> RÝSKLÝ BÖLGE: " << currentRepeat << " adet yan yana '"
                    << dnaSequence[i - 1] << "' tespit edildi. (Ýndeks: " << (i - currentRepeat) << ")" << endl;
                totalErrors++;
            }
            currentRepeat = 1;
        }
    }

    // Döngü sonu kontrolü
    if (currentRepeat >= maxRepeat) {
        cout << "-> RÝSKLÝ BÖLGE: " << currentRepeat << " adet yan yana '"
            << dnaSequence.back() << "' tespit edildi. (Ýndeks: " << (dnaSequence.length() - currentRepeat) << ")" << endl;
        totalErrors++;
    }

    if (totalErrors == 0) {
        cout << "Durum: Baþarýlý. Dizilimde kritik bir homopolimer (tekrar) hatasý bulunmadý." << endl;
    }
    else {
        cout << ">> Toplam " << totalErrors << " adet riskli bölge bulundu." << endl;
        cout << ">> Not: Gelecekteki YZ/Python katmaný bu dizilimleri optimize edecektir." << endl;
    }
    cout << "-----------------------------------------------------\n" << endl;
}