# create_excel.py
import pandas as pd

def create_excel():
    medicines = {
        "Medicine": [
            "Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine",
            "Azithromycin", "Metformin", "Aspirin", "Omeprazole",
            "Prednisolone", "Vitamin C"
        ],
        "Dosage": [
            "500mg", "400mg", "250mg", "10mg",
            "500mg", "850mg", "75mg", "20mg",
            "5mg", "500mg"
        ]
    }

    df = pd.DataFrame(medicines)
    df.to_excel("medicines.xlsx", index=False)
    print("Excel file created successfully: medicines.xlsx")

if __name__ == "__main__":
    create_excel()
