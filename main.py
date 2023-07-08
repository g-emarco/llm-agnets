from agents.get_agents import get_search_agent, get_gmail_agent
from dotenv import load_dotenv

from utils.callbacks import LLMInstrumentationHandler

load_dotenv()

if __name__ == "__main__":
    agent = get_search_agent()
    full_name1 = "Bastien Legras"
    full_name2 = "Avi Shitrit"

    # res = agent.run(
    #     f"You are CoinMaster Developer by Moonactive,"
    #     f"In the game, every new village is themed differently, from Stone Age and Sunny Hawaii to Snowy Alps."
    #     f"A custom village is a tailor made village based on the {full_name}'s Linkedin profile page."
    #     f" search for it and create a custom village based on the {full_name}'s Linkedin title and summary."
    #     "example 1: if the user is a developer the village should contain computers and hoodies"
    #     "example 2: if the user is a product manager the village should contain lots of tickets, GANTs and Todo Lists"
    #     f"Your result should be an elaborate description of what the village looks and feels like",
    #     callbacks=[LLMInstrumentationHandler()],
    # )

    # full_name1 = "Bastien Legras"
    # full_name2 = "Avi Shitrit"
    full_name1 = "Eden Marco"
    # res = agent.run(
    #     f"what is the relation between {full_name1} and {full_name2}",
    #     callbacks=[LLMInstrumentationHandler()],
    # )

    linkedin_info = agent.run(
        f"1. Search on google {full_name1}'s Linkedin profile"
        f"2. Summarize {full_name1}'s linkedin information to 2 sentences",
        callbacks=[LLMInstrumentationHandler()],
    )

    agent2 = get_gmail_agent()
    pitch_chain = agent2.run(
        f"You are a super funny BDR that uses a lot of 'bro' when you write. I want you to:"
        f"Write a 1 line draft email to {full_name1},"
        f"pitching Google PaLM 2 based on his {linkedin_info} information summary",
        callbacks=[LLMInstrumentationHandler()],
    )


def sdr_spy(full_name: str) -> str:
    spy_agent = get_search_agent()
    person_summary = spy_agent.run(
        f"1. Search on google {full_name}'s Linkedin profile"
        f"2. Summarize {full_name}'s linkedin information to 2 sentences",
        callbacks=[LLMInstrumentationHandler()],
    )
    return person_summary


def sdr_email(full_name: str, person_summary: str, topic: str) -> None:
    email_agent = get_gmail_agent()
    email_agent.run(
        f"You are a super funny SDR that uses a lot of 'bro' when you write. I want you to:"
        f"Write a 1 line draft email to {full_name},"
        f"pitching {topic} based solely on {full_name}'s {person_summary} information summary",
        callbacks=[LLMInstrumentationHandler()],
    )


def sdr_start(full_name: str, topic: str):
    person_summary = sdr_spy(full_name=full_name)
    sdr_email(full_name=full_name, person_summary=person_summary, topic=topic)
