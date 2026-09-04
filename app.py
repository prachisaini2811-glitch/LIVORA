import streamlit as st
from datetime import datetime, timedelta
import time

# ============================================================
# LIVORA — Live Better. Study Smarter.
# First Working Version
# ============================================================

st.set_page_config(
    page_title="LIVORA",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CUSTOM CSS ----------------------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8fbf7, #f7f3fb);
    }

    .main-title {
        font-size: 55px;
        font-weight: 800;
        margin-bottom: 0;
        color: #39483f;
    }

    .subtitle {
        font-size: 20px;
        color: #69756d;
        margin-bottom: 25px;
    }

    .card {
        background: rgba(255,255,255,0.82);
        padding: 24px;
        border-radius: 22px;
        box-shadow: 0 8px 25px rgba(80,80,80,0.08);
        margin-bottom: 18px;
        border: 1px solid rgba(130,130,130,0.08);
    }

    .card h3 {
        color: #46584c;
    }

    .big-number {
        font-size: 34px;
        font-weight: 700;
        color: #52695a;
    }

    .small-text {
        color: #758078;
    }

    .pill {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 20px;
        background: #ebe5f5;
        color: #5b4c70;
        margin: 4px;
    }

    .quote {
        padding: 25px;
        border-radius: 20px;
        background: #eee9f7;
        font-size: 20px;
        color: #514b5c;
        text-align: center;
    }

    footer {
        text-align: center;
        padding: 30px;
        color: #7a817d;
    }
</style>
""", unsafe_allow_html=True)


# -------------------- SESSION STATE --------------------------

defaults = {
    "water": 0,
    "water_target": 8,
    "tasks": [],
    "reminders": [],
    "mood": "Not selected",
    "study_minutes": 0,
    "movement": 0,
    "focus_running": False,
    "focus_seconds": 25 * 60,
    "notes": "",
    "profile_name": "Student",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------- SIDEBAR -------------------------------

st.sidebar.markdown("# 🌿 LIVORA")
st.sidebar.caption("Live Better. Study Smarter.")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📚 Study Hub",
        "⏱️ Focus Timer",
        "📅 Timetable Maker",
        "📝 Notes & Resources",
        "🧠 Mind Maps",
        "❓ Important Questions",
        "📝 Exam Preparation",
        "🧘 Yoga",
        "🏃 Movement",
        "😊 Well-being",
        "💧 Wellness",
        "🔔 Smart Reminders",
        "⚙️ Settings"
    ]
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">LIVORA 🌿</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Live Better. Study Smarter.</div>',
        unsafe_allow_html=True
    )

    st.write(f"### Good morning, {st.session_state.profile_name}! 👋")

    st.markdown("""
    <div class="quote">
    ✨ Small steps every day can make studying and daily life feel much easier.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Dashboard
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>💧 Water</h3>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="big-number">{st.session_state.water}/{st.session_state.water_target}</div>',
            unsafe_allow_html=True
        )

        st.progress(
            min(
                st.session_state.water /
                max(st.session_state.water_target, 1),
                1.0
            )
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>📚 Study</h3>
        """, unsafe_allow_html=True)

        hours = st.session_state.study_minutes // 60
        minutes = st.session_state.study_minutes % 60

        st.markdown(
            f'<div class="big-number">{hours}h {minutes}m</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>🏃 Movement</h3>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="big-number">{st.session_state.movement}</div>',
            unsafe_allow_html=True
        )

        st.caption("Movement breaks")

        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
        <h3>😊 Mood</h3>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="big-number">{st.session_state.mood}</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("⚡ Quick Actions")

    q1, q2, q3, q4 = st.columns(4)

    with q1:
        if st.button("📚 Start Studying", use_container_width=True):
            st.session_state.focus_seconds = 25 * 60
            st.session_state.focus_running = False
            st.success("Focus session prepared! Go to Focus Timer.")

    with q2:
        if st.button("📅 Make Timetable", use_container_width=True):
            st.info("Open Timetable Maker from the sidebar.")

    with q3:
        if st.button("💧 Add Water", use_container_width=True):
            st.session_state.water += 1
            st.rerun()

    with q4:
        if st.button("🧘 Take a Break", use_container_width=True):
            st.session_state.movement += 1
            st.success("Break recorded! 🌿")

    st.subheader("🌱 Today's Focus")

    focus_items = [
        "Complete one important study task",
        "Take regular movement breaks",
        "Drink water according to your personal needs",
        "Give yourself some quiet time"
    ]

    for item in focus_items:
        st.markdown(f"• {item}")

    st.markdown("""
    <footer>
    Designed by Dixa ✨
    </footer>
    """, unsafe_allow_html=True)


# ============================================================
# STUDY HUB
# ============================================================

elif page == "📚 Study Hub":

    st.title("📚 Study Hub")

    st.write(
        "Simple study techniques to help you learn, revise and remember."
    )

    techniques = {
        "🧠 Active Recall":
            "Close your book and try to explain the topic from memory.",

        "🔁 Spaced Revision":
            "Review important material again after increasing time gaps.",

        "✍️ Better Notes":
            "Use headings, keywords, short explanations and examples.",

        "🎯 One Task at a Time":
            "Choose one clear task instead of trying to study everything together.",

        "📖 Teach the Topic":
            "Explain a concept in your own words as if you were teaching someone.",

        "🔕 Reduce Distractions":
            "Keep unnecessary notifications and distracting tabs away during study."
    }

    for title, description in techniques.items():
        st.markdown(
            f"""
            <div class="card">
            <h3>{title}</h3>
            <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOCUS TIMER
# ============================================================

elif page == "⏱️ Focus Timer":

    st.title("⏱️ Focus Timer")

    st.write("Use a simple focus session and take breaks between sessions.")

    duration = st.selectbox(
        "Choose session length",
        [15, 25, 30, 45, 60]
    )

    if st.button("▶️ Start New Session"):
        st.session_state.focus_seconds = duration * 60
        st.session_state.focus_running = True

    minutes = st.session_state.focus_seconds // 60
    seconds = st.session_state.focus_seconds % 60

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
        <div style="font-size:65px;font-weight:700;">
        {minutes:02d}:{seconds:02d}
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.focus_running:

        if st.session_state.focus_seconds > 0:
            time.sleep(1)
            st.session_state.focus_seconds -= 1
            st.rerun()
        else:
            st.session_state.focus_running = False
            st.session_state.study_minutes += duration
            st.balloons()
            st.success("Focus session complete! 🎉")

    if st.button("⏸️ Pause"):
        st.session_state.focus_running = False
        st.rerun()

    if st.button("🔄 Reset"):
        st.session_state.focus_running = False
        st.session_state.focus_seconds = duration * 60
        st.rerun()

    st.subheader("✅ Today's Tasks")

    task = st.text_input("Add a study task")

    if st.button("Add Task"):
        if task.strip():
            st.session_state.tasks.append({
                "task": task,
                "done": False
            })
            st.success("Task added!")

    for i, item in enumerate(st.session_state.tasks):

        checked = st.checkbox(
            item["task"],
            value=item["done"],
            key=f"task_{i}"
        )

        st.session_state.tasks[i]["done"] = checked


# ============================================================
# TIMETABLE
# ============================================================

elif page == "📅 Timetable Maker":

    st.title("📅 Timetable Maker")

    st.write(
        "Create a simple study plan based on your available time."
    )

    subjects_text = st.text_area(
        "Enter your subjects",
        "Accountancy\nBusiness Studies\nEconomics\nEnglish"
    )

    start_time = st.time_input(
        "Study starts at"
    )

    hours = st.number_input(
        "Available study hours",
        min_value=1,
        max_value=12,
        value=4
    )

    break_time = st.number_input(
        "Break after each session (minutes)",
        min_value=5,
        max_value=60,
        value=10
    )

    session_length = st.number_input(
        "Study session length (minutes)",
        min_value=15,
        max_value=120,
        value=45
    )

    if st.button("✨ Generate Timetable"):

        subjects = [
            x.strip()
            for x in subjects_text.split("\n")
            if x.strip()
        ]

        if not subjects:
            st.warning("Please enter at least one subject.")
        else:

            total_minutes = hours * 60
            current = datetime.combine(
                datetime.today(),
                start_time
            )

            timetable = []

            subject_index = 0

            while total_minutes >= session_length:

                subject = subjects[
                    subject_index % len(subjects)
                ]

                end = current + timedelta(
                    minutes=session_length
                )

                timetable.append(
                    (
                        current.strftime("%I:%M %p"),
                        end.strftime("%I:%M %p"),
                        subject
                    )
                )

                current = end + timedelta(
                    minutes=break_time
                )

                total_minutes -= (
                    session_length + break_time
                )

                subject_index += 1

            st.subheader("Your Timetable")

            for start, end, subject in timetable:
                st.markdown(
                    f"""
                    <div class="card">
                    <b>{start} – {end}</b>
                    <br>
                    📚 {subject}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# NOTES & RESOURCES
# ============================================================

elif page == "📝 Notes & Resources":

    st.title("📝 Notes & Resources")

    class_level = st.selectbox(
        "Class",
        ["8", "9", "10", "11", "12"]
    )

    subjects = {
        "8": ["Mathematics", "Science", "English", "Social Science"],
        "9": ["Mathematics", "Science", "English", "Social Science"],
        "10": ["Mathematics", "Science", "English", "Social Science"],
        "11": [
            "Accountancy",
            "Business Studies",
            "Economics",
            "Applied Mathematics",
            "English",
            "IP"
        ],
        "12": [
            "Accountancy",
            "Business Studies",
            "Economics",
            "Applied Mathematics",
            "English",
            "IP"
        ]
    }

    subject = st.selectbox(
        "Subject",
        subjects[class_level]
    )

    st.markdown(
        f"""
        <div class="card">
        <h3>📖 {class_level} — {subject}</h3>
        <p>
        Add your own notes and revision material here.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    user_notes = st.text_area(
        "Write your notes",
        value=st.session_state.notes,
        height=250
    )

    if st.button("💾 Save Notes"):
        st.session_state.notes = user_notes
        st.success("Notes saved for this session! 💚")


# ============================================================
# MIND MAPS
# ============================================================

elif page == "🧠 Mind Maps":

    st.title("🧠 Mind Maps")

    st.write(
        "Create a simple text-based mind map for revision."
    )

    subject = st.text_input(
        "Subject",
        "Business Studies"
    )

    chapter = st.text_input(
        "Chapter",
        "Business Services"
    )

    main_topic = st.text_input(
        "Main Topic",
        chapter
    )

    branches = st.text_area(
        "Enter branches — one per line",
        "Meaning\nTypes\nFunctions\nAdvantages\nLimitations"
    )

    if st.button("🌿 Create Mind Map"):

        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
            <h2>🌿 {main_topic}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        cols = st.columns(3)

        branch_list = [
            x.strip()
            for x in branches.split("\n")
            if x.strip()
        ]

        for i, branch in enumerate(branch_list):
            with cols[i % 3]:
                st.markdown(
                    f"""
                    <div class="card">
                    <h3>🌱 {branch}</h3>
                    <p>Add key points here.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# IMPORTANT QUESTIONS
# ============================================================

elif page == "❓ Important Questions":

    st.title("❓ Important Questions")

    st.caption(
        "These are practice questions. They are not a guarantee of what "
        "will appear in an exam."
    )

    class_level = st.selectbox(
        "Class",
        ["8", "9", "10", "11", "12"]
    )

    subject = st.text_input(
        "Subject",
        "Business Studies"
    )

    chapter = st.text_input(
        "Chapter",
        "Business Services"
    )

    question_type = st.selectbox(
        "Question Type",
        [
            "Very Short Answer",
            "Short Answer",
            "Long Answer",
            "Application Based",
            "Case Based"
        ]
    )

    if st.button("🔎 Show Practice Questions"):

        questions = [
            f"Define the main concept of {chapter}.",
            f"Explain two important features of {chapter}.",
            f"Why is {chapter} important?",
            f"Give suitable examples related to {chapter}.",
            f"Explain the advantages and limitations of the topic."
        ]

        for i, question in enumerate(questions, 1):
            st.markdown(
                f"""
                <div class="card">
                <b>Q{i}.</b> {question}
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# EXAM PREPARATION
# ============================================================

elif page == "📝 Exam Preparation":

    st.title("📝 Exam Preparation")

    exam_date = st.date_input(
        "Exam Date"
    )

    today = datetime.now().date()
    days_left = (exam_date - today).days

    if days_left > 0:
        st.success(
            f"📅 {days_left} days remaining!"
        )
    elif days_left == 0:
        st.warning("Your exam is today!")
    else:
        st.info("That exam date has passed.")

    st.subheader("✅ Revision Checklist")

    chapters = st.text_area(
        "Enter chapters — one per line",
        "Chapter 1\nChapter 2\nChapter 3"
    )

    for i, chapter in enumerate(chapters.split("\n")):
        if chapter.strip():
            st.checkbox(
                chapter.strip(),
                key=f"chapter_{i}"
            )

    st.subheader("🎯 Daily Goal")

    goal = st.text_input(
        "Today's study goal"
    )

    if st.button("Save Goal"):
        if goal:
            st.success(f"Goal saved: {goal}")


# ============================================================
# YOGA
# ============================================================

elif page == "🧘 Yoga":

    st.title("🧘 Yoga Library")

    st.write(
        "Gentle, beginner-friendly movements for stretching, "
        "relaxation and taking a study break."
    )

    filter_option = st.selectbox(
        "Choose a category",
        [
            "All",
            "Morning",
            "Relaxation",
            "Stretch",
            "Balance",
            "Before Sleep"
        ]
    )

    yoga = [
        ("Mountain Pose", "Standing posture for gentle body awareness.",
         "Morning", "30 seconds"),

        ("Child's Pose", "A comfortable resting and stretching position.",
         "Relaxation", "30–60 seconds"),

        ("Cat-Cow", "Gentle movement for the back and spine.",
         "Stretch", "5–8 slow cycles"),

        ("Downward Dog", "A full-body gentle stretch.",
         "Stretch", "20–30 seconds"),

        ("Tree Pose", "A simple balance exercise.",
         "Balance", "20 seconds each side"),

        ("Butterfly Pose", "A gentle seated stretch.",
         "Stretch", "30 seconds"),

        ("Legs-Up-the-Wall", "A quiet relaxation position.",
         "Before Sleep", "2–5 minutes"),

        ("Easy Seated Pose", "Comfortable position for breathing.",
         "Relaxation", "1–2 minutes")
    ]

    for name, description, category, duration in yoga:

        if filter_option != "All" and category != filter_option:
            continue

        st.markdown(
            f"""
            <div class="card">
            <h3>🌿 {name}</h3>
            <p>{description}</p>
            <p><b>Suggested time:</b> {duration}</p>
            <span class="pill">{category}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "Move gently and stop if something hurts or feels uncomfortable."
    )


# ============================================================
# MOVEMENT
# ============================================================

elif page == "🏃 Movement":

    st.title("🏃 Movement Breaks")

    st.write(
        "Short movement breaks can help you step away from your desk."
    )

    movements = [
        "🚶 Walk around for a few minutes",
        "🙆 Gentle shoulder rolls",
        "👐 Stretch your hands and wrists",
        "🧍 Stand up and change position",
        "🌿 Take a short outdoor break",
        "👀 Look away from your screen for a while"
    ]

    for movement in movements:
        st.markdown(
            f"""
            <div class="card">
            {movement}
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("✅ Complete Movement Break"):
        st.session_state.movement += 1
        st.success(
            f"Movement break #{st.session_state.movement} recorded!"
        )


# ============================================================
# WELL-BEING
# ============================================================

elif page == "😊 Well-being":

    st.title("😊 Well-being")

    st.write(
        "A small space to check in with yourself."
    )

    mood = st.select_slider(
        "How are you feeling today?",
        options=[
            "😞 Low",
            "😕 Not great",
            "😐 Okay",
            "🙂 Good",
            "😄 Great"
        ]
    )

    if st.button("Save Mood"):
        st.session_state.mood = mood
        st.success("Mood saved 💚")

    st.subheader("🌬️ Box Breathing")

    st.write(
        "Try a slow breathing pattern: inhale gently, pause, "
        "exhale gently, pause."
    )

    if st.button("Start Breathing Activity"):
        st.info(
            "Breathe slowly and comfortably for a few rounds. "
            "There is no need to force your breathing."
        )

    st.subheader("📓 Journal")

    journal = st.text_area(
        "Write anything you want to reflect on"
    )

    if st.button("Save Journal"):
        st.success("Journal entry saved for this session.")


# ============================================================
# WELLNESS
# ============================================================

elif page == "💧 Wellness":

    st.title("💧 Student Wellness")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["💧 Water", "😴 Sleep", "🥗 Food", "🌿 Daily Habits"]
    )

    with tab1:

        st.subheader("Water Tracker")

        st.session_state.water_target = st.number_input(
            "Your personal daily water target",
            min_value=1,
            max_value=20,
            value=st.session_state.water_target
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("➕ Add 1"):
                st.session_state.water += 1
                st.rerun()

        with col2:
            if st.button("➖ Remove 1"):
                st.session_state.water = max(
                    0,
                    st.session_state.water - 1
                )
                st.rerun()

        with col3:
            if st.button("🔄 Reset Water"):
                st.session_state.water = 0
                st.rerun()

        st.progress(
            min(
                st.session_state.water /
                max(st.session_state.water_target, 1),
                1.0
            )
        )

        st.write(
            f"{st.session_state.water} / "
            f"{st.session_state.water_target}"
        )

    with tab2:

        st.subheader("😴 Sleep Routine")

        sleep_tips = [
            "Keep a fairly regular sleep schedule.",
            "Give yourself time to wind down before bed.",
            "Keep your study space separate from your sleep space when possible.",
            "Avoid studying until you are completely exhausted."
        ]

        for tip in sleep_tips:
            st.markdown(f"• {tip}")

    with tab3:

        st.subheader("🥗 Student Food Ideas")

        foods = [
            "Fruit + curd",
            "Vegetable sandwich",
            "Dal + roti + vegetables",
            "Rice + dal + vegetables",
            "Paneer/tofu wrap",
            "Nuts and fruit",
            "Homemade poha or upma"
        ]

        for food in foods:
            st.markdown(f"• {food}")

        st.caption(
            "Aim for regular, varied meals and snacks that suit your needs."
        )

    with tab4:

        st.subheader("🌿 Healthy Habits")

        habits = [
            "Take regular study breaks",
            "Move your body throughout the day",
            "Drink water when thirsty",
            "Get enough sleep",
            "Make time for hobbies",
            "Stay connected with people you trust"
        ]

        for habit in habits:
            st.checkbox(habit)


# ============================================================
# SMART REMINDERS
# ============================================================

elif page == "🔔 Smart Reminders":

    st.title("🔔 Smart Reminders")

    st.write(
        "Create reminders for study, breaks, water, movement and other tasks."
    )

    reminder_text = st.text_input(
        "Reminder"
    )

    reminder_type = st.selectbox(
        "Type",
        [
            "Study",
            "Water",
            "Movement",
            "Break",
            "Sleep",
            "General"
        ]
    )

    reminder_time = st.time_input(
        "Reminder time"
    )

    if st.button("➕ Add Reminder"):

        if reminder_text.strip():

            st.session_state.reminders.append(
                {
                    "text": reminder_text,
                    "type": reminder_type,
                    "time": reminder_time.strftime("%I:%M %p"),
                    "done": False
                }
            )

            st.success("Reminder added!")

    st.subheader("Your Reminders")

    if not st.session_state.reminders:
        st.info("No reminders yet.")

    for i, reminder in enumerate(
        st.session_state.reminders
    ):

        col1, col2 = st.columns([5, 1])

        with col1:
            st.write(
                f"🔔 **{reminder['text']}** — "
                f"{reminder['time']} · {reminder['type']}"
            )

        with col2:

            if st.button(
                "✓",
                key=f"complete_reminder_{i}"
            ):
                st.session_state.reminders[i]["done"] = True

        if reminder["done"]:
            st.success("Completed")


# ============================================================
# SETTINGS
# ============================================================

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.subheader("👤 Profile")

    name = st.text_input(
        "Your name",
        value=st.session_state.profile_name
    )

    if st.button("Save Profile"):
        st.session_state.profile_name = (
            name.strip() if name.strip() else "Student"
        )
        st.success("Profile updated!")

    st.subheader("🎨 Preferences")

    theme = st.selectbox(
        "Preferred style",
        [
            "Soft & Calm",
            "Minimal",
            "Lavender",
            "Sage Green"
        ]
    )

    st.write(f"Current preference: **{theme}**")

    st.subheader("🔔 Focus Mode")

    focus_mode = st.toggle(
        "Turn Focus Mode ON"
    )

    if focus_mode:
        st.info(
            "Focus Mode is ON inside LIVORA."
        )
    else:
        st.success(
            "Focus Mode is OFF."
        )

    st.subheader("🧹 Session Data")

    if st.button("Reset LIVORA Data"):
        for key in defaults:
            if key in st.session_state:
                del st.session_state[key]

        st.success("Session data reset. Refresh the app.")


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<hr>
<div style="text-align:center; padding:15px; color:#788078;">
🌿 LIVORA — Live Better. Study Smarter.<br>
Designed by Dixa ✨
</div>
""", unsafe_allow_html=True)
