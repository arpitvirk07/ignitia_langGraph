import streamlit as st
from graph import ignitia_graph

st.title("🌙 Ignitia — Startup Blueprint Generator")
idea = st.text_area("Enter your startup idea:")

if st.button("Generate"):
    if idea.strip():
        result = ignitia_graph.invoke({"idea": idea})

        st.subheader("🧠 Core Idea")
        st.write(result["concept"])

        st.subheader("📊 Market Analysis")
        st.write(result["analysis"])

        st.subheader("🎨 Branding Strategy")
        st.write(result["branding"])

    else:
        st.warning("Please enter an idea first.")
