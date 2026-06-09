# Campus Buddy

Campus Buddy is an interactive, web-based chatbot designed to act as a 24/7 information assistant for college campuses. It provides instant responses to common queries regarding timings, departments, library resources, examinations, admissions, and campus facilities.

The application is built using Python and Streamlit, featuring a fully responsive user interface styled with a modern dark theme.

## Key Features

* **Instant Information Retrieval:** Auto-replies to queries about operating schedules, academic divisions, admissions criteria, library policies, and campus infrastructure.
* **Interactive Control Panel:** A sidebar menu allowing users to navigate and trigger category queries with a single click.
* **Clean Responsive Layout:** A customized dark-mode interface styled with custom CSS and typography (Plus Jakarta Sans).
* **Session-Based State Management:** Stores user queries and responses to maintain persistent chat history during the session.
* **Feedback Mechanics:** Captures ratings and suggestions to measure user experience.

## Project Structure

```text
.
├── app.py                # Main Streamlit Chatbot Application
├── requirements.txt      # Python Dependencies
├── flowchart.mermaid     # System logic flowchart
├── report.md             # Detailed documentation report
├── presentation.md       # Project presentation slides outline
├── viva_questions.md     # Project Q&A guide
└── mockups/              # UI screenshot mockups
```

## Getting Started

### Prerequisites

* Python 3.8 or higher

### Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the local development server:
```bash
streamlit run app.py
```
Once the server starts, it will automatically open the application in your default web browser (typically at `http://localhost:8501`).
