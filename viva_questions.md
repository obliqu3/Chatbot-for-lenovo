# 🎓 Viva Voce Questions & Answers – Campus Buddy Project

This document compiles the most common viva questions and technical inquiries that evaluators may ask during your project presentation.

---

### Q1: What is the objective of the Campus Buddy Chatbot?
* **Answer:** The primary objective is to create a 24/7 automated information desk for a college campus. It helps students, parents, and visitors find instant, accurate responses regarding college timings, academic departments, library facilities, examinations, admissions, and contact details without needing to navigate complex web pages or visit administrative offices physically.

### Q2: What technology stack did you use, and why?
* **Answer:** We used **Python** and **Streamlit**. Python was chosen because of its robust text-processing ecosystem, clean syntax, and standard libraries. Streamlit was selected because it is a rapid application development framework for python. It allows us to build a responsive, highly interactive web UI with built-in state management (session state) without writing complex React, Vue, or backend REST API code from scratch.

### Q3: Explain the dialogue management or logic flow of your chatbot.
* **Answer:** The chatbot follows a **rule-based, intent-matching logic**:
  1. The user types a query or clicks a sidebar button.
  2. The input is pre-processed (converted to lowercase, trailing spaces removed).
  3. The engine runs it through `match_intent()`, which scans for specific list-based keywords associated with each category (e.g., "hours" or "schedule" matches the `timings` intent).
  4. If a keyword is found, the chatbot fetches the corresponding predefined HTML/Markdown payload.
  5. If no keywords match, the model falls back to a descriptive helper message suggesting possible query categories.
  6. The query and reply are saved in Streamlit's `st.session_state.messages` list to persist the conversation context.

### Q4: How is conversation history maintained in Streamlit since it is stateless?
* **Answer:** Streamlit runs the script from top to bottom on every user interaction. To maintain state, we use **`st.session_state`**. We initialize a key `messages` as a list (`st.session_state.messages = []`) when the app first loads. Every user query and assistant response is appended to this list. In each script execution cycle, we loop through and re-render all messages in this list.

### Q5: What is the purpose of the fallback response, and what does yours contain?
* **Answer:** A fallback response prevents the chatbot from crashing or going silent when it receives a query it doesn't understand. Our fallback response politely notifies the user that the query could not be matched, displays a structured checklist of topics the chatbot is trained on, and guides the user to use the Quick Navigation buttons in the sidebar.

### Q6: How does the sidebar Quick Navigation work?
* **Answer:** The sidebar contains buttons for each primary category. In Streamlit, when a button is clicked, it returns `True` for that run cycle. We capture this event, construct a mock user message, and trigger the corresponding intent handler. This provides an alternative, error-free path for users who prefer clicking menu items rather than typing.

### Q7: How did you implement styling to make the UI look premium?
* **Answer:** Streamlit's default UI was enhanced by injecting custom HTML and CSS via `st.markdown(..., unsafe_allow_html=True)`. We imported the modern font **Plus Jakarta Sans** from Google Fonts, applied dark-themed container styling (`#0d1117`), created glowing gradient borders, custom padding, shadows, and styled table structures for displaying department info.

### Q8: What are the main limitations of this chatbot?
* **Answer:**
  * **No Semantic Understanding:** Because it relies on keyword matching, it cannot understand synonyms or contextually related terms unless they are explicitly defined in the keyword lists.
  * **Static Data:** If information like timings or fees changes, the source code itself must be updated. It doesn't fetch information dynamically from a live database or API.
  * **Limited Context:** It handles single-turn queries and doesn't support complex multi-turn slot filling (e.g., asking "What is the HOD's name?" immediately after asking about CSE without repeating "CSE").

### Q9: How can this chatbot be enhanced in the future?
* **Answer:**
  * **LLM Integration:** Connect the chatbot to a Large Language Model (like Gemini or OpenAI) using Retrieval-Augmented Generation (RAG) to scan the college handbook and answer complex queries.
  * **Dynamic Databases:** Integrate the backend with a PostgreSQL or MongoDB database to fetch student-specific data (e.g., personal exam marks, attendance).
  * **Voice Recognition:** Incorporate Web Speech APIs to allow users to interact via voice commands.
  * **Multi-lingual Support:** Add translation layers to answer queries in regional languages.

### Q10: How do you deploy this application online?
* **Answer:** It is ready for cloud deployment. We can use **Streamlit Community Cloud** by linking a GitHub repository containing `app.py` and `requirements.txt`. The platform automatically provisions a container, installs the requirements, and hosts the app publicly on a `<name>.streamlit.app` subdomain. Alternatively, it can be deployed on **Hugging Face Spaces** or **Render**.
