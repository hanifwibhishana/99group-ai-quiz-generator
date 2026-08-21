# 🏢 99 Group: AI Quiz Generation System

An end-to-end, automated AI Quiz Generation System designed to train and evaluate 99 Group property agents. This project is submitted as part of the AI Engineer technical assessment.

## 🚀 Project Overview
This application leverages Large Language Models (LLMs) to dynamically generate factual, industry-relevant multiple-choice quizzes based on any real estate topic. To ensure enterprise-grade reliability and prevent AI hallucinations, the system incorporates three core AI engineering paradigms:
1. **Search-Augmented Generation (Web-RAG)**
2. **LLM-as-a-Judge (Automated Quality Assurance)**
3. **Human-in-the-Loop (Admin Approval Workflow)**

---

## 🧠 System Architecture & Workflow

Below is the high-level workflow of the system when generating a quiz:

```text
[User/Admin] --> Enters Topic (e.g., "KPR Interest Rates 2026")
       |
       v
[Tavily Search API] --> Scrapes real-time web context regarding the topic.
       |
       v
[Groq API: Generator] --> Ingests scraped context + System Prompt to generate JSON Quiz.
       |
       v
[Groq API: Evaluator] --> (LLM-as-a-Judge) Cross-references the generated JSON against the 
       |                  Tavily source text to strictly flag any hallucinations.
       v
[Admin Dashboard] --> HR reviews the draft, reads the AI Judge feedback, and edits if necessary.
       |
       v
[Local JSON DB] <--- Saves the quiz as "Published".
       |
       v
[User Dashboard] <--- Agents access and complete the live quiz.