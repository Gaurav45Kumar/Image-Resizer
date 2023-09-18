import cv2
import os

# Try to load the image
image = cv2.imread("C:\\faces\\diljit.jpeg")

if image is None:
    print("Error: Could not open or read the image.")
else:
    # Define the new width and height for the resized image
    new_width = 300  # Change this value to your desired width
    new_height = 200  # Change this value to your desired height

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Define the path for the resized image in the specified directory
    output_dir = r"C:\Python Projects CWH\Image Resizer"
    output_path = os.path.join(output_dir, "resized.jpeg")

    # Save the resized image to the specified directory
    cv2.imwrite(output_path, resized_image)

    # Display the resized image (optional)
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Resized image saved as {output_path}")
