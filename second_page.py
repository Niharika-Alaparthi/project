
import streamlit as st
#from database import authenticate_user
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
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        #height: 100vh;
        position: absolute;
        top: 100%;                /* Move the container to the center vertically */
        left: 150%;               /* Move the container to the center horizontally */
        transform: translate(-50%, -50%);
    }

    /* Login Card */
    .login-card {
        background: #fff;
        padding: 5rem;
        border-radius: 18px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0);
        width: 900px;
        text-align: center;
    }

    /* Input fields */
    .login-card input {
        width: 100%;
        padding: 0.8rem;
        margin: 0.8rem 0;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    /* Login Button */
    .login-button {
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        border: none;
        color: white;
        padding: 0.8rem 1.5rem;
        margin-top: 1rem;
        font-size: 16px;
        border-radius: 4px;
        cursor: pointer;
        transition: 0.3s ease;
    }

    .login-button:hover {
        background: linear-gradient(90deg, #2575fc, #6a11cb);
    }

    /* Signup link */
    .signup-text {
        margin-top: 1rem;
        font-size: 14px;
        color: #666;
    }

    .signup-text a {
        color: #2575fc;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the page
#st.markdown("<h1 style='text-align: center;'>Narrative QA & Summarization</h1>", unsafe_allow_html=True)



# Container for the login page content

st.markdown('<div class="login-container">', unsafe_allow_html=True)

    # Login Card content
st.markdown(
    """
    <div class="login-card">
        <h2>Login</h2>
        <form>
            <input type="text" placeholder="Enter your email" required>
            <input type="password" placeholder="Enter your password" required>
            <button class="login-button">Login</button>
        </form>
        <div class="signup-text">
            Don't have an account? <a href="#">Sign up</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

    # Close the login-container div
st.markdown('</div>', unsafe_allow_html=True)


