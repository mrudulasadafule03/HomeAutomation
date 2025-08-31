# Major_project
This is my final year project (Major Project ) of Diploma in Computer Technology at S.E.S Polytechnic Solapur.

GROUP MEMBERS : 
1. Viresh Kamlapure 
2. Sahil Chouhan 
3. Mrudula Sadafule 
4. Komal Kudal

---

# 🏠 Home Automation System

A **Home Automation System** project designed to control and monitor appliances using sensors, Python scripts, and a simple web interface.  
This system demonstrates how IoT and automation can improve comfort, security, and efficiency in smart homes.

---

## 🚀 Features
- 🔌 **Device Control** – Turn ON/OFF appliances (fan, bulb, etc.).
- 🎛️ **Sensor Integration** – Read input from IR sensors and other devices.
- 🌐 **Web Interface** – Control appliances from a browser (`index.html`).
- 🎥 **Demo Videos** – Output demonstration included (`output1.mp4`, `output2_compressed.mp4`, `output3.mp4`).
- 🖼️ **UI Assets** – Images for ON/OFF state visualization.

---

## 🛠️ Technologies Used
- **Programming Language:** Python (homeAutomation.py, ir.py, sensor.py)  
- **Frontend:** HTML  
- **Backend/Logic:** Python scripts  
- **Media:** Images & Videos for simulation/demonstration  
- **Hardware (if connected):** IR Sensors, Home Appliances  

---

## 📂 Project Structure

```bash
home-automation/
├── HomeAutomation-main/
│   ├── FINAL_REPORT_merged.pdf
│   ├── README.md
│   ├── homeAutomation.py
│   ├── index.html
│   ├── ir.py
│   ├── output1.mp4
│   ├── output2_compressed.mp4
│   ├── output3.mp4
│   ├── sensor.py
│   └── static/
│       └── images/
│           ├── BOFF.jpg
│           ├── BON.jpg
│           ├── FOFF.jpg
│           ├── FON.jpg
│           └── background.jpg
```

---

## ⚡ Installation & Setup
## 1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/HomeAutomation.git
   cd HomeAutomation-main
   ```
## 2. Install dependencies (Python 3 required):
- flask → for running the web server (serving index.html)
- gpiozero → for controlling GPIO pins (used in Raspberry Pi)
- RPi → Raspberry Pi GPIO library (RPi.GPIO)
- time → Python standard library (already included, no need to install)

## 3. Run the Python script:

```bash
python homeAutomation.py
```

## 4. Open the web interface in your browser:

```bash
http://localhost:5000
```
(Adjust port if defined differently in the code)


