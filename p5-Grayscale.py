import cv2

img = cv2.imread('quote.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

while True:
    cv2.imshow('Quote Image - Original',img)
    cv2.imshow('Quote Image - Grayscale',gray)
    cv2.imshow('Quote Image - Binary',binary)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()

# cv2.threshold - Main method
# cv2.THRESH_BINARY - SUb method



# Error : TypeError: Expected Ptr<cv::UMat> for argument 'mat'


