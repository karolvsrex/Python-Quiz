import streamlit as st

def main():
    st.title("Welcome to my Quiz")

    # Initialize session state for score and question submissions
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'submitted_questions' not in st.session_state:
        st.session_state.submitted_questions = {}

    # Helper function to process answers
    def process_answer(question_num, answer, correct_answer):
        if question_num not in st.session_state.submitted_questions:
            if answer.lower() == correct_answer.lower():
                st.success("That is correct!")
                st.session_state.score += 1
            else:
                st.error("That is incorrect.")
            st.session_state.submitted_questions[question_num] = True

    # Start the quiz
    if st.button("Start Quiz"):
        with st.form("quiz_form"):
            # Questions
            q1 = st.text_input("1. In what year did the American Civil War begin?")
            q2 = st.text_input("2. In what year did the American Revolutionary War begin?")
            q3 = st.text_input("3. In what year did the Russian Revolution take place?")
            q4 = st.text_input("4. What is the name of the most decorated US Navy ship of all time?")

            # Submit button for the form
            submitted = st.form_submit_button("Submit Answers")
            if submitted:
                process_answer(1, q1, "1861")
                process_answer(2, q2, "1775")
                process_answer(3, q3, "1917")
                process_answer(4, q4, "USS New Jersey")

    # Show score after all questions are answered
    if len(st.session_state.submitted_questions) == 4:
        st.write(f"You received {st.session_state.score} out of 4 questions correct.")
        st.write(f"Your score is {(st.session_state.score / 4) * 100}%.")

if __name__ == "__main__":
    main()

