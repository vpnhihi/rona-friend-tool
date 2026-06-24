with st.sidebar:
    st.header("📱 Đăng nhập Zalo Thật")
    
    acc_name = st.text_input("Tên tài khoản", value="Zalo Account 1")
    proxy = st.text_input("Proxy (tùy chọn)", placeholder="http://user:pass@ip:port")
    
    cookies_input = st.text_area("Dán Cookies từ chat.zalo.me (JSON format)", height=150)
    
    if st.button("✅ Login Zalo", type="primary"):
        if cookies_input:
            try:
                cookies = json.loads(cookies_input)
                st.success(f"Đăng nhập {acc_name} thành công!")
                st.session_state.accounts.append({
                    "name": acc_name,
                    "cookies": cookies,
                    "proxy": proxy,
                    "status": "Đã login"
                })
            except:
                st.error("Cookies không đúng format JSON")
        else:
            st.warning("Vui lòng dán cookies")
