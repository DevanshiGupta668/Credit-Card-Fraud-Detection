import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Credit Card Fraud Detector",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LOAD TRAINED MODEL
# =========================================================

pipeline = joblib.load("model/fraud_pipeline.joblib")

# =========================================================
# PREMIUM UI CSS
# =========================================================

st.markdown("""
<style>
/* ---------- GLOBAL ---------- */

.stApp {
    background: #f6f7fb;
    color: #171a2b;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ---------- HEADER ---------- */

.header-box {
    background: linear-gradient(135deg, #111827 0%, #1e1b4b 100%);
    border-radius: 22px;
    padding: 22px 28px;
    margin-bottom: 25px;
    box-shadow: 0 15px 40px rgba(30, 27, 75, 0.18);
}

.header-left {
    display: inline-block;
    vertical-align: middle;
}

.header-icon {
    display: inline-flex;
    width: 48px;
    height: 48px;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    border-radius: 14px;
    font-size: 24px;
    margin-right: 13px;
    vertical-align: middle;
}

.header-text {
    display: inline-block;
    vertical-align: middle;
}

.header-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 800;
    margin: 0;
}

.header-subtitle {
    color: #a5b4fc;
    font-size: 12px;
    margin-top: 3px;
}

.header-status {
    float: right;
    margin-top: 6px;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(74, 222, 128, 0.25);
    color: #86efac;
    border-radius: 30px;
    padding: 9px 14px;
    font-size: 12px;
    font-weight: 700;
}

.status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    background: #4ade80;
    border-radius: 50%;
    margin-right: 6px;
}

/* ---------- HERO ---------- */

.hero-box {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #4f46e5 0%, #6366f1 45%, #7c3aed 100%);
    border-radius: 25px;
    padding: 48px 45px;
    margin-bottom: 28px;
    box-shadow: 0 18px 45px rgba(79, 70, 229, 0.22);
}

.hero-box:after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border: 55px solid rgba(255,255,255,0.08);
    border-radius: 50%;
    right: -95px;
    top: -130px;
}

.hero-small {
    color: #ddd6fe;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-title {
    color: #ffffff;
    font-size: 40px;
    font-weight: 850;
    letter-spacing: -1px;
    line-height: 1.1;
    margin: 0;
}

.hero-description {
    color: #e0e7ff;
    font-size: 15px;
    line-height: 1.65;
    max-width: 680px;
    margin-top: 15px;
}

/* ---------- SECTION ---------- */

.section-title {
    font-size: 19px;
    font-weight: 800;
    color: #181b2f;
    margin-top: 25px;
    margin-bottom: 6px;
}

.section-description {
    color: #7b8195;
    font-size: 13px;
    margin-bottom: 15px;
}

/* ---------- SETTINGS CARD ---------- */

.settings-card {
    background: #ffffff;
    border: 1px solid #e5e7ef;
    border-radius: 18px;
    padding: 20px 24px 10px 24px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(24, 27, 47, 0.05);
}

.settings-label {
    color: #30344b;
    font-size: 14px;
    font-weight: 700;
}

.settings-text {
    color: #8a90a3;
    font-size: 12px;
    margin-top: 3px;
}

/* ---------- FILE UPLOADER ---------- */

[data-testid="stFileUploader"] {
    background: #ffffff;
    border: 1px solid #e5e7ef;
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 8px 25px rgba(24, 27, 47, 0.05);
}

[data-testid="stFileUploaderDropzone"] {
    background: #f8f8ff;
    border: 2px dashed #c7c9f7;
    border-radius: 14px;
    min-height: 135px;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #6366f1;
    background: #f4f4ff;
}

/* ---------- SLIDER ---------- */

[data-testid="stSlider"] {
    padding-top: 4px;
}

/* ---------- RESULT MESSAGE ---------- */

.fraud-box {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    color: #be123c;
    border-radius: 15px;
    padding: 15px 18px;
    margin: 22px 0;
    font-size: 14px;
    font-weight: 700;
}

.safe-box {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    color: #15803d;
    border-radius: 15px;
    padding: 15px 18px;
    margin: 22px 0;
    font-size: 14px;
    font-weight: 700;
}

/* ---------- RESULTS CARD ---------- */

.results-heading {
    background: linear-gradient(135deg, #111827, #27204f);
    color: #ffffff;
    border-radius: 18px 18px 0 0;
    padding: 19px 23px;
    margin-top: 25px;
}

.results-title {
    font-size: 18px;
    font-weight: 800;
}

.results-subtitle {
    color: #aeb4c8;
    font-size: 12px;
    margin-top: 4px;
}

/* ---------- DATAFRAME ---------- */

[data-testid="stDataFrame"] {
    border: 1px solid #e5e7ef;
    border-radius: 0 0 18px 18px;
    overflow: hidden;
}

/* ---------- DOWNLOAD BUTTON ---------- */

.stDownloadButton > button {
    width: 100%;
    min-height: 48px;
    border: none !important;
    border-radius: 13px !important;
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    font-weight: 750 !important;
    box-shadow: 0 8px 22px rgba(79, 70, 229, 0.20);
}

.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #4338ca, #6d28d9) !important;
}

/* ---------- EMPTY STATE ---------- */

.empty-box {
    background: #ffffff;
    border: 1px solid #e5e7ef;
    border-radius: 20px;
    text-align: center;
    padding: 40px 20px;
    margin-top: 22px;
    box-shadow: 0 8px 25px rgba(24, 27, 47, 0.05);
}

.empty-icon {
    font-size: 38px;
    margin-bottom: 8px;
}

.empty-title {
    color: #20233a;
    font-size: 18px;
    font-weight: 800;
}

.empty-text {
    color: #858b9e;
    font-size: 13px;
    margin-top: 6px;
}

/* ---------- FOOTER ---------- */

.footer-box {
    text-align: center;
    color: #9298aa;
    font-size: 11px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #e5e7ef;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header-box">
    <div class="header-left">
        <span class="header-icon">🛡️</span>
        <span class="header-text">
            <div class="header-title">CreditGuard</div>
            <div class="header-subtitle">Intelligent Credit Card Fraud Detection</div>
        </span>
    </div>
    <span class="header-status">
        <span class="status-dot"></span>
        Model Ready
    </span>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero-box">
    <div class="hero-small">AI • MACHINE LEARNING • SECURITY</div>
    <div class="hero-title">Credit Card Fraud Detector</div>
    <div class="hero-description">
        Upload a transaction dataset and use the trained machine learning
        model to identify transactions that may look fraudulent.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# THRESHOLD
# =========================================================

st.markdown(
    '<div class="section-title">Detection Settings</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Adjust the fraud probability threshold used to flag transactions.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="settings-card">
    <div class="settings-label">Fraud Probability Threshold</div>
    <div class="settings-text">
        Transactions at or above this probability will be flagged.
    </div>
</div>
""", unsafe_allow_html=True)

threshold = st.slider(
    "Fraud probability threshold",
    0.0,
    1.0,
    0.5,
    0.01,
    label_visibility="collapsed"
)

# =========================================================
# UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">Transaction Data</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Upload your transactions in CSV format to begin detection.</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload transactions CSV",
    type="csv"
)

# =========================================================
# ORIGINAL ML FUNCTIONALITY
# =========================================================

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    # Drop the label column if it is present
    features = data.drop(columns=["Class"], errors="ignore")

    # Predict fraud probability
    fraud_probs = pipeline.predict_proba(features)[:, 1]

    # Create results
    results = data.copy()
    results["fraud_probability"] = fraud_probs
    results["flagged"] = fraud_probs >= threshold

    # Count flagged transactions
    flagged_count = int(results["flagged"].sum())
    total_count = len(results)

    # =====================================================
    # RESULT MESSAGE
    # =====================================================

    if flagged_count > 0:
        st.markdown(
            f"""
<div class="fraud-box">
🚨 {flagged_count} transaction(s) flagged as potentially fraudulent out of {total_count} transaction(s).
</div>
""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
<div class="safe-box">
✓ No transactions were flagged out of {total_count} analyzed transaction(s).
</div>
""",
            unsafe_allow_html=True
        )

    # =====================================================
    # RESULTS
    # =====================================================

    st.markdown("""
<div class="results-heading">
    <div class="results-title">Detection Results</div>
    <div class="results-subtitle">
        Transactions sorted from highest to lowest fraud probability
    </div>
</div>
""", unsafe_allow_html=True)

    st.dataframe(
        results.sort_values(
            "fraud_probability",
            ascending=False
        ),
        use_container_width=True,
        height=450
    )

    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.markdown(
        '<div class="section-title">Export Results</div>',
        unsafe_allow_html=True
    )

    csv = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️  Download Scored CSV",
        csv,
        "scored_transactions.csv",
        "text/csv",
        use_container_width=True
    )

else:

    # =====================================================
    # EMPTY STATE
    # =====================================================

    st.markdown("""
<div class="empty-box">
    <div class="empty-icon">📄</div>
    <div class="empty-title">Ready for analysis</div>
    <div class="empty-text">
        Upload a transaction CSV above to begin fraud detection.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer-box">
    🛡️ CreditGuard &nbsp;•&nbsp; Credit Card Fraud Detection System
    <br><br>
    Powered by Machine Learning
</div>
""", unsafe_allow_html=True)