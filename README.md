# Pasco County MPUD: A Geospatial Audit

### [🔗 View the Full StoryMap Portfolio](https://storymaps.arcgis.com/stories/89a7965cbe4743c29b8d56fc765aee2d)

<img width="996" height="509" alt="Pasco MPUD" src="https://github.com/user-attachments/assets/b5652bff-5522-4dd8-ab8a-2e6c29ecdfe2" />

## Project Overview
This project performs a comprehensive geospatial audit of Master Planned Unit Developments (MPUDs) within Pasco County, Florida. The primary focus was transitioning a legacy administrative dataset into a high-precision geospatial tool by resolving topological overlaps and correcting geometry to create a reliable "source of truth" for regional planning.

## 🛠️ Automation & Data Governance (PyQGIS)
To ensure the integrity of the audit and maintain a defensible record of data commits, I developed a custom **Python-based Data Governance tool** embedded within the QGIS environment. This system transitions the workflow from manual technician entry to automated analyst-level oversight.

### **1. Research & Logic Development**
[INSERT PHOTO LINK HERE]
*Utilizing the Python `datetime` and `os` libraries to build a localized auditing logic. This phase involved researching the PyQGIS API to ensure the script could operate silently in the background without interrupting the primary spatial analysis.*

### **2. System Integration**
[INSERT PHOTO LINK HERE]
*The script is integrated via QGIS Project Macros as an "Event Listener." It is designed to trigger automatically upon every project save, capturing critical metadata including timestamps and project paths to ensure accountability across the project lifecycle.*

### **3. External Audit Trail**
[INSERT PHOTO LINK HERE]
*The final implementation generates a persistent, external `.txt` log. This ensures that even if the project file is moved or shared, a permanent record of data commits remains accessible for QA/QC and regulatory reporting.*

## Technical Objectives
* **Zoning Compliance:** Auditing spatial boundaries of MPUDs against historical planning records and the Pasco County Comprehensive Plan.
* **Topological Integrity:** Identifying and resolving gaps, overlaps, and geometry errors within the MPUD feature class.
* **Data Governance:** Implementing automated logging to track edits and maintain version control throughout the audit process.

## Key Skills Demonstrated
* **Advanced Python (PyQGIS):** Automating quality control workflows and data governance protocols.
* **Geospatial Auditing:** Identifying discrepancies between historical documentation and current digital spatial databases.
* **Data Integrity:** Mastering the "dirty cleaning" process to ensure administrative data is map-ready and analytically sound.

## Data Sources
* **Pasco County BOCC:** Master Planned Unit Development (MPUD) feature services and historical zoning records.

---
**Geospatial Analysis, Automation Scripting, and StoryMap Design by Leonard Sala.**
