import os
from datetime import datetime
from qgis.core import QgsProject

def mpud_audit_notification():
    try:
        # 1. GATHER PROJECT DATA
        path = QgsProject.instance().fileName()
        project_name = os.path.basename(path) if path else "Unsaved_Pasco_Project"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the log entry
        log_entry = f"[{timestamp}] PROJECT: {project_name} | EDITOR: Lenny Sala | STATUS: Save Verified\n"

        # 2. DEFINE THE DYNAMIC DOCUMENTS PATH
        log_dir = os.path.join(os.path.expanduser("~"), "Documents", "GIS_Logs")
        log_file = os.path.join(log_dir, "mpud_audit_trail.txt")

        # 3. CREATE DIRECTORY AND APPEND LOG
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        with open(log_file, "a") as f:
            f.write(log_entry)
        
        # Print confirmation to the QGIS Python Console
        print(f"--- SUCCESS: Audit Log committed to Documents/GIS_Logs ---")
        
    except Exception as e:
        print(f"CRITICAL ERROR in Audit Script: {e}")

def openProject():
    # Connect the save event to our function
    QgsProject.instance().projectSaved.connect(mpud_audit_notification)
    print("SYSTEM STATUS: Governance Module Loaded. Target: Documents/GIS_Logs")

def saveProject():
    pass

def closeProject():
    # Clean up the connection when closing
    try:
        QgsProject.instance().projectSaved.disconnect(mpud_audit_notification)
    except:
        pass