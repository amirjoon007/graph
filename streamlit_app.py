import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# تنظیمات صفحه
st.set_page_config(page_title="G(Z_n) Graph Visualizer", layout="centered")

# عنوان و توضیحات برنامه
st.title("Graph Visualizer for G(Z_n)")
st.write("این برنامه گرافی از G(Z_n) را بر اساس شرط ضربی نمایش می‌دهد. عدد n را وارد کنید تا گراف مربوطه ساخته شود.")

# ورودی کاربر برای n
n = st.number_input("مقدار n را وارد کنید:", min_value=1, step=1, format="%d")

# دکمه رسم گراف
if st.button("رسم گراف"):
    # ایجاد گراف G(Z_n)
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    
    # افزودن یال‌ها طبق شرط a * b ≡ 0 (mod n)
    for a, b in combinations(nodes, 2):
        if (a * b) % n == 0:
            G.add_edge(a, b)
    
    # رسم گراف با چیدمان دایره‌ای
    pos = nx.circular_layout(G)
    node_colors = ["#FFD700" if node % 2 == 0 else "#FF6347" for node in G.nodes]
    
    # نمایش گراف
    fig, ax = plt.subplots(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, edge_color="#4682B4", font_weight="bold", ax=ax)
    plt.title(f"G(Z_{n}) with Enhanced Graphics", fontsize=15, color="#333333", pad=20)
    plt.axis("off")
    st.pyplot(fig)
