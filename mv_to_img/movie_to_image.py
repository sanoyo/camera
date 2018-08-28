# Reference URL
# http://testpy.hatenablog.com/entry/2017/07/13/003000
import os
import shutil
import cv2
import time

def video_2_frames(video_file='../VIDEO_0062.mp4', image_dir='image_dir', image_file='img_%s.png'):
    # Delete the entire directory tree if it exists.
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Video to frames
    i = 0
    # Create Object
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        # 時間計測スタート→1枚ごとの時間
        start = time.time()
        # flag → フレームの読み込みができるいるかどうか
        # frame → フレームごとの座標
        flag, frame = cap.read()
        if flag == False:  # Is a frame left?
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(6), frame)  # Save a frame
        print('Save', image_dir+image_file % str(i).zfill(6))
        # 時間計測終了
        end = time.time()
        # 計測時間表示
        print (end-start, "[sec]")
        i += 1

    cap.release()  # When everything done, release the capture


video_2_frames()
