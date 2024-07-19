import cv2

# Read input image
img = cv2.imread('test_img.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth the image while keeping edges sharp
color = cv2.bilateralFilter(img, 9, 250, 250)

# Combine the edges and color image
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Save output image
cv2.imwrite('cartoon_image.jpg', cartoon)
print("Successful")