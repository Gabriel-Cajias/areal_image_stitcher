import cv2 as cv
import os
if __name__ == "__main__":
    """
    for filename in os.listdir("src/"):
        img_path = os.path.join("src/", filename)
        img = cv.imread(img_path)
        if img is not None:
            imgs.append(img)
        else:
            print("HELL NO")
    """
    for o in range(1,187, 11):
        imgs = []
        for i in range(o, o+11):
            if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                num = "00" + str(i)
            elif i < 100:
                num = "0" + str(i)
            elif i > 100:
                num = str(i)
            img = cv.imread("src/DJI_0" + num + ".JPG")
            simg = cv.resize(img, (720, 480))
            if img is not None:
                imgs.append(simg)

        stitcher = cv.Stitcher.create(cv.Stitcher_SCANS)

        status, pano = stitcher.stitch(imgs)
        if status == cv.Stitcher_OK:
            print("Stitching completed successfully.")
            cv.imwrite("SHOWED_" + str(o) + ".png", pano)
        else:
            print("Stitching failed with status code:", status)
            if status == cv.Stitcher_ERR_NEED_MORE_IMGS:
                print("Need more images to stitch.")
            elif status == cv.Stitcher_ERR_HOMOGRAPHY_ESTIMATION_FAILED:
                print("Homography estimation failed.")
            elif status == cv.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
                print("Camera parameters adjustment failed.")

