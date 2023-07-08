import easyocr
import cv2

# read the image
filename = 'demo2.jpeg'
img = cv2.imread(f'images/{filename}')

# make instance of easyocr reader
# we are asking english 'en' to detect in images
reader = easyocr.Reader(['en'])

# detect text from image
detected_text = reader.readtext(img)

# Open the file in append mode to preserve existing content
file_path = 'detected_text.txt'
with open(file_path, 'a') as file:
    # Iterate over the detected text results
    file.write(f'\nDetected Text of {filename} \n')
    print(detected_text)
    for bbox, text, conf in detected_text:
        if conf > 0.3:
            # Draw bounding box and add text on the image
            cv2.rectangle(img, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (255, 0, 0), 1)
            cv2.putText(img, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

            # Write the text and its confidence to the file
            file.write(f'Text: {text}, Confidence: {conf}\n')

            # Print the confidence
            print(f'Text: {text}, Confidence: {conf}\n')

# Save the image with bounding boxes and text

# cv2.imwrite(f'text_in_{filename}', img)
cv2.imwrite(f'images_with_text/{filename}', img)

