import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage import exposure
from scipy.stats import pearsonr

# Define the directory containing images and the path to clinical data
image_dir = 'data/images'
clinical_data_path = 'data/clinical_data.xlsx'
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Function to preprocess and analyze images
def analyze_images(image_dir):
    results = []

    for image_file in os.listdir(image_dir):
        if image_file.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(image_dir, image_file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Preprocess the image (e.g., thresholding, denoising)
            _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
            denoised = cv2.medianBlur(thresh, 5)

            # Analyze the image using region properties
            labeled_image = label(denoised)
            properties = regionprops(labeled_image)

            for prop in properties:
                result = {
                    'image': image_file,
                    'area': prop.area,
                    'bbox': prop.bbox,
                    'eccentricity': prop.eccentricity,
                    'extent': prop.extent,
                    'perimeter': prop.perimeter,
                }
                results.append(result)

    return pd.DataFrame(results)

# Function to perform statistical analysis
def perform_statistical_analysis(merged_data):
    # Descriptive statistics
    stats_summary = merged_data.describe()

    # Correlation analysis between LEMG scores and image properties
    correlations = {}
    for col in merged_data.columns:
        if col not in ['patient_id', 'LEMG_score']:
            correlations[col] = pearsonr(merged_data['LEMG_score'], merged_data[col])

    return stats_summary, correlations

# Analyze images and save results to a DataFrame
print("Analyzing images...")
image_analysis_results = analyze_images(image_dir)
image_analysis_results.to_csv(os.path.join(output_dir, 'image_analysis_results.csv'), index=False)

# Load clinical data
print("Loading clinical data...")
clinical_data = pd.read_excel(clinical_data_path)

# Merge image analysis results with clinical data
print("Merging data...")
merged_data = pd.merge(clinical_data, image_analysis_results, on='patient_id')

# Perform statistical analysis
print("Performing statistical analysis...")
stats_summary, correlations = perform_statistical_analysis(merged_data)

# Save statistical summary and correlation results
stats_summary.to_csv(os.path.join(output_dir, 'stats_summary.csv'))
with open(os.path.join(output_dir, 'correlations.csv'), 'w') as f:
    for key, value in correlations.items():
        f.write(f"{key},{value[0]},{value[1]}
")

# Display statistical summary
print(stats_summary)
print("Correlation analysis complete. Results saved to 'correlations.csv'.")
