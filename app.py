import streamlit as st

st.set_page_config(
    page_title="Ruiqing Wang",
    page_icon="👩🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![]('eileen.jpg')
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.image('eileen.jpg')
    
with col2:
    st.markdown(
        """
    # Hi, I'm Ruiqing Wang
    I am an HCI researcher, currently pursuing my Master’s degree in Data Science and Information Technology at GIX. Drawing inspiration from Artificial Intelligence and Mixed Reality, I designed a collaborative system that seamlessly integrates the virtual and the real world and proposed AI models to facilitate interactions between humans and devices, aiming to enhance health and overall well-being.
                 
    - My homepage [🌍 ruiqing.ai](https://ruiqing.ai)
    - Bellevue, Washington, US
    """
    )

st.markdown(
    """
# Education

- [2023-2025 University of Washington]
- [2022-2023 Tsinghua University]
"""
)

st.markdown(
    """
# Work Experience

- [2022 Information Department in Fuyao Group]
- [2021 The Future Laboratory in Tsinghua University]
"""
)

st.markdown(
    """
# Skills

- [Design Tools: Solidworks, Rhino, Fusion 360, KeyShot, UE5, Unity, KiCad, AutoCAD, Figma, Ai, Ps, Pr]
- [Programming Tools: Python, C/C++, Arduino, Platform IO, PyTorch, MATLAB, SPSS]
"""
)

st.markdown(
    """
# Interesting Projects

- [FlexiGrow: LLM GPT4-based Intelligent Deformable Plant Pet](https://ruiqing.ai/blog/flexigrow/)
- [Intelligent Frit Pattern Industrial Design Software for Vehicle Glass](https://ruiqing.ai/blog/fritpattern/)
- [GymBand: Adaptive Music Recommendation for Heathier Fitness](https://ruiqing.ai/blog/gymband/)
"""
)
