import streamlit as st
import datetime

# Configure app page properties
st.set_page_config(
    page_title="Campus Buddy - College Information Chatbot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styles for chat interface and containers
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
    /* Main container and font settings */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0d1117;
        color: #c9d1d9;
    }
    
    /* Header customization */
    .header-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
    }
    
    .header-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .header-subtitle {
        color: #a3b8cc;
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }

    /* Sidebar design */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    .sidebar-title {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    /* Chat bubble styling overrides */
    .stChatMessage {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 12px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stChatMessage:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.2) !important;
        border-color: #58a6ff !important;
    }
    
    /* Custom style for chatbot responses */
    .bot-response {
        line-height: 1.6;
    }
    
    .info-card {
        background: rgba(88, 166, 255, 0.1);
        border-left: 4px solid #58a6ff;
        padding: 1rem;
        border-radius: 4px 8px 8px 4px;
        margin: 0.75rem 0;
    }

    .info-title {
        font-weight: 600;
        color: #58a6ff;
        margin-bottom: 0.5rem;
    }
    
    /* Buttons in sidebar */
    .stButton>button {
        background: linear-gradient(135deg, #1f6feb 0%, #104eab 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #58a6ff 0%, #1f6feb 100%) !important;
        box-shadow: 0 4px 15px rgba(88, 166, 255, 0.4) !important;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# Display header
st.markdown("""
<div class="header-container">
    <div class="header-title">🎓 Campus Buddy</div>
    <div class="header-subtitle">Your 24/7 Smart College Information Assistant</div>
</div>
""", unsafe_allow_html=True)

# Local dataset containing campus details
CAMPUS_INFO = {
    "timings": {
        "title": "🕒 College Timings & Schedule",
        "keywords": ["time", "timing", "timings", "hours", "open", "close", "schedule", "working", "holiday", "saturday", "sunday"],
        "response": """
**Here are the official operating hours for our campus:**
<div class="info-card">
    <div class="info-title">Academic & Administrative Schedule</div>
    <ul>
        <li><b>Regular Classes:</b> Monday to Friday — 9:00 AM to 4:30 PM</li>
        <li><b>Lunch Recess:</b> 12:30 PM to 1:30 PM</li>
        <li><b>Office/Administrative Hours:</b> Monday to Friday — 9:00 AM to 5:00 PM</li>
        <li><b>Saturdays:</b> 9:00 AM to 1:00 PM (Active only on 1st and 3rd Saturdays; 2nd and 4th Saturdays are holidays)</li>
        <li><b>Sundays & Public Holidays:</b> Campus remains completely closed.</li>
    </ul>
</div>
        """
    },
    "departments": {
        "title": "🏢 Academic Departments",
        "keywords": ["dept", "department", "departments", "branch", "branches", "course", "courses", "cse", "it", "ece", "eee", "civil", "mechanical", "engineering"],
        "response": """
**We offer several highly-rated undergraduate and postgraduate engineering branches:**
<div class="info-card">
    <div class="info-title">Offered Engineering Disciplines (B.Tech / M.Tech)</div>
    <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
        <tr style="border-bottom: 2px solid #30363d; text-align: left;">
            <th style="padding: 8px;">Department Name</th>
            <th style="padding: 8px;">Intake Capacity</th>
            <th style="padding: 8px;">Head of Department (HOD)</th>
        </tr>
        <tr style="border-bottom: 1px solid #21262d;">
            <td style="padding: 8px;">💻 Computer Science & Engineering (CSE)</td>
            <td style="padding: 8px;">180 Seats</td>
            <td style="padding: 8px;">Dr. A. K. Sharma</td>
        </tr>
        <tr style="border-bottom: 1px solid #21262d;">
            <td style="padding: 8px;">🌐 Information Technology (IT)</td>
            <td style="padding: 8px;">120 Seats</td>
            <td style="padding: 8px;">Dr. R. S. Verma</td>
        </tr>
        <tr style="border-bottom: 1px solid #21262d;">
            <td style="padding: 8px;">📡 Electronics & Communication (ECE)</td>
            <td style="padding: 8px;">120 Seats</td>
            <td style="padding: 8px;">Dr. P. C. Joshi</td>
        </tr>
        <tr style="border-bottom: 1px solid #21262d;">
            <td style="padding: 8px;">⚡ Electrical & Electronics (EEE)</td>
            <td style="padding: 8px;">60 Seats</td>
            <td style="padding: 8px;">Dr. V. K. Singh</td>
        </tr>
        <tr style="border-bottom: 1px solid #21262d;">
            <td style="padding: 8px;">⚙️ Mechanical Engineering (ME)</td>
            <td style="padding: 8px;">60 Seats</td>
            <td style="padding: 8px;">Dr. S. K. Gupta</td>
        </tr>
        <tr>
            <td style="padding: 8px;">🏗️ Civil Engineering (CE)</td>
            <td style="padding: 8px;">60 Seats</td>
            <td style="padding: 8px;">Dr. M. L. Mehta</td>
        </tr>
    </table>
</div>
        """
    },
    "library": {
        "title": "📚 Central Library Facilities",
        "keywords": ["library", "libraries", "book", "books", "journal", "journals", "read", "reading", "borrow", "card", "ieee"],
        "response": """
**Our Central Library is a state-of-the-art information and resource center:**
<div class="info-card">
    <div class="info-title">Library Timings & Policies</div>
    <ul>
        <li><b>Operating Hours:</b> Monday to Saturday — 8:00 AM to 8:00 PM</li>
        <li><b>Digital Library Access:</b> Open 24/7 via the campus intranet student portal.</li>
        <li><b>Resources:</b> Over 52,000 physical volumes, 150 print journals, and online access to IEEE, Springer, and ScienceDirect databases.</li>
        <li><b>Borrowing Guidelines:</b>
            <ul>
                <li>UG Students: Up to 4 books for 14 days.</li>
                <li>PG Students: Up to 6 books for 21 days.</li>
                <li>Fine for late return: ₹5 per day per book.</li>
            </ul>
        </li>
    </ul>
</div>
        """
    },
    "exams": {
        "title": "📝 Examination Cell & Results",
        "keywords": ["exam", "exams", "examination", "examinations", "test", "tests", "midterm", "mid-term", "result", "results", "hall ticket", "admit card", "coe"],
        "response": """
**Information from the Office of the Controller of Examinations (CoE):**
<div class="info-card">
    <div class="info-title">Academic Examination Schedule</div>
    <ul>
        <li><b>Mid-Semester Examinations:</b> Conducted twice per semester (Mid-Sem I in Week 6, Mid-Sem II in Week 12).</li>
        <li><b>End-Semester Practical & Theory Exams:</b> 
            <ul>
                <li>Odd Semester: November / December</li>
                <li>Even Semester: April / May</li>
            </ul>
        </li>
        <li><b>Exam Cell Contact:</b> Email: <a href="mailto:coe@college.edu" style="color:#58a6ff;">coe@college.edu</a> | Extension No. 104</li>
        <li><b>Important Portals:</b> Students can register for exams, download hall tickets, and view grades via the official Student ERP Portal.</li>
    </ul>
</div>
        """
    },
    "contact": {
        "title": "📞 Contact Details & Address",
        "keywords": ["contact", "contacts", "phone", "number", "numbers", "email", "emails", "address", "call", "location", "reach", "map", "helpline"],
        "response": """
**Get in touch with the college administration:**
<div class="info-card">
    <div class="info-title">Contact & Location Info</div>
    <ul>
        <li><b>Main Campus Address:</b> Engineering College Road, Tech Park District, Sector-5, City - 560001.</li>
        <li><b>General Administrative Helpline:</b> +91-11-22334455 / +91-11-22334456</li>
        <li><b>Admission Support Line:</b> +91-9988776655 | Toll-Free: 1800-123-4567</li>
        <li><b>General Inquiry Email:</b> <a href="mailto:info@college.edu" style="color:#58a6ff;">info@college.edu</a></li>
        <li><b>Admissions Helpdesk:</b> <a href="mailto:admissions@college.edu" style="color:#58a6ff;">admissions@college.edu</a></li>
    </ul>
</div>
        """
    },
    "admissions": {
        "title": "🎓 Admissions & Fee Structure",
        "keywords": ["admission", "admissions", "fee", "fees", "join", "eligibility", "apply", "criteria", "quota", "seat", "cost", "scholarship"],
        "response": """
**Join our upcoming academic batch! Here is what you need to know about the admissions process:**
<div class="info-card">
    <div class="info-title">Eligibility Criteria</div>
    <ul>
        <li>Completion of 10+2 (Higher Secondary) with Physics, Chemistry, and Mathematics.</li>
        <li>Minimum of 50% aggregate marks in PCM (45% for reserved categories).</li>
        <li>Valid scorecard from State Joint Entrance Exam (JEE) or National level exam.</li>
    </ul>
</div>
<div class="info-card">
    <div class="info-title">Annual Tuition Fees (Approx.)</div>
    <ul>
        <li><b>State Quota (Merit List):</b> ₹1,25,000 per annum</li>
        <li><b>All-India/JEE Quota:</b> ₹1,80,000 per annum</li>
        <li><b>Management Quota:</b> ₹2,50,000 per annum</li>
        <li><i>Note: Hostel, mess, and transportation fees are calculated separately. Scholarships available for merit holders and economically weak students.</i></li>
    </ul>
</div>
        """
    },
    "facilities": {
        "title": "🏗️ Campus Infrastructure & Facilities",
        "keywords": ["facility", "facilities", "hostel", "hostels", "canteen", "mess", "bus", "buses", "transport", "sports", "gym", "medical", "wi-fi", "wifi", "infrastructure"],
        "response": """
**Our college boasts a vibrant, self-contained 50-acre green campus with top-tier amenities:**
<div class="info-card">
    <div class="info-title">Key Campus Amenities</div>
    <ul>
        <li><b>Hostel Accommodation:</b> Separate, multi-story hostels for boys and girls. Equipped with Wi-Fi, modern kitchens, 24/7 security, power backup, and indoor games.</li>
        <li><b>Cafeteria & Dining:</b> Central, hygienic food court serving multi-cuisine meals and snacks at subsidized student rates.</li>
        <li><b>Sports Complex:</b> Full-sized football turf, cricket pitch, basketball court, indoor badminton courts, and a fully equipped gymnasium.</li>
        <li><b>Transport Network:</b> Fleet of 25 air-conditioned buses running routes across the entire city and nearby suburbs.</li>
        <li><b>Medical Support:</b> 24/7 healthcare center on campus with a resident doctor and dedicated ambulance.</li>
        <li><b>Connectivity:</b> High-speed 100 Mbps Wi-Fi connectivity throughout classrooms, labs, and hostels.</li>
    </ul>
</div>
        """
    }
}

# Helper to match user text queries against dataset keywords
def match_intent(user_query):
    query_lower = user_query.lower().strip()
    
    # Check for direct keyword matches
    for key, content in CAMPUS_INFO.items():
        for keyword in content["keywords"]:
            if keyword in query_lower:
                return key
                
    # Fallback to general greeting or help if query is empty or too generic
    greetings = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening", "supp", "yo"]
    if any(g in query_lower.split() for g in greetings):
        return "greeting"
        
    return None

# Render sidebar components
with st.sidebar:
    st.markdown('<div class="sidebar-title">🎓 Control Panel</div>', unsafe_allow_html=True)
    
    st.markdown("### Quick Navigation Menu")
    st.write("Click any topic below to query the chatbot instantly:")
    
    col1, col2 = st.columns(2)
    with col1:
        btn_timings = st.button("🕒 Timings")
        btn_library = st.button("📚 Library")
        btn_contact = st.button("📞 Contacts")
    with col2:
        btn_depts = st.button("🏢 Departments")
        btn_exams = st.button("📝 Exams")
        btn_admissions = st.button("🎓 Admissions")
        
    btn_facilities = st.button("🏗️ Campus Facilities")
    
    st.markdown("---")
    
    # Feedback form
    st.markdown("### 💬 Session Feedback")
    feedback_rating = st.slider("Rate your conversation:", 1, 5, 5)
    feedback_text = st.text_area("Suggestions / Comments:", placeholder="Help us improve Campus Buddy...")
    if st.button("Submit Feedback"):
        st.success("Thank you for your valuable feedback!")
        
    st.markdown("---")
    
    # Clear conversation history
    if st.button("🧹 Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Initialize state array
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render welcome message on first load
if len(st.session_state.messages) == 0:
    welcome_text = """
    👋 Hello! I am **Campus Buddy**, your virtual campus guide. 
    
    I can assist you with quick information about our engineering college. Ask me anything about:
    * **College Timings & Office Hours**
    * **Academic Departments & Courses**
    * **Central Library Resources**
    * **Examination Schedules & Results**
    * **Admissions Eligibility & Fee Structure**
    * **Campus Facilities (Hostel, Transport, Gym, etc.)**
    * **Contact Numbers & Campus Location**
    
    Feel free to type your question below or click one of the quick buttons in the sidebar menu!
    """
    st.session_state.messages.append({"role": "assistant", "content": welcome_text})

# Sidebar action handler
clicked_intent = None
if btn_timings:
    clicked_intent = "timings"
elif btn_depts:
    clicked_intent = "departments"
elif btn_library:
    clicked_intent = "library"
elif btn_exams:
    clicked_intent = "exams"
elif btn_contact:
    clicked_intent = "contact"
elif btn_admissions:
    clicked_intent = "admissions"
elif btn_facilities:
    clicked_intent = "facilities"

if clicked_intent:
    user_msg = f"Tell me about {CAMPUS_INFO[clicked_intent]['title']}"
    st.session_state.messages.append({"role": "user", "content": user_msg})
    
    bot_ans = CAMPUS_INFO[clicked_intent]["response"]
    st.session_state.messages.append({"role": "assistant", "content": bot_ans})

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Input box for user queries
if not clicked_intent:
    user_input = st.chat_input("Ask a question about the college...")
    
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        intent = match_intent(user_input)
        
        with st.chat_message("assistant"):
            if intent == "greeting":
                reply = """
                👋 **Hello there!** How can I assist you today? 
                
                You can ask me questions about timings, library services, departments, exams, admissions, campus facilities, or contact info.
                """
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
            elif intent in CAMPUS_INFO:
                reply = CAMPUS_INFO[intent]["response"]
                st.markdown(reply, unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
            else:
                # Fallback response
                fallback_reply = """
                🕵️‍♂️ **I'm sorry, I couldn't find a direct match for your query.**
                
                To help you best, here is what I am trained to answer:
                1. 🕒 **College Timings:** Office and class schedules.
                2. 🏢 **Departments:** Available academic branches and HOD details.
                3. 📚 **Library:** Library timings, book counts, and borrowing rules.
                4. 📝 **Examinations:** Mid-term and end-term exam calendars.
                5. 🎓 **Admissions:** Fee details and eligibility criteria.
                6. 🏗️ **Facilities:** Hostel, cafeteria, transport, and Wi-Fi.
                7. 📞 **Contact:** Phone numbers, email addresses, and location map.
                
                *Please try rephrasing your question or select one of the Quick Navigation buttons in the sidebar!*
                """
                st.markdown(fallback_reply)
                st.session_state.messages.append({"role": "assistant", "content": fallback_reply})
