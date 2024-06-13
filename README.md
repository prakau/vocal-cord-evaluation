# Comprehensive Evaluation of Vocal Cord Fixation

This project processes CT images and laryngeal electromyography (LEMG) data to evaluate vocal cord fixation. The script normalizes data, aligns scans, analyzes images and LEMG data, and performs statistical evaluations.

## Files and Directory Structure

vocal-cord-evaluation/
│
├── data/
│ ├── images/ # Directory containing CT images
│ └── clinical_data.xlsx # Clinical data file
│
├── results/ # Directory for storing results
│
├── README.md
├── requirements.txt
└── script.py

## Steps

1. **Data Collection and Preparation**
   - Collect patient demographics, clinical history, CT imaging, and LEMG data.
   - Ensure all CT images are processed and standardized for consistency in analysis.
   - Enter all relevant data into a structured database for easy access and analysis.

2. **Image Analysis**
   - Analyze CT images for structural abnormalities, fixation patterns, and glottis measurements.
   - Select representative images per patient to capture the full range of vocal cord movement.

3. **Electromyography Analysis**
   - Analyze LEMG data for spontaneous potential scores and neurogenic changes in the thyroarytenoid muscle.
   - Evaluate the contraction characteristics of the affected vocal cords.

4. **Statistical Analysis**
   - Summarize demographic data, diagnosis distribution, and imaging findings.
   - Compare open and closed phase characteristics, glottis measurements, and contraction patterns across different etiologies.
   - Assess the correlation between LEMG findings and CT imaging results.

5. **Interpretation and Reporting**
   - Interpret findings in the context of clinical diagnoses and patient outcomes.
   - Generate comprehensive reports summarizing the analysis for each patient.

## Usage

1. Place the metadata, raw data, and background data files in the `data` directory.
2. Run the script using Python 3.

```sh
python script.py
```

## Dependencies

Install the required packages using:

```sh
pip install -r requirements.txt
```

## Output

The processed data and analysis results are saved in the results directory.
