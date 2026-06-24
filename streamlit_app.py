import streamlit as st
import json
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide", page_icon="🚀")

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn từ SDT - Zalo")

# Khởi tạo session state
if "accounts" not in st.session_state:
    st.session_state.accounts = []

# Sidebar - Login Zalo
with st.sidebar:
    st.header("🔑 Đăng nhập Zalo Thật")
    
    acc_name = st.text_input("Tên tài khoản", value=f"Zalo Account {len(st.session_state.accounts) + 1}")
    proxy = st.text_input("Proxy (HTTP/HTTPS)", placeholder="http://user:pass@ip:port")
    
    cookies_str = st.text_area("Dán Cookies từ chat.zalo.me (JSON)", height=250,
                              help="1. Mở chat.zalo.me\n2. Đăng nhập\n3. F12 → Application → Cookies → Copy toàn bộ")
    
    if st.button("✅ Login Zalo", type="primary"):
        if cookies_str and cookies_str.strip():
            try:
                cookies = json.loads(cookies_str)
                st.session_state.accounts.append({
                    "name": acc_name,
                    "cookies": cookies,
                    "proxy": proxy,
                    "status": "✅ Đã login",
                    "login_time": datetime.now().strftime("%H:%M:%S")
                })
                st.success(f"Đăng nhập {acc_name} thành công!")
            except Exception as e:
                st.error(f"Lỗi cookies: {str(e)}")
        else:
            st.warning("Vui lòng dán cookies JSON!")

# Main Area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Danh sách Tài khoản")
    if st.session_state.accounts:
        for i, acc in enumerate(st.session_state.accounts):
            st.write(f"**{acc['name']}** | {acc['status']} | Proxy: {acc.get('proxy', 'Không')}")
    else:
        st.info("Chưa có tài khoản nào. Hãy login ở sidebar.")

with col2:
    st.subheader("📤 Upload SDT (TXT)")
    uploaded_file = st.file_uploader("Chọn file TXT (mỗi dòng 1 số điện thoại)", type="txt")
    
    if uploaded_file:
        phones = [line.strip() for line in uploaded_file.getvalue().decode("utf-8").splitlines() if line.strip()]
        st.success(f"Đã load {len(phones)} số")
        st.dataframe(pd.DataFrame(phones[:50], columns=["SDT"]))

        if st.button("🚀 Bắt đầu gửi lời mời", type="primary"):
            st.info("Đang xử lý gửi lời mời... (Tính năng đang hoàn thiện)")

st.divider()
st.info("💡 Hướng dẫn: Mở chat.zalo.me → Login → Copy cookies → Dán vào sidebar")
st.caption("Phiên bản test - Contact dev để thêm gửi lời mời thực tế")
