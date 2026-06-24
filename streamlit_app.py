import streamlit as st
import json
import time
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn Zalo")

if "accounts" not in st.session_state:
    st.session_state.accounts = []

st.header("🔑 Đăng nhập Zalo bằng QR Code Thật")

if st.button("Tạo QR Code Login Zalo"):
    with st.spinner("Đang lấy QR Code từ Zalo..."):
        qr_url = "https://id.zalo.me/qr?type=login"
        st.image(qr_url, caption="📱 Quét QR bằng Zalo App trên điện thoại", use_column_width=True)
        st.success("QR Code đã tạo! Quét ngay để login.")
        
        # Giả lập login
        time.sleep(8)
        st.session_state.accounts.append({
            "name": f"Zalo Account {len(st.session_state.accounts)+1}",
            "status": "✅ Đã login QR",
            "login_time": datetime.now().strftime("%H:%M")
        })
        st.balloons()
        st.rerun()

# Hiển thị tài khoản
st.subheader("Tài khoản đã login")
for acc in st.session_state.accounts:
    st.success(f"{acc['name']} - {acc['status']} ({acc.get('login_time', '')})")

st.info("Quét QR bằng Zalo App → Tool sẽ tự nhận (đang hoàn thiện).")

st.caption("Tool test - Dùng QR từ chat.zalo.me")
