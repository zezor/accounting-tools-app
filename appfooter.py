import streamlit as st
def app_footer():
    st.markdown("""
        <hr style="border-top: 1px solid #bbb;">
        <div style="text-align: center; font-size: 14px; color: gray;">
            Developed by <strong>Kemma Solutions</strong><br>
            📧 <a href="mailto:kemma@example.com" style="color: gray;">kemma@example.com</a><br>
            🔗 <a href="https://www.linkedin.com/company/kemma-solutions" target="_blank" style="color: gray;">LinkedIn</a> | 
            <a href="https://twitter.com/kemma_solutions" target="_blank" style="color: gray;">Twitter</a><br><br>
            &copy; 2025 All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)
app_footer()