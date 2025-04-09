# Face Recognition Advance Attendance System

This project is a face recognition-based attendance system developed using Python and Streamlit. It provides an efficient and automated way to mark attendance by recognizing individuals' faces in real-time.

## Purpose

The purpose of this project is to simplify the attendance tracking process by leveraging face recognition technology. It eliminates the need for manual attendance marking, reduces human error, and provides a more efficient and accurate attendance management system.
## Features

- Mark attendance by recognizing faces in real-time
- Register new users by uploading their images
- View the attendance sheet with date and time details
- User-friendly web interface built with Streamlit
- Easy setup and usage

## Face Recognition Model

The Face Recognition Advance Attendance System utilizes the face_recognition model, which is based on deep learning algorithms and has been trained on a large dataset of facial images. This model is responsible for accurately recognizing and identifying faces in real-time.

The face_recognition model is a Python library that can be used to recognize faces in images and videos. It is based on the dlib face recognition library, which uses deep learning to extract features from faces. The face_recognition model is easy to use and can be integrated into a variety of applications.

### How It Works

The face_recognition model works by first detecting faces in an image or video. This is done using a face detector, which is a machine learning algorithm that is trained to identify faces in images. Once the faces have been detected, the model then extracts features from each face. These features are used to create a face encoding for each face. The face encoding is a unique identifier for each face, and it can be used to compare faces to each other.

The face_recognition model uses a deep learning algorithm to extract features from faces. Deep learning is a type of machine learning that uses artificial neural networks to learn from data. The deep learning algorithm in the face_recognition model is trained on a large dataset of images of faces. This dataset includes images of faces from a variety of angles, with different expressions, and in different lighting conditions.

Once the face encodings have been created, they can be compared to each other using the compare_faces() method. This method will return a list of boolean values indicating whether or not each face in the first image matches a face in the second image. The tolerance parameter can be used to adjust the sensitivity of the comparison. A higher tolerance value will result in more matches, while a lower tolerance value will result in fewer matches.

The face_recognition model is a powerful tool for face recognition. It is easy to use, open source, and highly accurate. However, it can be slow on large datasets and is not as accurate as some other face recognition models.

Here are some of the steps involved in how the face_recognition model works:

1. Face detection: The first step is to detect faces in an image or video. This is done using a face detector, which is a machine learning algorithm that is trained to identify faces in images.
2. Feature extraction: Once the faces have been detected, the model then extracts features from each face. These features are used to create a face encoding for each face.
3. Face encoding: The face encoding is a unique identifier for each face. It is a vector of numbers that represents the important features of a face.
4. Face comparison: The face encodings can be compared to each other using the compare_faces() method. This method will return a list of boolean values indicating whether or not each face in the first image matches a face in the second image.

### Basic Usage

The basic usage of the face_recognition model is to create a face encoding for each face in an image or video. This can be done using the face_encodings() method. Once the face encodings have been created, they can be compared to each other using the compare_faces() method. This method will return a list of boolean values indicating whether or not each face in the first image matches a face in the second image.

### Advanced Usage

The face_recognition model also provides a number of advanced features, such as the ability to:

- Identify faces in real time
- Track faces over time
- Detect faces that are wearing sunglasses or hats
- Recognize faces even if they are partially obscured

### Features and Capabilities
- Accurate face recognition: The model can accurately identify individuals by comparing face encodings.
- Real-time processing: It can process video streams or images in real-time, allowing for quick face recognition.
- Robustness to variations: The model can handle variations in lighting, pose, and facial expressions, ensuring reliable face recognition under different conditions.

### Limitations
While the face_recognition model is highly effective, it is important to note its limitations:

- Occlusions: Heavy occlusions, such as wearing sunglasses or face masks, may affect the accuracy of face recognition.
- Image quality: Low-resolution or blurry images might result in lower recognition accuracy.
- Training data bias: The model's performance may vary depending on the diversity of the training dataset.

It's essential to consider these limitations and optimize the system's usage accordingly.

### Alternatives

There are a number of other face recognition models available, including:

* OpenCV
* TensorFlow
* PyTorch

These models offer a variety of features and capabilities, so it is important to choose the one that is best suited for your specific needs.


## Getting Started
To run this project on your local system, please ensure you have the following prerequisites:

### Prerequisites
- Python (version 3.7 or higher)
- Anaconda (recommended for managing Python environments)
- Git (optional, for cloning the project repository)

### Run Locally

1. Clone the project repository to your local machine using the following command:

```bash
  git clone https://github.com/Pranav-Programmer/Face-Recognition-Advance-Attendance-System
```
2. Open Visual Studio Code or any other Python IDE of your choice.

3. Set up the Python environment for the project using Anaconda or your preferred method.

4. Install the required dependencies by running the following command in the terminal:

```bash
  pip install -r requirements.txt
```

5. Launch the application by running the following command in the terminal:

```bash
  streamlit run Attendance_System.py
```

6. Open your web browser and go to the provided local URL to access the application.


## How to Use the Face Recognition Advance Attendance System

Welcome to the Face Recognition Advance Attendance System! This guide will walk you through the steps to use this system effectively for marking attendance.

### Prerequisites
Before getting started, make sure you have the following:

- A computer with a webcam
- An internet connection
- Google Chrome or any other modern web browser installed

### Step 1: Access the System

1. Open your web browser and enter the URL provided by the system administrator.

2. The system homepage will be displayed, showing the menu options on the sidebar.

>![A1](https://user-images.githubusercontent.com/79044490/194722506-7c676ba1-8d40-467f-bba4-2db21e9332de.png)

### Step 2: Register Yourself

Without registration the system will not recognize you.

![A3](https://user-images.githubusercontent.com/79044490/194722566-dd276a5a-7c82-45d7-97dd-687259213e00.png)

1. Click on the "REGISTER" option in the sidebar menu.

2. You will be directed to the registration page.

3. Click on the "Choose File" button and select an image of yourself. Make sure the image has a clear and visible face.

4. Once the image is selected, click on the "Upload" button to upload your image for registration.

5. Wait for the system to process the image and confirm the registration.

![A4](https://user-images.githubusercontent.com/79044490/194722583-1f1c2181-f1af-48f4-ae66-a9f1c0adae39.png)

### Step 3: Mark Your Attendance
1. Click on the "MARK ATTENDANCE" option in the sidebar menu.

2. You will see a checkbox labeled "MARK YOUR PRESENCE." Check this checkbox to enable attendance marking.

3. The system will access your webcam and start detecting your face.

4. Position yourself in front of the webcam, ensuring your face is clearly visible.

5. The system will recognize your face and display your name on the screen, indicating successful attendance marking.

6. Wait for a few seconds to allow the system to complete the attendance marking process.

7. Once the attendance is marked, you can close the webcam window.

![A2](https://user-images.githubusercontent.com/79044490/194722538-0c93231f-8284-41d4-adaa-7b7ebcace883.png)

### Step 4: View Attendance Sheet
1. Click on the "ATTENDANCE SHEET" option in the sidebar menu.

2. The attendance sheet will be displayed, showing the names and timestamps of individuals' attendance.

3. You can view the attendance sheet for your reference.

![A5](https://user-images.githubusercontent.com/79044490/194722590-08611b50-af90-4bd0-8607-d6a3df330ff8.png)

Congratulations! You have successfully used the Face Recognition Advance Attendance System to register yourself and mark your attendance. Repeat the process whenever you need to mark your attendance in the future.
