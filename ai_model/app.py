import streamlit as st
import dnacore
import time
import plotly.graph_objects as go

# 1. SAYFA AYARLARI VE BAŞLIK
st.set_page_config(page_title="DNA Storage AI", page_icon="🧬", layout="wide")

st.title("🧬 DNA Veri Depolama ve Yapay Zeka Optimizasyonu")
st.markdown("Yüksek performanslı **C++ Motoru** ve **ONNX Yapay Zeka Ağı** kullanılarak geliştirilmiş otonom DNA depolama paneli.")
st.divider()

# 2. C++ YAPAY ZEKA MOTORUNU BAŞLATMA
@st.cache_resource
def load_ai():
    return dnacore.DnaAiEngine("dna_ai_model.onnx")

ai_engine = load_ai()

# --- YARDIMCI FONKSİYONLAR ---
def optimize_sequence(dna_seq, risk_score):
    if risk_score > 0.5:
        return dna_seq + "GC"
    return dna_seq

def restore_sequence(dna_seq):
    if dna_seq.endswith("GC"):
        return dna_seq[:-2]
    return dna_seq
# -----------------------------

# 3. KULLANICI ETKİLEŞİM ALANI
mesaj = st.text_area("DNA'ya Dönüştürülecek Mesajı Girin:", "Teknofest DNA Depolama Projesi! $$$$$$$$ Bu sistem kusursuz calisiyor.")

if st.button("Sistemi Çalıştır 🚀"):
    st.divider()
    
    col1, col2 = st.columns(2)
    
    # --- AŞAMA 1: C++ ENCODING ---
    with col1:
        st.subheader("1. Aşama: C++ DNA Sentezi")
        start_time = time.time()
        
        byte_dizisi = list(mesaj.encode('utf-8'))
        dna_dizilimi = dnacore.encode_to_dna(byte_dizisi)
        
        encode_sure = time.time() - start_time
        
        st.success(f"✅ Orijinal mesaj C++ motoruyla {len(dna_dizilimi)} bazlık DNA'ya kodlandı. (Süre: {encode_sure:.4f} sn)")
        st.text_area("Ham DNA Dizilimi (Riskli Olabilir):", dna_dizilimi, height=150)
        
    # --- AŞAMA 2: YAPAY ZEKA OPTİMİZASYONU ---
    with col2:
        st.subheader("2. Aşama: ONNX Risk Analizi")
        with st.spinner("C++ Çekirdeği yapay zeka analizi yapıyor..."):
            start_time = time.time()
            risk_skoru = ai_engine.analyze_risk(dna_dizilimi)
            optimize_dna = optimize_sequence(dna_dizilimi, risk_skoru)
            ai_sure = time.time() - start_time
        
        # --- GÖRSELLEŞTİRME (PLOTLY GAUGE CHART) ---
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = risk_skoru,
            title = {'text': "Biyolojik Risk Skoru", 'font': {'size': 20}},
            number = {'valueformat': ".4f"},
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge = {
                'axis': {'range': [0, 1]},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0, 0.4], 'color': "#abf7b1"},  # Güvenli (Yeşil)
                    {'range': [0.4, 0.5], 'color': "#f7e4ab"}, # Sınır (Sarı)
                    {'range': [0.5, 1.0], 'color': "#f7abab"}  # Riskli (Kırmızı)
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 0.5
                }
            }
        ))
        
        fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, width='stretch')
        
        # Analiz Sonucu Metni
        yama_sayisi = len(optimize_dna) - len(dna_dizilimi)
        if risk_skoru > 0.5:
            st.warning(f"⚠️ Yüksek Risk! {yama_sayisi} adet biyolojik yama uygulandı. (Süre: {ai_sure:.4f} sn)")
        else:
            st.info(f"✅ Düşük Risk. Dizilim güvenli, yama uygulanmadı. (Süre: {ai_sure:.4f} sn)")
            
        st.text_area("Optimize Edilmiş Güvenli DNA:", optimize_dna, height=150)
        
    st.divider()
    
    # --- AŞAMA 3: DECODING VE KURTARMA ---
    st.subheader("3. Aşama: Veri Kurtarma (Decoding)")
    start_time = time.time()
    
    temizlenmis_dna = restore_sequence(optimize_dna)
    kurtarilan_bytes = dnacore.decode_from_dna(temizlenmis_dna)
    kurtarilan_mesaj = bytes(kurtarilan_bytes).decode('utf-8')
    
    decode_sure = time.time() - start_time
    
    if mesaj == kurtarilan_mesaj:
        st.success(f"🎉 **Kayıpsız Kurtarılan Mesaj:** {kurtarilan_mesaj} (Çözme Süresi: {decode_sure:.4f} sn)")
    else:
        st.error("❌ Veri kurtarma başarısız! Bütünlük bozuldu.")