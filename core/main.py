from agents import triage_agent
from swarm.repl import run_demo_loop
from tools.switchers import (
    switch_to_availability_agent,
    switch_to_cancellation_agent,
    switch_to_reviews_agent,
)

triage = triage_agent
triage.functions = [
    switch_to_availability_agent,
    switch_to_cancellation_agent,
    switch_to_reviews_agent,
]

if __name__ == "__main__":
    run_demo_loop(triage, debug=False, stream=True)
