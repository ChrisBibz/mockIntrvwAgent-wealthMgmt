
import streamlit as st
import random

# Define the mock interview agent
class MockInterviewAgent:
    def __init__(self):
        self.questions = [
            "Why do you want this job?",
            "What do you do for fun?",
            "Where do you see yourself 36 months from now?",
            "Where do you see the industry three to five years from now?",
            "Who is your competition?",
            "Are there any new products or markets that you're exploring?",
            "Looking forward, what concerns you the most?"
        ]
        self.follow_up_questions = [
            "Can you elaborate on that?",
            "Why do you think that's important?",
            "How does that relate to your previous experience?",
            "What steps would you take to address that?"
        ]

    def conduct_interview(self):
        st.title("Mock Interview Agent")
        st.write("Welcome to the mock interview for an entry-level position at our wealth management firm.")
        st.write("Let's start with some questions.")

        responses = []
        for question in self.questions:
            st.subheader(f"Question: {question}")
            answer = st.text_input(f"Your answer to: '{question}'", key=question)
            follow_up = random.choice(self.follow_up_questions)
            st.markdown(f"**Follow-up Question:** {follow_up}")
            follow_up_answer = st.text_input(f"Your answer to follow-up: '{follow_up}'", key=question+"_followup")
            responses.append((question, answer, follow_up, follow_up_answer))

        if st.button("Submit Interview"):
            st.success("Thank you for participating in the mock interview. We hope this helps you prepare for your real interview.")
            st.write("### Summary of Your Responses:")
            for q, a, fq, fa in responses:
                st.markdown(f"**Q:** {q}")
                st.markdown(f"**A:** {a}")
                st.markdown(f"**Follow-up:** {fq}")
                st.markdown(f"**Follow-up Answer:** {fa}")
                st.markdown("---")

# Run the app
agent = MockInterviewAgent()
agent.conduct_interview()
