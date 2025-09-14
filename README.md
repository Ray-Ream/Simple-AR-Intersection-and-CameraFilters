# Simple-AR-Intersection-and-CameraFilters

使用 MediaPipe 進行簡單 AR 疊圖互動 (Python 範例)、影像濾鏡  

簡介  
本專案提供一個使用 MediaPipe 進行簡單 AR 疊圖互動 的範例。  
程式以 Python 撰寫，並可在 CPU 上執行，無需額外 GPU 加速。  
使用者可透過 電腦相機 (內建或外接 webcam) 進行即時互動。  
Introduction  
This project provides a simple Augmented Reality (AR) overlay interaction example using MediaPipe.  
It is implemented in Python and can run purely on CPU, without requiring GPU acceleration.  
The interaction works in real time with a computer camera or external webcam.  

功能 Features  
- 使用 MediaPipe 偵測臉部 / 手部關鍵點  
- 在畫面中即時疊加圖像 (範例：眼鏡、貼紙、圖示)  
- 支援一般電腦與 webcam  
- 輕量化運算，CPU 即可執行  
- Face / Hand landmark detection via MediaPipe  
- Real-time overlay of images (e.g., glasses, stickers, icons)  
- Works with computer camera / webcam  
- CPU-friendly, no GPU required  

環境需求 Requirements  
-Python 3.8+  
-OpenCV  
-MediaPipe  
```pip install opencv-python mediapipe```
