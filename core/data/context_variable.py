from datetime import datetime

context_variables = {
    "patient_context": {
        "PATIENT_ID": "patient_67890",
        "NAME": "Matheus R.",
        "PHONE_NUMBER": "(987) 999-9999",
        "EMAIL": "matheus@example.com",
        "INSURANCE_STATUS": "Ative",
        "MEDICAL_HISTORY": ["Hypertension", "Penicillin allergy"],
        "LOCATION": "Av. Siempreviva 742, Super City, Best Nation",
    },
    "general_context": {"current_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
}
