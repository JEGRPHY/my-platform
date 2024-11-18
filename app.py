import streamlit as st

# Title and Header with Space Theme
st.markdown(
    """
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #1c1c1c !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">Cosmology Learning Portal 🌌</div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔭 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Cosmic Documents", "Simulations", "Space Videos"]
)

# Background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.nasa.gov/sites/default/files/thumbnails/image/stsci-h-p2001a-m-2000x1500_0.png');
        background-size: cover;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page
if page == "Home":
    st.subheader("Welcome to the Universe of Learning")
    st.write("""
        Explore the mysteries of the cosmos! This portal offers resources, simulations, 
        and videos to guide your journey into the universe.
    """)
    st.image(
        "https://cdn.pixabay.com/photo/2013/07/18/20/25/galaxy-164097_960_720.jpg",
        caption="The Vast Universe Awaits",
        use_column_width=True,
    )

# Cosmic Documents Page
elif page == "Cosmic Documents":
    st.subheader("🌌 Cosmic Documents")
    uploaded_files = st.file_uploader("Upload cosmic files to share:", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            st.write(f"Uploaded: {file.name}")
            st.download_button(label="Download", data=file, file_name=file.name)

    st.write("## Shared Documents:")
    st.markdown("[Astronomy Lecture Notes (PDF)](https://example.com/astronomy-notes)")
    st.markdown("[Star Chart (PDF)](https://example.com/star-chart)")

# Simulations Page
elif page == "Simulations":
    st.subheader("🚀 Explore the Universe with Simulations")
    st.write("### Simulation 1: Gravity and Orbital Motion")
    st.markdown("[Open Simulation](https://example.com/gravity-simulation)")

    st.write("### Simulation 2: Black Hole Explorer")
    st.markdown("[Open Simulation](https://example.com/black-hole-simulation)")

    st.image(
        "https://cdn.pixabay.com/photo/2014/09/07/22/36/black-hole-438428_960_720.jpg",
        caption="Simulate and Learn",
        use_column_width=True,
    )

# Space Videos Page
elif page == "Space Videos":
    st.subheader("🌠 Space Exploration Videos")
    st.video("https://www.youtube.com/watch?v=GO5FwsblpT8")  # Replace with a relevant link
    st.video("https://www.youtube.com/watch?v=9zA-rZQB-xk")  # Replace with another link

    st.write("### More Cosmic Videos:")
    st.markdown("- [Hubble Telescope Journey](https://www.youtube.com/watch?v=GO5FwsblpT8)")
    st.markdown("- [The Scale of the Universe](https://www.youtube.com/watch?v=9zA-rZQB-xk)")

# Footer
st.sidebar.info("🚀 Created by Your Name - Exploring the Cosmos")
