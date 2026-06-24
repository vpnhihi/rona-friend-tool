import streamlit as st
import pandas as pd
import json
from datetime import datetime

st.set_page_config(page_title="Rona Friend Tool", layout="wide")
st.title("🚀 Rona Friend Tool - Tự động kết bạn Zalo")

# Sidebar - Quản lý tài khoản
with st.sidebar:
    st.header("📱 Quản lý Tài khoản Zalo")
    if st.button("Thêm tài khoản mới"):
        st.session_state.accounts.append({"name": "Zalo Account " + str(len(st.session_state.accounts)+1), "proxy": "", "status": "Chưa login"})
    
    accounts = st.session_state.get("accounts", [])
    for i, acc in enumerate(accounts):
        with st.expander(acc["name"]):
            proxy = st.text_input("Proxy[](http://user:pass@ip:port)", value=acc.get("proxy", ""), key=f"proxy_{i}")
            if st.button("Login Zalo", key=f"login_{i}"):
                st.success(f"Đăng nhập {acc['name']} thành công (test)")

# Main
tab1, tab2 = st.tabs(["Kết bạn từ SDT", "Quản lý"])

with tab1:
    st.subheader("Upload danh sách SDT (TXT)")
    uploaded = st.file_uploader("Chọn file TXT (mỗi dòng 1 số)", type="txt")
    
    if uploaded:
        phones = [line.strip() for line in uploaded.getvalue().decode().splitlines() if line.strip()]
        st.success(f"Đã load {len(phones)} số điện thoại")
        st.dataframe(pd.DataFrame(phones, columns=["SDT"]))
        
        if st.button("🚀 Bắt đầu gửi lời mời", type="primary"):
            st.info("Đang xử lý... (Tính năng gửi lời mời đang phát triển)")
            # TODO: Gọi hàm gửi lời mời

with tab2:
    st.write("Log hoạt động sẽ hiển thị ở đây")

# Khởi tạo session
if "accounts" not in st.session_state:
    st.session_state.accounts = []

st.caption("Phiên bản test - Liên hệ dev để bổ sung đầy đủ chức năng gửi lời mời & multi proxy")
