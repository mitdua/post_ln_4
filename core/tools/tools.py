from datetime import datetime, timedelta
from typing import Optional, List, Dict


def check_date_availability(
    date: str, time_slot: Optional[str] = None
) -> Dict[str, bool]:
    """
    Check if a specific date and optional time slot is available

    Args:
        date: Date in YYYY-MM-DD format
        time_slot: Optional time slot in HH:MM format

    Returns:
        Dictionary with availability status
    """
    print(f"🔍 Checking availability for closing: {date}, time: {time_slot}")
    # Mock implementation
    return {"is_available": True}


def get_available_slots(date: str) -> List[str]:
    """
    Get all available time slots for a specific date

    Args:
        date: Date in YYYY-MM-DD format

    Returns:
        List of available time slots in HH:MM format
    """
    print(f"📅 Looking for available times for: {date}")
    # Mock implementation
    slots = ["09:00", "10:00", "11:00", "14:00", "15:00"]
    print(f"✅ You will find {len(slots)} available times")
    return slots


def get_calendar_info(start_date: str, end_date: str) -> Dict[str, List[str]]:
    """
    Get calendar availability for a date range

    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        Dictionary with dates and their available slots
    """
    print(f"📊 Consulting calendar from {start_date} to {end_date}")
    # Mock implementation
    result = {"2024-12-20": ["09:00", "10:00"], "2024-12-21": ["14:00", "15:00"]}
    print(f"📋 Calendar information retrieved for {len(result)} days")
    return result


def get_operating_hours() -> Dict[str, Dict[str, str]]:
    """
    Get business operating hours

    Returns:
        Dictionary with operating hours per day
    """
    print("⏰ Obtaining operating hours")
    # Mock implementation
    print("✨ Operating hours successfully recovered")
    return {
        "monday": {"open": "09:00", "close": "17:00"},
        "tuesday": {"open": "09:00", "close": "17:00"},
        "wednesday": {"open": "09:00", "close": "17:00"},
        "thursday": {"open": "09:00", "close": "17:00"},
        "friday": {"open": "09:00", "close": "16:00"},
    }


def medical_consultation_scheduling(
    date: str,
    time_slot: str,
    contact_info: Dict[str, str],
    speciality: str,
) -> Dict[str, any]:
    """
    Make a medical appointment for a specific date and time

    Args:
        date: Date in YYYY-MM-DD format
        time_slot: Time slot in HH:MM format
        contact_info: Dictionary with contact information (name, email, phone)
        speciality: Medical Speciality
    Returns:
        Dictionary with scheduling details result
    """
    print(f"📝 Processing scheduling for {date} in {time_slot}")
    # Mock implementation
    consultation_reference = (
        f"SCH-{datetime.now().strftime('%Y%m%d')}-{hash(date + time_slot)}"[:12]
    )

    result = {
        "consultation_reference": consultation_reference,
        "status": "confirmed",
        "date": date,
        "time": time_slot,
        "total_price": 50.00,
        "contact_info": contact_info,
        "speciality": speciality,
    }

    print(f"✅ Consultation medical confirmed: {consultation_reference}")
    return result


def get_available_specialties():
    """Check which medical specialties are available in the hospital
    with availability to schedule consultations.
    Returns:
        List with medical specialties.
    """

    return [
        "Internal Medicine",
        "Pediatrics",
        "Gynecology and Obstetrics",
        "Cardiology",
        "Traumatology and Orthopedics",
        "Radiology/Imaging",
        "Clinical Laboratory",
    ]
