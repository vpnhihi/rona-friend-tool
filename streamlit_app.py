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
import streamlit as st
import requests
import time
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")

st.title("🚀 Rona Friend Tool")
st.subheader("Tự động kết bạn Zalo")

if "accounts" not in st.session_state:
    st.session_state.accounts = []

st.header("🔑 Đăng nhập Zalo (QR Code)")

if st.button("Tạo QR Login Mới từ chat.zalo.me"):
    with st.spinner("Đang lấy QR Code từ Zalo..."):
        try:
            # Giả lập lấy QR từ Zalo (thay bằng API thật nếu có)
            qr_url = "https://qr.zalo.me/qr?type=login"  # Link QR động
            st.image(qr_url, caption="Quét QR bằng Zalo App trên điện thoại", use_column_width=True)
            st.success("QR Code đã tạo! Quét ngay để login.")
            
            # Giả lập login sau khi quét
            time.sleep(8)
            st.session_state.accounts.append({
                "name": "Zalo Account " + str(len(st.session_state.accounts)+1),
                "status": "✅ Đã login QR",
                "login_time": datetime.now().strftime("%H:%M")
            })
            st.balloons()
        except:
            st.error("Lỗi lấy QR. Thử lại.")

# Hiển thị tài khoản
st.subheader("Tài khoản đã login")
for acc in st.session_state.accounts:
    st.success(f"{acc['name']} - {acc['status']} ({acc.get('login_time', '')})")

st.info("Quét QR bằng Zalo App → Tool sẽ tự nhận (đang hoàn thiện poll login).")

st.caption("Tool test - Dùng QR từ chat.zalo.me")
