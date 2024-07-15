'''import cv2
import numpy as np

def detect_dominant_color(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize image to reduce processing time
    image = cv2.resize(image, (600, 400))
    
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Reshape image to a 2D array of pixels
    pixels = image_rgb.reshape(-1, 3)
    
    # Convert pixels to float
    pixels = np.float32(pixels)
    
    # Define criteria and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 3  # Number of clusters (colors)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert centers to integers
    centers = np.uint8(centers)
    
    # Get dominant colors
    dominant_colors = centers[labels.flatten()]
    
    # Count occurrences of each color
    unique, counts = np.unique(labels, return_counts=True)
    color_counts = dict(zip(unique, counts))
    
    # Sort colors by count
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for i in sorted_colors:
        result.append({
            'color': centers[i[0]].tolist(),
            'count': i[1]
        })
    
    return result

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    results = detect_dominant_color(image_path)
    print(results)'''
