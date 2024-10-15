import streamlit as st
import cv2

def find_working_camera():
    for i in range(10):  # Check first 10 indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            return i
    return None

def main():
    st.title("Webcam Feed")

    camera_index = find_working_camera()

    if camera_index is None:
        st.error("No working camera found. Please check the following:")
        st.write("1. Ensure your webcam is properly connected.")
        st.write("2. Check if any other application is using the webcam.")
        st.write("3. Restart your computer and try again.")
        st.write("4. If the problem persists, try a different USB port or webcam.")
        return

    # Create a VideoCapture object with the working index
    cap = cv2.VideoCapture(camera_index)

    # Streamlit image placeholder
    image_placeholder = st.empty()

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if ret:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Display the frame in the Streamlit app
                image_placeholder.image(frame, channels="RGB")
            else:
                st.warning("Failed to capture frame from webcam")
                break
    finally:
        # Release the VideoCapture object
        cap.release()

if __name__ == "__main__":
    main()
