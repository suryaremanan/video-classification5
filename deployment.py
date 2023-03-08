import streamlit as st
import tensorflow as tf
import requests
import urllib.parse

# Load the TensorFlow Lite model.
interpreter = tf.lite.Interpreter(model_path="/Users/apple/Downloads/new/new TFLite/saved_model.tflite")
interpreter.allocate_tensors()

# Define the input and output details.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define a function to classify a YouTube video.
def classify_video(video_url):
    # Extract the video ID from the URL.
    parsed_url = urllib.parse.urlparse(video_url)
    query_dict = urllib.parse.parse_qs(parsed_url.query)
    video_id = query_dict["v"][0]

    # Download the video thumbnail.
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    response = requests.get(thumbnail_url)
    image_data = response.content

    # Preprocess the image data.
    image = tf.image.decode_jpeg(image_data, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.expand_dims(image, 0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Run the model on the image.
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # Return the predicted class.
    class_index = tf.argmax(predictions[0]).numpy()
    class_names = ["news","sports","travel","entertainment","music"]  # Replace with your own class names
    return class_names[class_index]

# Define the Streamlit app.
def app():
    st.title("YouTube Video Classification")

    # Create a text input field for the YouTube video URL.
    video_url = st.text_input("Enter a YouTube video URL")

    # Create a button to run the classification model.
    if st.button("Classify"):
        # Call the classify_video function and display the result.
        result = classify_video(video_url)
        st.write("The predicted class is:", result)

# Run the Streamlit app.
if __name__ == "__main__":
    app()
