# 🚀 AI-Powered Resume & Job Description Skill Matcher

A lightweight AI-powered system that extracts skills from resumes and job descriptions, compares them using keyword matching + LLM-powered skill classification, and outputs:

- Match Score (%)
- Matched Keywords
- Missing Keywords
- Extra Keywords in Resume

This project is designed to be **easy to deploy**, **LLM-agnostic**, and **GitHub-friendly** (works with OpenAI, Groq, DeepSeek, TogetherAI, or local LLaMA).

---

## ✨ Features

- 🔍 Extracts skills from resumes & JDs  
- 🤖 AI-powered skill expansion (optional)  
- 🔑 Supports ANY OpenAI-compatible API (OpenAI/Groq/DeepSeek/TogetherAI)  
- 🧠 Custom skill database (`skills.db`)  
- 🎯 Returns structured output:
  ```json
  {
    "match_score": 82.5,
    "matched_keywords": [...],
    "missing_keywords": [...],
    "extra_keywords": [...]
  }
