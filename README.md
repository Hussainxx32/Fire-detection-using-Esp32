# Fire-detection-using-ESP32
This project presents a fire detection system usning ESP32 and a flame sensor, combined with signal processing and machine learning techniques to improve detection accuracy.
# Project Overview
The system works in three main stages:

1- Data Acquisition
- Flame sensor readings are collected using ESP32
- Real fire is represented using a stable flame source (candle)
2- Signal Processing
- Sensor data is filtered using an FIR low-pass filter
- Features are extracted from the signal such as: Mean, Standard Deviation, RMS, Ratio
3- Machine Learning Classification
- A Random Forest classifier is trained using Python
- The model classifies flame conditions based on extracted features
- Achieved accuracy: 73.53%
# Technologies Used
- ESP32
- flame sensor
- Arduino IDE
- python
- signal processing
# Results
- The system successfully differentiates fire conditions using sensor data
- Machine learning improved detection compared to raw sensor readings
- Final model accuracy reached approximately 73.53%
# Limitations
- Dataset size is limited
- Data collected under controlled conditions only
# Future Improvements
- Increase window size for more stable feature extraction
- Collect more sensor readings per sample
- Add a temperature sensor (e.g., DS18B20) as an additional feature
- Deploy the trained model on ESP32 for real-time detection
- Implement real-time alerts and notificatons
# LinkedIn Link
[https://www.linkedin.com/in/hussain-almasabi-37315a244?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BtUEcboraSEeqhYdSOOl8bg%3D%3D]
