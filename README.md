# 👁️ Face Recognition System

A real-time face recognition application built with **Python**, **OpenCV**, and the dlib-based **face_recognition** library. This system automatically identifies individuals from a webcam feed by comparing them against a pre-defined database of images.

---
## 📸 Demo
Below is an example of the system in action, successfully identifying targets from the webcam feed:

| Example 1: Bill Gates 
| :---: 
| ![Bill Gates Detection](https://github.com/user-attachments/assets/b7bba4a0-7707-4d08-b366-421e92363f5a) 

---


## 🚀 Features

* **Real-time Recognition:** Captures video via webcam and identifies faces with low latency.
* **Automated Encoding:** Automatically loads and encodes all images stored in the database directory upon startup.
* **High Accuracy:** Utilizes `face_recognition` (state-of-the-art dlib models) to calculate face distances and identify the closest match.
* **Visual Feedback:** Draws bounding boxes around detected faces and labels them with their corresponding filenames in uppercase.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Libraries:**
    * **OpenCV:** Image processing and webcam handling.
    * **face_recognition:** Face detection and 128-dimension feature encoding.
    * **NumPy:** Efficient mathematical operations for distance calculation and array manipulation.
    * **OS:** File system management and directory traversal.
