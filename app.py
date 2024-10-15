import streamlit as st
import cv2

def main():
    st.title("Webcam Feed")

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Streamlit image placeholder
    image_placeholder = st.empty()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame in the Streamlit app
            image_placeholder.image(frame, channels="RGB")
        else:
            st.error("Failed to capture frame from webcam")
            break

    # Release the VideoCapture object
    cap.release()

if __name__ == "__main__":
    main()
