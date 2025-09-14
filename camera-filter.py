# Import required Libraries
from random import *

import cv2
import numpy as np

from tkinter import *
from PIL import Image, ImageTk

# region Tkinter setup.
win = Tk()
win.title("期末專案")
win.geometry("800x600")
win.resizable(False, False)
# endregion

# Create a Label to capture the Video frames
label = Label(win)
label.grid(row=0, column=0)
cap = cv2.VideoCapture(0)


def btn_ModChange(n):
    print("Change mode to: ", n, "mode.")
    global mode
    mode = n


glass_button = Button(win, text='Glass filter', command=lambda: btn_ModChange(1))
glass_button.grid(row=1, column=0, ipadx=5, pady=5, sticky=W + E + N + S)
oil_button = Button(win, text='Oli effect filter', command=lambda: btn_ModChange(2))
oil_button.grid(row=2, column=0, ipadx=5, pady=5, sticky=W + E + N + S)
old_button = Button(win, text='Old filter', command=lambda: btn_ModChange(3))
old_button.grid(row=3, column=0, ipadx=5, pady=5, sticky=W + E + N + S)
original_button = Button(win, text='Original mod', command=lambda: btn_ModChange(0))
original_button.grid(row=4, column=0, ipadx=5, pady=5, sticky=W + E + N + S)


def glass_Filter(img):
    h, w = img.shape[:2]
    glassImage = np.zeros((h, w, 3), np.uint8)
    for i in range(h - 6):
        for j in range(w - 6):
            idx = int(np.random.random() * 6)
            glassImage[i, j] = img[i + idx, j + idx]
    return glassImage


def oil(img):
    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    dst = np.zeros((height, width, 3), np.uint8)

    for i in range(2, height - 2):
        for j in range(2, width - 2):
            arr1 = np.zeros(8, np.uint8)
            for m in range(-2, 2):
                for n in range(-2, 2):
                    p1 = int(gray[i + m, j + n] / 32)
                    arr1[p1] = arr1[p1] + 1

            currentMax = max(arr1)
            currentMaxIdx = list(arr1).index(currentMax)
            for m in range(-2, 2):
                for n in range(-2, 2):
                    if (currentMaxIdx * 32) <= gray[i + m, j + n] <= ((currentMaxIdx + 1) * 32):
                        (b, g, r) = img[i + m, j + n]
                        dst[i, j] = (b, g, r)
    return dst


def oil_effect(img):
    h, w, n = img.shape
    new_img = np.zeros((h - 2, w, n), dtype=np.uint8)
    for i in range(h - 4):
        for j in range(w):
            if randint(1, 10) % 3 == 0:
                new_img[i, j] = img[i - 3, j]
            elif randint(1, 10) % 2 == 0:
                new_img[i, j] = img[i + 3, j]
            else:
                new_img[i, j] = img[i + 2, j]
    return new_img


def old(img):
    h, w, n = img.shape
    oldImg = np.zeros((h, w, n), np.uint8)
    for i in range(h):
        for j in range(w):
            # b = 0.272 * img[i, j][2] + 0.534 * img[i, j][1] + 0.131 * img[i, j][0]
            # g = 0.349 * img[i, j][2] + 0.686 * img[i, j][1] + 0.168 * img[i, j][0]
            # r = 0.393 * img[i, j][2] + 0.769 * img[i, j][1] + 0.189 * img[i, j][0]

            b = 0.272 * img[i, j][2] + 0.534 * img[i, j][1]
            g = 0.349 * img[i, j][2] + 0.686 * img[i, j][1]
            r = 0.393 * img[i, j][2] + 0.769 * img[i, j][1]
            if b > 255:
                b = 255
            if g > 255:
                g = 255
            if r > 255:
                r = 255
            oldImg[i, j] = np.uint8((b, g, r))
    return oldImg


# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    frame = cap.read()[1]
    frame = cv2.resize(frame, (600, 400))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if mode == 1:

        delay_time = 30
        cv2image = glass_Filter(cv2image)
    elif mode == 2:
        delay_time = 100
        cv2image = oil_effect(cv2image)
    elif mode == 3:
        delay_time = 100
        cv2image = old(cv2image)
    else:
        delay_time = 20
        pass

    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    img_Tk = ImageTk.PhotoImage(image=img)
    label.img_Tk = img_Tk
    label.configure(image=img_Tk)
    # Repeat after an interval to capture continuously
    label.after(delay_time, show_frames)


btn_ModChange(0)
show_frames()
win.mainloop()
