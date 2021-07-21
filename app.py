
import streamlit as st
import pandas as pd
from model_process import process_detect, show_lines
import numpy as np
import cv2
import imutils
import math

st.title("Detecção de Pessoas")
st.sidebar.title('Configurations')



video_source = "video/example_02.mp4"
vs = cv2.VideoCapture(video_source)
_, frame = vs.read()
frame = imutils.resize(frame, width=640)
(H, W) = frame.shape[:2]
frame_show = st.empty()
frame_show.image(frame, channels="BGR")  

st.sidebar.header('UP')
up_x0 = st.sidebar.slider("UP X0", 0, W)
up_y0 = st.sidebar.slider("UP Y0", 0, H)
up_x1 = st.sidebar.slider("UP X1", 0, W)
up_y1 = st.sidebar.slider("UP Y1", 0, H)

st.sidebar.header('DOWN')
down_x0 = st.sidebar.slider("DOWN X0", 0, W)
down_y0 = st.sidebar.slider("DOWN Y0", 0, H)
down_x1 = st.sidebar.slider("DOWN X1", 0, W)
down_y1 = st.sidebar.slider("DOWN Y1", 0, H)

p0_up = np.array((up_x0, up_y0))
p1_up = np.array((up_x1, up_y1))
p0_down = np.array((down_x0, down_y0))
p1_down = np.array((down_x1, down_y1))


if st.sidebar.button('MOSTRAR LIHAS'):
    show_lines(frame, p0_up, p1_up, p0_down, p1_down)


if st.sidebar.button('RUN'):
    deltaY = up_y1 - up_y0
    deltaX = up_x1 - up_x0
    y_line = False
    angle = abs(math.atan2(deltaY, deltaX)*180/math.pi)
    if (angle >= 0 and angle < 45) or (angle > 135 and angle <= 180):
        y_line=True
    else:
        y_line=False
    
    process_detect(vs, p0_up, p1_up, p0_down, p1_down, y_line)





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
