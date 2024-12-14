import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="My Python Website", page_icon="🌐")

# Homepage
st.title("🌟 Welcome to My Python Website!")
st.write("""
    This is a simple interactive website built with Streamlit.
    Explore the sections below to learn more about it!
""")

# Navigation Menu
menu = ["Home", "About", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Section
if choice == "Home":
    st.header("Home")
    st.write("""
        Welcome to the homepage! Here, you can find all the latest updates and features
        of this website. Enjoy exploring!
    """)

    st.subheader("Fun Facts")
    if st.button("Click Me!"):
        st.success("Streamlit is an awesome framework for building websites with Python!")

# About Section
elif choice == "About":
    st.header("About")
    st.write("""
        This website was created using Streamlit, a lightweight Python framework for building
        interactive and data-driven web applications.

        Features:
        - Interactive UI components
        - Simple to use and deploy
        - Great for Python developers
    """)

# Contact Section
elif choice == "Contact":
    st.header("Contact Me")
    st.write("Fill out the form below to get in touch!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Thank you, {name}! Your message has been received.")
