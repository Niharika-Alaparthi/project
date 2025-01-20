
import streamlit as st

st.set_page_config(page_title="Narrative QA and Summarization",page_icon='📚',layout='wide',initial_sidebar_state='collapsed')
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
        background: url("https://images.unsplash.com/photo-1491841550275-ad7854e35ca6?q=80&w=3474&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D") no-repeat center center fixed;
        background-size: cover;
    }

    /* A "hero-container" to vertically & horizontally align items */
    .hero-container {
        #min-height: 100vh;      /* full viewport height */
        display: flex;
        flex-direction: column; /* stack elements vertically */
        justify-content: center;/* center vertically */
        align-items: flex-end;  /* push content to the right */
        text-align: center;      /* right-align text inside */
        background-color: rgba(0, 0, 0, 0); /* dark overlay for readability */
        padding-top:100px;
        padding-right: 50px;    /* add spacing from right edge */
        box-sizing: border-box;
    }

    /* Typewriter heading (31 characters total) */
    .typewriter {
        color: #262730;
        font-weight: bold;
        font-size: 48px;
        margin: 0 0 5px 0;     /* bottom margin for spacing, no top margin */
        white-space: nowrap;    /* keep text on a single line */
        border-right: 4px solid ; #262730/* blinking cursor color  #ff69b4*/
        box-sizing: border-box;
        
        /* We animate from 0 to 31 characters wide (matching the heading text length).
        steps(31, end) to animate exactly 31 steps (one per character). */
        width: 0ch;
        overflow: hidden;
        animation:
            typing 3s steps(31, end) forwards,
            blink-caret 0.75s step-end infinite;
    }

    /* Keyframes for "typing" effect: from 0ch width to 31ch */
    @keyframes typing {
    from { width: 0ch; }
    to   { width: 31ch; }
    }

    /* Keyframes for blinking cursor */
    @keyframes blink-caret {
    50% { border-color: transparent; }
    }

    /* Subtext: smaller than heading */
    .subtext {
        font-size: 25px;
        color: #0a0a0a;
        margin: 0 0 5px 0; /* spacing below */
    }

    /* Button row horizontally */
    .button-row {
        display: inline-flex;
        gap: 20px;
        margin-right: 40px;
        margin-bottom: 5px; /* a bit of bottom spacing */
    }

    /* Button styles */
    .btn {
        text-decoration: none;
        background-color: #0a0a0a;
        color: #000;
        border: 1px solid #ccc;
        padding: 0.6em 1.2em;
        border-radius: 4px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-family: sans-serif;
    }
    .btn:hover {
        background-color: #0a0a0a;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero-container">
        <!-- Typewriter heading (31 characters) -->
        <div class="typewriter">Narrative QA and Summarization</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtext section
st.markdown(
    """
    <div class="hero-container">
    <div class="subtext">
        Discover the power of AI to summarize narratives and answer your questions efficiently. 
        
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons section
st.markdown(
    """
    <div class="hero-container">
    <div class="button-row">
        <a class="btn" href="#">Login</a>
        <a class="btn" href="#">Sign Up</a>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

