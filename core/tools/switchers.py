from agents import availability_agent, cancellation_agent, reviews_agent


def switch_to_availability_agent():
    return availability_agent


def switch_to_cancellation_agent():
    return cancellation_agent


def switch_to_reviews_agent():
    return reviews_agent
