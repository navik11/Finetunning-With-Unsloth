# Finetunning-with-Unsloth [Datasets]

This repository contains datasets prepared for fine-tuning language and vision models with [Unsloth](https://github.com/unslothai/unsloth).  
The datasets are agriculture-focused, covering crop production, crop recommendation, and farmer query-response pairs.

---

## Repository Structure  

### 1. **AgricultureDataset.csv**  
A structured dataset of agricultural production across Indian states and districts.  

**Columns:**  
- `State_Name` – Name of the state  
- `District_Name` – Name of the district  
- `Crop_Year` – Year of production  
- `Season` – Agricultural season (e.g., Kharif, Rabi, etc.)  
- `Crop` – Type of crop  
- `Area` – Cultivation area (in hectares)  
- `Production` – Crop production (in tonnes)  

---

### 2. **Crop_recommendation.csv**  
A dataset for **crop recommendation** based on soil and climate parameters.  

**Columns:**  
- `N` – Nitrogen content in soil  
- `P` – Phosphorus content in soil  
- `K` – Potassium content in soil  
- `temperature` – Temperature in °C  
- `humidity` – Relative humidity (%)  
- `ph` – Soil pH value  
- `rainfall` – Rainfall (mm)  
- `label` – Recommended crop  

---

### 3. **farmer_call_query_dataset.csv**  
A conversational dataset of **farmer queries** and expert-provided **answers**. Useful for fine-tuning **chatbot-style models** for agriculture support.  

**Columns:**  
- `questions` – Farmer’s query  
- `answers` – Expert’s response  

---