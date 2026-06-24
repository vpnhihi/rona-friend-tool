import streamlit as st
import json
import time
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn Zalo")

if "accounts" not in st.session_state:
    st.session_state.accounts = []

# Login Tab
st.header("🔑 Đăng nhập Zalo")
acc_name = st.text_input("Tên tài khoản", "Zalo Account 1")
cookies_str = st.text_area("Dán Cookies JSON từ chat.zalo.me", height=200)

if st.button("✅ Login Zalo", type="primary"):
    if cookies_str.strip():
        try:
            cookies = json.loads(cookies_str)
            st.session_state.accounts.append({
                "name": acc_name,
                "cookies": cookies,
                "status": "✅ Đã login"
            })
            st.success("Login thành công!")
        except:
            st.error("Cookies sai format!")
    else:
        st.warning("Vui lòng dán cookies")

# Kết bạn Tab
st.header("📤 Kết bạn từ SDT")
uploaded_file = st.file_uploader("Upload file TXT SDT (mỗi dòng 1 số)", type="txt", key="uploader1")

if uploaded_file:
    phones = [line.strip() for line in uploaded_file.getvalue().decode().splitlines() if line.strip()]
    st.success(f"Đã load {len(phones)} số điện thoại")
    st.dataframe(phones[:20], use_container_width=True)

    if st.button("🚀 Bắt đầu gửi lời mời", type="primary"):
        if st.session_state.accounts:
            st.info("Đang gửi lời mời bằng cookies...")
            for phone in phones[:20]:
                st.write(f"Đang gửi đến {phone}...")
                time.sleep(1)
            st.success("Hoàn thành batch!")
        else:
            st.error("Chưa có tài khoản Zalo nào!")

st.sidebar.write(f"**Tài khoản đã login**: {len(st.session_state.accounts)}")
st.caption("Tool test - Dùng cookies để login")
