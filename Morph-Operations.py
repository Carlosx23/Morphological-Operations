# Importing necessary libraries
from tkinter import image_names
import cv2
import numpy as np

# Function to demonstrate erosion operation
def erosion_exercise():
    image = cv2.imread('carlos.png')  # Load the image
    image2 = cv2.imread('carlos2.png')  # Load another image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for erosion
    erosion = cv2.erode(image, kernel)  # Apply erosion operation to the image
    erosion2 = cv2.erode(image2, kernel)  # Apply erosion operation to the second image

    # Display the original and eroded images
    cv2.imshow('original_image', image)
    cv2.imshow('original_image2', image2)
    cv2.imshow('eroded_image', erosion)
    cv2.imshow('eroded_image2', erosion2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to demonstrate dilation operation
def dilation_exercise():
    image = cv2.imread('carlos.png')  # Load the image
    image2 = cv2.imread('carlos2.png')  # Load another image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for dilation
    dilation = cv2.dilate(image, kernel)  # Apply dilation operation to the image
    dilation2 = cv2.dilate(image2, kernel)  # Apply dilation operation to the second image

    # Display the original and dilated images
    cv2.imshow('original_image', image)
    cv2.imshow('original_image2', image2)
    cv2.imshow('dilated_image', dilation)
    cv2.imshow('dilated_image2', dilation2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to demonstrate opening operation
def opening_exercise():
    image = cv2.imread('carlos.png')  # Load the image
    image2 = cv2.imread('carlos2.png')  # Load another image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for morphological opening
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)  # Apply opening operation to the image
    opening2 = cv2.morphologyEx(image2, cv2.MORPH_OPEN, kernel)  # Apply opening operation to the second image

    # Display the original and opened images
    cv2.imshow('original_image', image)
    cv2.imshow('original_image2', image2)
    cv2.imshow('opened_image', opening)
    cv2.imshow('opened_image2', opening2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to demonstrate closing operation
def closing_exercise():
    image = cv2.imread('carlos.png')  # Load the image
    image2 = cv2.imread('carlos2.png')  # Load another image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for morphological closing
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)  # Apply closing operation to the image
    closing2 = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, kernel)  # Apply closing operation to the second image

    # Display the original and closed images
    cv2.imshow('original_image', image)
    cv2.imshow('original_image2', image2)
    cv2.imshow('closed_image', closing)
    cv2.imshow('closed_image2', closing2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to demonstrate a specific points exercise
def points_exercise():
    image = cv2.imread('carlos_puntos.png')  # Load the image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for morphological opening
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)  # Apply opening operation to the image
    opened2 = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)  # Apply opening operation again

    cv2.imshow('original_image', image)  # Display the original image
    cv2.imshow('opened_image', opened)  # Display the image after the opening operation
    cv2.imshow('opened_image2', opened2)  # Display the image after opening twice

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to demonstrate another specific points exercise
def points_exercise2():
    image = cv2.imread('carlos_puntos2.png')  # Load the image

    kernel = np.ones((3, 3), np.uint8)  # Create a filter (kernel) for morphological closing
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)  # Apply closing operation to the image
    closed2 = cv2.morphologyEx(closed, cv
