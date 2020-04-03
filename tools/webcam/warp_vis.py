#!/usr/bin/env python3.6
import numpy as np
import time

# copied from common.transformations/camera.py
eon_focal_length = 910.0 # pixels
eon_dcam_focal_length = 860.0 # pixels

webcam_focal_length = 908.0 # pixels

###############################################
want_width = 1280
want_height = 720
want_fps = 2
want_hdw_change = 0
###############################################
fac=1.
eon_intrinsics = np.array([
  [eon_focal_length,   0.,   1164/fac],
  [  0.,  eon_focal_length,  874/fac],
  [  0.,    0.,     1.]])

eon_dcam_intrinsics = np.array([
  [eon_dcam_focal_length,   0,   1152/fac],
  [  0,  eon_dcam_focal_length,  864/fac],
  [  0,    0,     1]])

webcam_intrinsics = np.array([
  [webcam_focal_length,   0.,   want_width/fac],
  [  0.,  webcam_focal_length,  want_height/fac],
  [  0.,    0.,     1.]])

if __name__ == "__main__":
  import cv2
  trans_webcam_to_eon_rear = np.dot(eon_intrinsics,np.linalg.inv(webcam_intrinsics))
  trans_webcam_to_eon_front = np.dot(eon_dcam_intrinsics,np.linalg.inv(webcam_intrinsics))
  print("trans_webcam_to_eon_rear:\n", trans_webcam_to_eon_rear)
  print("trans_webcam_to_eon_front:\n", trans_webcam_to_eon_front)

  cap = cv2.VideoCapture(1)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, want_width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, want_height)
  if want_hdw_change > 0:
    cap.set(cv2.CV_CAP_PROP_FPS, want_fps)
  startTime = time.time() * 100
  while (True):
    ret, img = cap.read()
    if ret:
      nowTime = time.time() * 100
      if (nowTime-startTime) > 100/want_fps:
        startTime = nowTime
        # img = cv2.warpPerspective(img, trans_webcam_to_eon_rear, (1164,874), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        img2 = cv2.warpPerspective(img, trans_webcam_to_eon_front, (1164,874), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        print(img.shape, end='\r')
        cv2.imshow('preview', img2)
        cv2.waitKey(10)


