# Face Recognition Attendance System
A simple Flask-based web application to take attendance using face recognition. This system uses a webcam to detect and recognize faces in real-time, marking the attendance of registered students. The model is trained using images captured from the webcam, and the attendance data is saved in CSV files.

##Features
Face Recognition: Uses a webcam to detect and recognize faces from a list of registered users.
Attendance Tracking: Automatically marks attendance for recognized faces.
New User Registration: Allows adding new users by capturing their face images and training the recognition model.
Daily Attendance CSV: Attendance is saved in a CSV file, named with the current date, to track the attendance history.
Model Training: The system uses a K-Nearest Neighbors (KNN) classifier to recognize faces based on previously captured images.

##Install Dependencies
You can install the required Python packages using pip:
pip install -r requirements.txt

## Setup Instructions

1. Clone or Download the Repository
If you haven't already, clone or download the project repository to your local machine.

git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system

2. Place Haar Cascade Classifier
Ensure that the haarcascade_frontalface_default.xml file is available in the static directory. You can download it from the official OpenCV repository.

Download the file from: Haar Cascade Classifier
Place the file in the static/ folder of your project directory.

3. Directory Structure
Ensure that your project directory has the following structure:

/face-recognition-attendance-system
├── /static
│   ├── /faces            # Directory to store captured face images
│   ├── haarcascade_frontalface_default.xml  # Haar Cascade XML file
│   └── face_recognition_model.pkl  # Trained face recognition model (generated after training)
├── /Attendance           # Directory to store attendance CSV files
├── app.py                 # Main Flask app
├── /templates
│   └── home.html         # HTML template for the web interface
└── README.md             # This readme file

4. Add New Users (Initial Setup)
Before starting attendance tracking, you'll need to add new users. To do this:

Open the app in your browser (http://localhost:5000).
Click on the Add User button.
Enter the user's name and roll number.
The system will open the webcam and start capturing the user's face images.
It will capture 50 images and save them in the static/faces/ folder under a directory named with the user's name and roll number.
After image capture is complete, the system will train the model to recognize this user.
5. Train the Model
Once at least one user is added, the system will train a KNN model using the captured images. The model is saved in the static/face_recognition_model.pkl file, which will be used for real-time face recognition during attendance tracking.

##Usage Instructions
1. Start the Flask App
To start the Flask server and run the application, use the following command in your terminal:

bash
Copy code
python app.py
This will launch the app on http://localhost:5000/.

2. Web Interface
The web interface provides the following functionalities:

Home Page: Displays the attendance record for the current day, including the names, roll numbers, and times of students who have marked attendance.
Take Attendance: When you click on "Start Attendance," the system will begin capturing faces via the webcam, recognize registered users, and mark their attendance in the CSV file.
Add New User: This page allows you to add new users to the system by capturing their face images and training the model.
3. View Attendance
On the home page, you can see the list of names, roll numbers, and the time at which attendance was marked for each student.

4. Attendance File
Each day’s attendance is saved in a CSV file in the Attendance/ folder, with the filename format Attendance-MM_DD_YY.csv. The file includes the following columns:

Name: The name of the student.
Roll: The student's roll number.
Time: The time when the student's attendance was marked.
5. Model Updates
If you add a new user, the model will be retrained using the new face images. The updated model is saved as face_recognition_model.pkl in the static/ folder.

6. Stop the Application
To stop the Flask application, simply press Ctrl+C in your terminal.

**Additional Terms:**
This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
