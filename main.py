from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
pydantic import BaseModel
import httpx
import os

app = FastAPI(title="Borsa Pro AI & Tarama Motoru", version="1.0")

# CORS Ayarları (Frontend ile haberleşebilmesi için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    symbol: str
    analysis_type: str  # "ai_report", "tavan_taban", "takas", "kap_radar" vb.

# 1. Canlı Teorik Eşleşme Simülasyonu / Veri Servisi
@app.get("/api/teorik-eslesme")
async def get_teorik_eslesme():
    # Burada Borsa İstanbul seans öncesi/kapanış eşleşme verileri çekilir
    return {
        "status": "success",
        "data": [
            {"symbol": "THYAO", "fiyat": 310.50, "fark_yuzde": 2.45, "alis_lot": 1250000, "satis_lot": 450000},
            {"symbol": "GARAN", "fiyat": 112.20, "fark_yuzde": -1.15, "alis_lot": 300000, "satis_lot": 850000}
        ]
    }

# 2. Yapay Zekâ Hisse & Fon Analizi ve Derin Kapsamlı AI Raporu
@app.post("/api/ai-analiz")
async def generate_ai_analysis(req: AnalysisRequest):
    # Gerçek sistemde OpenAI / Claude API buraya entegre edilir.
    # Örnek simüle edilmiş AI yanıtı:
    symbol = req.symbol.upper()
    return {
        "symbol": symbol,
        "rapor_basligi": f"{symbol} - Derin Kapsamlı Yapay Zekâ & Temel Analiz Raporu",
        "teknik_skor": "8.5 / 10 (Güçlü Alım)",
        "temel_analiz": f"{symbol} için son bilanço döneminde net kâr marjında %14 artış gözlemlenmiştir. Yabancı takasındaki toparlanma trendi devam etmektedir.",
        "yapay_zeka_yorumu": "Kısa vadeli hareketli ortalamaların üzerindedir. Hacim momentumu desteklediği sürece yukarı yönlü hareket korunabilir."
    }

# 3. Tavan & Taban Taraması
@app.get("/api/tavan-taban")
async def tavan_taban_taramasi():
    return {
        "tavan_hisseler": ["KARTN", "EGEEN"],
        "taban_hisseler": [],
        "tavana_yaklasanlar": ["PASTR", "BRYAT"]
    }

# 4. Patron & Tahtacı KAP Radarı
@app.get("/api/kap-radar")
async def kap_radar():
    return {
        "son_bildirimler": [
            {"sirket": "EREGL", "aciklama": "Pay Alım Satım Bildirimi - Pay Geri Alım Programı", "saat": "18:02"},
            {"sirket": "SISE", "aciklama": "Özel Durum Açıklaması (Genel)", "saat": "17:45"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
