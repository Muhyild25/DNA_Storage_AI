/**
 * @file DnaCore.h
 * @brief DNA Veri Depolama Sistemi Çekirdek Motoru
 *
 * Bu kütüphane, dijital verilerin (binary) biyolojik DNA dizilimlerine (A, T, C, G)
 * dönüþtürülmesi (encoding) ve geri çözülmesi (decoding) süreçlerini yönetir.
 * Ayrýca DNA sentezinde oluþabilecek biyolojik hatalarý (homopolimer vb.) analiz eder.
 *
 * Not: Bu proje, DNA Storage araþtýrma ekibinin vizyonunu ve anýsýný
 * yaþatmak amacýyla geliþtirilmiþtir.
 */

#pragma once
#include <vector>
#include <string>
#include <cstdint>

 /**
  * @brief Ýkili dosyayý (binary) okur ve byte dizisi olarak döndürür.
  * @param filename Okunacak dosyanýn yolu/adý.
  * @return Dosya içeriðini barýndýran 8-bitlik veri vektörü.
  */
std::vector<uint8_t> readFile(const std::string& filename);

/**
 * @brief Verilen içeriði ikili formatta yeni bir dosyaya yazar.
 * @param filename Oluþturulacak dosyanýn yolu/adý.
 * @param data Dosyaya yazýlacak string veri (DNA dizilimi veya kurtarýlan metin).
 */
void writeFile(const std::string& filename, const std::string& data);

/**
 * @brief Ham byte dizisini DNA bazlarýna çevirir.
 * @param data Dönüþtürülecek 8-bitlik veri vektörü.
 * @return Sentezlenmiþ DNA dizilimi (A, T, C, G formatýnda string).
 */
std::string encodeToDNA(const std::vector<uint8_t>& data);

/**
 * @brief DNA dizilimini geri çözerek orijinal byte dizisini elde eder.
 * @param dnaSequence Çözülecek DNA string dizilimi.
 * @return Orijinal dosyayý temsil eden 8-bitlik veri vektörü.
 */
std::vector<uint8_t> decodeFromDNA(const std::string& dnaSequence);

/**
 * @brief DNA dizilimindeki biyolojik riskleri (homopolimerler) tarar ve terminale raporlar.
 * @param dnaSequence Analiz edilecek DNA string dizilimi.
 */
void analyzeBiologicalErrors(const std::string& dnaSequence);