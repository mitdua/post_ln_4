from swarm import Agent
from data.context_variable import context_variables
from prompts import *
from tools.tools import *

triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions(context_variables),
    functions=[],
)

availability_agent = Agent(
    name="Availability Agent",
    instructions=availability_instructions(context_variables),
    functions=[
        get_available_specialties,
        medical_consultation_scheduling,
        get_operating_hours,
        get_calendar_info,
        get_available_slots,
        check_date_availability,
    ],
)

cancellation_agent = Agent(
    name="Cancellation Agent",
    instructions=cancellation_instructions(context_variables),
    functions=[],
)

reviews_agent = Agent(
    name="Review Agent",
    instructions=reviews_instructions(context_variables),
    functions=[],
)
