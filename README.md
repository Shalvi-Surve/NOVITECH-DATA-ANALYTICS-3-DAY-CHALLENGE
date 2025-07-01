# **Movie Dataset Cleanup - Novitech Data Analysis Internship (Day 3 Challenge)**

## **Project Overview**
This repository contains the solution for the **Day 3 Data Cleanup Challenge** from the **Novitech Data Analysis Internship**. The script, **`clean_movies.py`**, cleans the **`movies.csv`** dataset by handling missing values, removing duplicates, and standardizing formats. It outputs cleaned files: **`movies_cleaned.csv`** and **`movies_cleaned.xlsx`**.

## **Key Features**
- **Data Cleaning**: Resolves missing values, eliminates duplicates, and standardizes data types.
- **Output Files**:
  - **`movies_cleaned.csv`**: Cleaned dataset in CSV format.
  - **`movies_cleaned.xlsx`**: Cleaned dataset in Excel format.
- **Warning Suppression**: Suppresses **`pandas`** **`RuntimeWarning`** for clean console logs.
- **Local Execution**: Runs on local Python environments like **Python IDLE**, **VS Code**, or **PyCharm**.

## **Technologies Used**
- **Python**: Version 3.x
- **Libraries**:
  - **`pandas`**: Data manipulation and cleaning.
  - **`numpy`**: Numerical operations.
  - **`openpyxl`**: Excel file output.
- **Environment**: Local Python setup.

## **Dataset**
The input dataset, **`movies.csv`**, includes columns like:
- **Title**: Movie name.
- **Genre**: Movie category.
- **Release Year**: Year of release.
- **Ratings**: Movie ratings.

The script ensures the data is clean and analysis-ready.

## **Getting Started**

### **Prerequisites**
- **Python 3.x** installed.
- Required libraries:
  ```bash
  pip install pandas numpy openpyxl
  ```
- The **`movies.csv`** dataset (not included; source from **Novitech** or your provider).

### **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. **Navigate to the Directory**:
   ```bash
   cd your-repo-name
   ```
3. **Install Dependencies**:
   ```bash
   pip install pandas numpy openpyxl
   ```

### **Usage**
1. **Prepare the Dataset**:
   - Place **`movies.csv`** in the same directory as **`clean_movies.py`**.
   - Check the file path in **`clean_movies.py`** (default: same directory).
2. **Run the Script**:
   ```bash
   python clean_movies.py
   ```
3. **Check Outputs**:
   - Find **`movies_cleaned.csv`** and **`movies_cleaned.xlsx`** in the project directory.

## **File Structure**
- **`clean_movies.py`**: Main cleaning script.
- **`movies.csv`**: Input dataset (not included; source separately).
- **`movies_cleaned.csv`**: Cleaned CSV output.
- **`movies_cleaned.xlsx`**: Cleaned Excel output.

## **Notes**
- Verify the **`movies.csv`** file path in **`clean_movies.py`** for your setup.
- The script suppresses **`pandas`** warnings for a cleaner console.
- For contributions or issues, submit a **pull request** or open an **issue** on **GitHub**.

## **Acknowledgments**
- **Novitech**: For the dataset and internship opportunity.
- **Open-Source Community**: For **`pandas`**, **`numpy`**, and **`openpyxl`** libraries.

## **Contact**
For feedback or questions, open an **issue** or visit [GitHub](https://github.com/your-username).
