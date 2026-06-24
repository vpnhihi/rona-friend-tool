import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn từ SDT - Zalo")

st.write("Phiên bản test - Đang hoàn thiện")

uploaded_file = st.file_uploader("Upload file Excel/CSV danh sách SDT", type=["xlsx", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.success(f"Đã load {len(df)} số điện thoại!")
    st.dataframe(df.head())

st.button("Bắt đầu gửi lời mời", type="primary")

st.info("Tool đang trong giai đoạn test. Contact dev để thêm tính năng đầy đủ.")
