# Pasco County MPUD: A Geospatial Audit

### [🔗 View the Full StoryMap Portfolio](https://storymaps.arcgis.com/stories/89a7965cbe4743c29b8d56fc765aee2d)

<img width="996" height="509" alt="Pasco MPUD" src="https://github.com/user-attachments/assets/b5652bff-5522-4dd8-ab8a-2e6c29ecdfe2" />

## Project Overview
This project performs a comprehensive geospatial audit of Master Planned Unit Developments (MPUDs) within Pasco County, Florida. By synthesizing historical planning records with modern spatial data, this audit evaluates zoning compliance, land use efficiency, and the long-term infrastructure impacts of large-scale residential and commercial developments.

## 🛠️ Automation & Data Governance (PyQGIS)
To ensure the integrity of the audit and maintain a defensible record of data commits, I developed a custom **Python-based Data Governance tool** embedded within the QGIS environment. This system transitions the workflow from manual technician entry to automated analyst-level oversight.

### **1. Research & Logic Development**
<img width="1279" height="761" alt="code research" src="https://github.com/user-attachments/assets/ac390fa5-6f31-4889-a8bc-558e424f5098" />

*Utilizing the Python `datetime` and `os` libraries to build a localized auditing logic. This phase involved researching the PyQGIS API to ensure the script could operate silently in the background without interrupting the primary spatial analysis.*

### **2. System Integration**
<img width="1280" height="761" alt="Setting up project macros in properties" src="https://github.com/user-attachments/assets/b90f0f14-8830-4210-a6fd-5c031e173cbc" />

*The script is integrated via QGIS Project Macros as an "Event Listener." It is designed to trigger automatically upon every project save, capturing critical metadata including timestamps and project paths to ensure accountability across the project lifecycle.*

### **3. External Audit Trail**
<img width="1280" height="763" alt="external save successfull" src="https://github.com/user-attachments/assets/d6c99f69-679b-4ec2-a1f7-64055d16e5b3" />

*The final implementation generates a persistent, external `.txt` log. This ensures that even if the project file is moved or shared, a permanent record of data commits remains accessible for QA/QC and regulatory reporting.*

## Technical Objectives
* **Zoning Compliance:** Auditing spatial boundaries of MPUDs against the Pasco County Comprehensive Plan.
* **Data Integration:** Aggregating data from the Pasco County BOCC, FEMA flood-prone delineations, and SWFWMD land cover datasets.
* **Infrastructure Analysis:** Evaluating the relationship between proposed development density and existing public facility capacity.

## Key Skills Demonstrated
* **ArcGIS Pro & StoryMaps:** Creating a narrative-driven spatial report for stakeholders and government officials.
* **Advanced Python (PyQGIS):** Automating quality control workflows and data governance protocols.
* **Planning & Regulatory Knowledge:** Understanding of Land Development Codes (LDC) and Future Land Use (FLU) classifications.
* **Geospatial Auditing:** Identifying discrepancies between historical documentation and current digital spatial databases.

## Data Sources
* **Pasco County BOCC:** Master Planned Unit Development (MPUD) feature services.
* **FEMA:** Floodplain and wetland delineations for environmental impact assessment.
* **SWFWMD:** Land Use and Land Cover (LULC) source layers.

---
**Geospatial Analysis, Automation Scripting, and StoryMap Design by Leonard Sala.**
