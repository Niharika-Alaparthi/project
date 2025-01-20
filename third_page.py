import streamlit as st

#st.set_page_config(page_title="Narrative QA and Summarization",page_icon='📚',layout='wide',initial_sidebar_state='collapsed')
#st.write("hello")

st.markdown(
    """
    <style>

    /* Hide Streamlit header & footer */
    header, footer {visibility: hidden;}

    /* Remove default padding/margin around main container */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Full-page background on .stApp to override Streamlit's default gray */
    .stApp {
        background: url("https://plus.unsplash.com/premium_photo-1701678180518-fa0c2ed2eb58?q=80&w=3432&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D") no-repeat center center fixed;
        background-size: cover;
    }
    /* Center alignment */
    .signup-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-left: 10px;
        #height: 100vh;
        #background-color: #fbd1d1; /* Light pink background */
    }

    /* Signup Card */
    .signup-card {
        background: #fff;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        width: 300px;
        text-align: center;
    }

    /* Input fields */
    .signup-card input {
        width: 100%;
        padding: 0.8rem;
        margin: 0.8rem 0;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    /* Signup Button */
    .signup-button {
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
        border: none;
        color: white;
        padding: 0.8rem 1.5rem;
        margin-top: 1rem;
        font-size: 16px;
        border-radius: 4px;
        cursor: pointer;
        transition: 0.3s ease;
    }

    .signup-button:hover {
        background: linear-gradient(90deg, #ff7eb3, #ff758c);
    }

    /* Login link */
    .login-text {
        margin-top: 1rem;
        font-size: 14px;
        color: #666;
    }

    .login-text a {
        color: #ff758c;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="signup-container">', unsafe_allow_html=True)   
    

st.markdown('<div class="signup-card">', unsafe_allow_html=True)

    # Username Field
username = st.text_input('Username', key="username")
st.markdown('<div class="username-field"></div>', unsafe_allow_html=True)

    # Email Field
email = st.text_input('Email', key="email")
st.markdown('<div class="email-field"></div>', unsafe_allow_html=True)

    # Date of Birth (without calendar)
dob = st.text_input('Date of Birth (DD/MM/YYYY)', key="dob")
st.markdown('<div class="dob-field"></div>', unsafe_allow_html=True)

    # Password Field
password = st.text_input('Password', type="password", key="password")
st.markdown('<div class="password-field"></div>', unsafe_allow_html=True)

    # Confirm Password Field
confirm_password = st.text_input('Confirm Password', type="password", key="confirm_password")
st.markdown('<div class="confirm-password-field"></div>', unsafe_allow_html=True)

    # Signup Button
if st.button('Sign Up', key="signup"):
        # Add functionality for handling sign-up here
    st.success("Signup Successful!")
    
    # Login Link
st.markdown('<div class="login-text">Already have an account? <a href="#">Login</a></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

