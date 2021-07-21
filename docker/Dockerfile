FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential cmake pkg-config
RUN apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
RUN apt-get apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get install libxvidcore-dev libx264-dev
RUN apt-get install libatlas-base-dev gfortran
RUN apt-get install python3-dev


RUN pip3 install pip --upgrade
RUN pip3 install scipy
RUN pip3 install numpy
RUN pip3 install imutils
RUN pip3 install pandas
RUN pip3 install dlib
RUN pip3 install opencv-python
RUN pip3 install streamlit

