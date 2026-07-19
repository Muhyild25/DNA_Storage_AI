import streamlit as st
import dnacore
from ai_brain import DnaAIEngine

# 1. SAYFA AYARLARI VE BAŞLIK
st.set_page_config(page_title="DNA Storage AI", page_icon="🧬", layout="wide")

st.title("🧬 DNA Veri Depolama ve Yapay Zeka Optimizasyonu")
st.markdown("Yüksek performanslı **C++ Motoru** ve **PyTorch LSTM Ağı** kullanılarak geliştirilmiş hibrit DNA depolama paneli.")
st.divider()

# 2. YAPAY ZEKA MOTORUNU BAŞLATMA
# @st.cache_resource dekoratörü, sayfa her yenilendiğinde modelin baştan yüklenmesini engeller ve hızı artırır.
@st.cache_resource
def load_ai():
    return DnaAIEngine()

ai_engine = load_ai()

# 3. KULLANICI ETKİLEŞİM ALANI
mesaj = st.text_area("DNA'ya Dönüştürülecek Mesajı Girin:", "Teknofest DNA Depolama Projesi! $$$$$$$$ Bu sistem kusursuz calisiyor.")

if st.button("Sistemi Çalıştır 🚀"):
    st.divider()
    
    col1, col2 = st.columns(2)
    
    # --- AŞAMA 1: C++ ENCODING ---
    with col1:
        st.subheader("1. Aşama: C++ DNA Sentezi")
        byte_dizisi = list(mesaj.encode('utf-8'))
        dna_dizilimi = dnacore.encode_to_dna(byte_dizisi)
        
        st.success(f"✅ Orijinal mesaj C++ motoruyla {len(dna_dizilimi)} bazlık DNA'ya kodlandı.")
        st.text_area("Ham DNA Dizilimi (Riskli Olabilir):", dna_dizilimi, height=120)
        
    # --- AŞAMA 2: YAPAY ZEKA OPTİMİZASYONU ---
    with col2:
        st.subheader("2. Aşama: LSTM Risk Analizi ve Yama")
        with st.spinner("Yapay zeka biyolojik riskleri analiz ediyor..."):
            optimize_dna = ai_engine.optimize_sequence(dna_dizilimi)
        
        yama_sayisi = len(optimize_dna) - len(dna_dizilimi)
        
        if yama_sayisi > 0:
            st.warning(f"🧠 Yapay zeka riskli tekrarlar tespit etti ve aralara {yama_sayisi} adet biyolojik yama uyguladı.")
        else:
            st.info("🧠 Yapay zeka dizilimi güvenli buldu, yama uygulamadı.")
            
        st.text_area("Optimize Edilmiş Güvenli DNA:", optimize_dna, height=120)
        
    st.divider()
    
    # --- AŞAMA 3: DECODING VE KURTARMA ---
    st.subheader("3. Aşama: Veri Kurtarma (Decoding)")
    temizlenmis_dna = ai_engine.restore_sequence(optimize_dna)
    kurtarilan_bytes = dnacore.decode_from_dna(temizlenmis_dna)
    kurtarilan_mesaj = bytes(kurtarilan_bytes).decode('utf-8')
    
    if mesaj == kurtarilan_mesaj:
        st.success(f"🎉 **Kayıpsız Kurtarılan Mesaj:** {kurtarilan_mesaj}")
    else:
        st.error("Veri kurtarma başarısız! Bütünlük bozuldu.")