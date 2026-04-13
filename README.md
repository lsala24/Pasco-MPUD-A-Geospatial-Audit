# Pasco County MPUD: A Geospatial Audit

### [🔗 View the Full StoryMap Portfolio](https://storymaps.arcgis.com/stories/89a7965cbe4743c29b8d56fc765aee2d)

<img width="996" height="509" alt="Pasco MPUD" src="https://github.com/user-attachments/assets/b5652bff-5522-4dd8-ab8a-2e6c29ecdfe2" />

## Project Overview
This project performs a comprehensive geospatial audit of Master Planned Unit Developments (MPUDs) within Pasco County, Florida. By synthesizing historical planning records with modern spatial data, this audit evaluates zoning compliance, land use efficiency, and the long-term infrastructure impacts of large-scale residential and commercial developments.

## 🛠️ Automation & Data Governance (PyQGIS)
To ensure the integrity of the audit and maintain a defensible record of data commits, I developed a custom **Python-based Data Governance tool** embedded within the QGIS environment.

### **1. Research & Logic Development**

*Code Research: Utilizing the Python `datetime` and `os` libraries to build a localized auditing logic that avoids the security risks of hard-coded credentials.*

<img width="1279" height="761" alt="code research" src="https://github.com/user-attachments/assets/b913d53d-4dd5-48fe-8ae1-a5371adf35a6" />


### **2. System Integration**
![Setting up Macros](images/Setting_up_project_macros_in_properties.PNG)
*Integrating the script via QGIS Project Macros. This "Event Listener" automatically triggers every time a project save is initiated, capturing metadata without requiring manual technician input.*

### **3. External Audit Trail**
![Success Message](images/external_save_successfull.PNG)
*The final output: A successful commit message in the Python console and a persistent, external `.txt` log that serves as a permanent paper trail of the audit's progress.*

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
