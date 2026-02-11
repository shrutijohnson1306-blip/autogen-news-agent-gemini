import os
from dotenv import load_dotenv
from gnews import GNews
import autogen

# ---------------- ENV ---------------- #
load_dotenv()
assert os.getenv("GOOGLE_API_KEY"), "GOOGLE_API_KEY missing"

# ---------------- TOOL ---------------- #

def get_google_news(query: str) -> str:
    google_news = GNews(language="en", country="IN", max_results=5)
    articles = google_news.get_news(query)

    if not articles:
        return "No news found."

    out = ["📰 Latest News:\n"]
    for a in articles:
        out.append(
            f"- {a['title']}\n"
            f"  Source: {a['publisher']['title']}\n"
            f"  Link: {a['url']}\n"
        )
    return "\n".join(out)

# ---------------- LLM CONFIG ---------------- #

llm_config = {
    "config_list": [
        {
            "model": "models/gemini-2.5-flash",
            "api_type": "google",
            "api_key": os.getenv("GOOGLE_API_KEY"),
        }
    ],
    "temperature": 0,
}

# ---------------- AGENTS ---------------- #

assistant = autogen.AssistantAgent(
    name="NewsAssistant",
    llm_config=llm_config,
    system_message="""
You are a news assistant.
You will receive news text and must present it clearly.
Do not call tools yourself.
""",
)

user = autogen.UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    code_execution_config=False,
)

# ---------------- RUN ---------------- #

print("🗞️ News Agent(type 'exit' to quit)\n")

while True:
    query = input("You > ")
    if query.lower() == "exit":
        break

    # 🔑 TOOL EXECUTION 
    news_text = get_google_news(query)

    # 🔑 LLM FORMATTING / AGENT RESPONSE
    user.initiate_chat(
        assistant,
        message=f"Here is the latest news:\n\n{news_text}",
        max_turns=1
    )
