from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPEN_AI_API_KEY"]=os.getenv("OPEN_AI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

# Senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content of the topic{topic} from Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# senior blog writer agent with yt tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from Yt channel',
    verbose=True,
    backstory=(
        "With a flare of simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)
