import cv2 as cv
import os
# Will turn this into a class eventually, in lecture rn
# This is temporary, will be replaced by gps coordinates
fileList = os.listdir("src/")

imgs = []

for i in fileList:
    img = cv.imread("src/" + i)
    if img is not None:
        imgs.append(cv.resize(img, (720, 480)))

# This is permanent
stitcher = cv.Stitcher.create(cv.Stitcher_SCANS)

status, pano = stitcher.stitch([imgs[11],imgs[12],imgs[13]])  # temporary bit
if status == cv.Stitcher_OK:
    print("Stitching completed successfully.")
    cv.imwrite("pano.png", pano)
else:
    print("Stitching failed with status code:", status)
    if status == cv.Stitcher_ERR_NEED_MORE_IMGS:
        print("Need more images to stitch.")
    elif status == cv.Stitcher_ERR_HOMOGRAPHY_ESTIMATION_FAILED:
        print("Homography estimation failed.")
    elif status == cv.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
        print("Camera parameters adjustment failed.")

