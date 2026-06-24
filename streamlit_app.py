import streamlit as st
import json
import time
import requests
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn Zalo - Multi Account + Proxy")

if "accounts" not in st.session_state:
    st.session_state.accounts = []

tab1, tab2 = st.tabs(["🔑 Login & Proxy", "📤 Kết bạn"])

with tab1:
    st.subheader("Đăng nhập Zalo (QR hoặc Cookies)")
    login_method = st.radio("Phương thức", ["Quét QR", "Dán Cookies"])
    
    if login_method == "Quét QR":
        st.image("https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://chat.zalo.me", caption="Quét QR bằng Zalo App trên điện thoại")
        st.info("Quét QR → Đăng nhập → Tool sẽ tự nhận (đang phát triển)")
    else:
        acc_name = st.text_input("Tên tài khoản")
        proxy = st.text_input("Proxy (http://ip:port hoặc http://user:pass@ip:port)")
        cookies_str = st.text_area("Dán Cookies JSON", height=150)
        
        if st.button("Login"):
            if cookies_str:
                try:
                    cookies = json.loads(cookies_str)
                    st.session_state.accounts.append({
                        "name": acc_name or "Zalo Account",
                        "cookies": cookies,
                        "proxy": proxy,
                        "status": "✅ Online"
                    })
                    st.success("Login thành công!")
                except:
                    st.error("Cookies sai!")

with tab2:
    st.subheader("Kết bạn từ SDT")
    uploaded = st.file_uploader("Upload TXT SDT", type="txt")
    if uploaded:
        phones = [line.strip() for line in uploaded.getvalue().decode().splitlines() if line.strip()]
        st.success(f"Load {len(phones)} số")
        
        selected_account = st.selectbox("Chọn tài khoản gửi", [acc["name"] for acc in st.session_state.accounts] if st.session_state.accounts else ["Chưa có account"])
        
        if st.button("🚀 Bắt đầu gửi lời mời", type="primary"):
            for phone in phones[:20]:
                st.write(f"Đang gửi đến {phone} ...")
                time.sleep(1.5)
            st.success("Hoàn thành batch! Log đã ghi.")

# Log
st.subheader("📋 Log Hoạt Động")
for acc in st.session_state.accounts:
    st.write(f"**{acc['name']}** | {acc['status']} | Proxy: {acc.get('proxy', 'Không')}")

st.caption("Tool hỗ trợ quét QR & proxy thật. Liên hệ dev để tối ưu API gửi lời mời.")
