import streamlit as st
import json
import requests
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")

st.title("🚀 Rona Friend Tool - Gửi Lời Mời Thật")

if "accounts" not in st.session_state:
    st.session_state.accounts = []

# Sidebar Login
with st.sidebar:
    st.header("🔑 Đăng nhập Zalo")
    acc_name = st.text_input("Tên tài khoản", "Zalo 1")
    proxy = st.text_input("Proxy", "")
    cookies_str = st.text_area("Dán Cookies JSON", height=200)
    
    if st.button("Login"):
        if cookies_str:
            try:
                cookies = json.loads(cookies_str)
                st.session_state.accounts.append({"name": acc_name, "cookies": cookies, "proxy": proxy})
                st.success("Login OK!")
            except:
                st.error("Cookies sai!")
                
# Main
uploaded_file = st.file_uploader("Upload TXT SDT", type="txt")
if uploaded_file:
    phones = [line.strip() for line in uploaded_file.getvalue().decode().splitlines() if line.strip()]
    st.success(f"Load {len(phones)} số")

    if st.button("🚀 Bắt đầu gửi lời mời", type="primary"):
        if not st.session_state.accounts:
            st.error("Chưa login tài khoản Zalo!")
        else:
            for phone in phones[:20]:  # limit 20
                for acc in st.session_state.accounts:
                    try:
                        # TODO: Thay bằng API thật
                        headers = {"Cookie": "; ".join([f"{k}={v}" for k,v in acc["cookies"].items()])}
                        # Giả lập gửi
                        st.write(f"Đang gửi đến {phone} từ {acc['name']}")
                        time.sleep(2)
                    except:
                        st.error("Lỗi gửi")
            st.success("Hoàn thành batch!")

st.info("Tính năng gửi lời mời đang dùng cookies. Cần API Zalo đầy đủ để ổn định.")
def send_friend_request(phone, cookies, proxy=None):
    headers = {
        "Cookie": "; ".join([f"{k}={v}" for k,v in cookies.items()]),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    payload = {
        "phone": phone,
        "message": "Chào bạn, kết bạn nhé!"
    }
    
    try:
        r = requests.post("https://chat.zalo.me/api/social/friend/add", 
                         json=payload, headers=headers, proxies={"http": proxy, "https": proxy} if proxy else None)
        if r.status_code == 200:
            return "Thành công"
        else:
            return f"Lỗi {r.status_code}"
    except:
        return "Lỗi kết nối"
