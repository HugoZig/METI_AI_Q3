import streamlit as st
import numpy as np

# --- PAGE CONFIGURATION ---
# It's a good practice to set the page configuration as the first Streamlit command.
st.set_page_config(
    page_title="Handwritten Image Generator",
    layout="centered" # or "wide"
)

# --- UI STYLING (CSS) ---
# Inject custom CSS to set a blank (white) background and ensure text is black.
st.markdown("""
<style>
    /* This targets the main container of the Streamlit app */
    .stApp {
        background-color: #FFFFFF; /* Set background to white */
    }
</style>
""", unsafe_allow_html=True)


# --- HEADER ---
# Use markdown with inline CSS for a black title.
st.markdown('<h1 style="color: black;">Handwritten Image Generator</h1>', unsafe_allow_html=True)

# --- DESCRIPTION ---
st.markdown('<p style="color: black;">Generate syntetic MNIST-like images using your trained model.</p>', unsafe_allow_html=True)

# --- USER INPUT ---
# Create a select box for the user to choose a digit.
# The options are a list of integers from 0 to 9.
digit_to_generate = st.selectbox(
    label="Chose a digit to generate (0-9):",
    options=list(range(10))
)


# --- GENERATE BUTTON AND LOGIC ---
# Create a button that the user will click to start the generation.
if st.button("Generate images"):
    # This block of code runs when the button is clicked.

    st.write(f"Generating a new image for the digit: **{digit_to_generate}**")

    # --- MODEL INFERENCE PLACEHOLDER ---
    # In a real application, you would put your model loading and
    # image generation code here.
    # For demonstration, we will create a simple placeholder image.

    with st.spinner('Generating...'):
        # Placeholder for a generated image (e.g., a 28x28 numpy array)
        # Replace this with your actual model's output
        placeholder_image = np.zeros((28, 28), dtype=np.uint8)
        # A real image would be a grayscale numpy array from 0 to 255.

        # Display the generated image.
        st.image(
            placeholder_image,
            caption=f"Synthetically generated image for digit {digit_to_generate}",
            width=200 # Control the display width of the image
        )

    st.success("Image generated successfully!")