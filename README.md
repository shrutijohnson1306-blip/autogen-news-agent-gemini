#  AI News Agent (AutoGen + Gemini + Google News Tool)

##  Project Overview

This project implements a tool-augmented AI agent that fetches real-time news using Google News and responds conversationally using an LLM (Gemini via AutoGen).

The agent:
- Accepts a news query
- Calls a Google News tool
- Retrieves latest articles
- Formats structured output
- Responds through an LLM-powered assistant

This demonstrates tool integration with LLM-based agents.

---

##  Architecture

User Query  
   ↓  
NewsAssistant (LLM Agent)  
   ↓  
Google News Tool  
   ↓  
Formatted News Output  

---

##  Tech Stack

- Python
- AutoGen Framework
- Gemini (LLM)
- Google News API (via GNews library)
- Environment-based API key configuration

---

