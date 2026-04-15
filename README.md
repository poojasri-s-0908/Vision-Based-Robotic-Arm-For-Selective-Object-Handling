# Vision-Based Robotic Waste Sorting System

## Overview
A modular robotic system for detecting and sorting waste using computer vision and a 3-DOF robotic arm.

## System Architecture
ESP32-CAM → WiFi → YOLOv8 (Python) → Detection → User Trigger → ESP8266 → Robotic Arm

## Features
- Real-time waste detection (paper, plastic)
- Custom-trained YOLOv8 model
- 3-DOF robotic arm with parallel gripper
- Smooth servo control using PCA9685
- Python GUI-based control system

## Hardware
- ESP32-CAM (AI Thinker)
- ESP8266 NodeMCU
- PCA9685 Servo Driver
- Servo Motors (25kg + MG995)

## Software
- Python (OpenCV, Ultralytics YOLOv8)
- Arduino (ESP8266 firmware)
- Roboflow (dataset)

## Current Status
- Vision system: Working
- Robotic arm: Working
- Integration: Semi-automated (manual trigger)

## Future Work
- Automatic actuation from detection
- Multi-class waste sorting
- Fully autonomous rover integration

## Pictures

CAD - ARM: <br>
<img width="995" height="602" alt="image" src="https://github.com/user-attachments/assets/5766520b-847f-4731-ac8d-2b2ea3557665" />
<br>
CAD - ROVER: <br>
<img width="853" height="661" alt="image" src="https://github.com/user-attachments/assets/1dff2aaa-8243-455b-bc28-35221dd83583" />
<br>
Python Control Interface: <br>
<img width="1600" height="822" alt="image" src="https://github.com/user-attachments/assets/b5581921-9a91-4ab4-b3ce-72d213ae9851" />
<br>
Vision Subsystem: <br>
<img width="1399" height="624" alt="image" src="https://github.com/user-attachments/assets/95c09f0f-252e-4068-bc57-95c5644c7cdf" />
<br>
## Demo <br>
<img width="360" height="294" alt="image" src="https://github.com/user-attachments/assets/2efd478d-768f-4210-bb5c-3e99fc0153d9" />
<img width="335" height="353" alt="image" src="https://github.com/user-attachments/assets/de67f3ae-c2d6-49d9-a343-e66f9a53936e" />



