from agents.get_agents import get_search_agent, get_gmail_agent
from dotenv import load_dotenv

from utils.callbacks import LLMInstrumentationHandler

load_dotenv()
if __name__ == "__main__":
    pass


def sdr_spy(full_name: str, verbose: bool = False) -> str:
    spy_agent = get_search_agent()
    person_summary = spy_agent.run(
        f"1. Search on google {full_name}'s Linkedin profile"
        f"2. Summarize {full_name}'s linkedin information to 2 sentences",
        callbacks=[LLMInstrumentationHandler()] if verbose else [],
    )
    return person_summary


def sdr_email(
    full_name: str, person_summary: str, topic: str, verbose: bool = False
) -> None:
    email_agent = get_gmail_agent()
    email_agent.run(
        f"You are a super funny SDR that uses a lot of 'bro' when you write. I want you to:"
        f"Write a 1 line draft email to {full_name},"
        f"pitching {topic} based solely on {full_name}'s {person_summary} information summary",
        callbacks=[LLMInstrumentationHandler()] if verbose else [],
    )


def sdr_start(full_name: str, topic: str, verbose: bool = True):
    person_summary = sdr_spy(full_name=full_name, verbose=verbose)
    print(person_summary)
    sdr_email(
        full_name=full_name, person_summary=person_summary, topic=topic, verbose=verbose
    )
