import streamlit as st

def main():
    st.title("Welcome to my Quiz")

    # Initialize session state variables
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answers_submitted' not in st.session_state:
        st.session_state.answers_submitted = False

    # Defining the questions and their correct answers
    questions = {
        "In what year did the American Civil War begin?": "1861",
        "In what year did the American Revolutionary War begin?": "1775",
        "In what year did the Russian Revolution take place?": "1917",
        "What is the name of the most decorated US Navy ship of all time?": "uss new jersey"
    }

    # Creating input fields for each question
    user_answers = {}
    for q in questions:
        user_answers[q] = st.text_input(q, key=q)

    # Submit button for the entire quiz
    if st.button("Submit Quiz"):
        st.session_state.answers_submitted = True
        st.session_state.score = sum(user_answers[q].lower() == answer.lower() for q, answer in questions.items())
    
    # Display the score after the quiz has been submitted
    if st.session_state.answers_submitted:
        st.write(f"You received {st.session_state.score} out of {len(questions)} questions correct.")
        st.write(f"Your score is {(st.session_state.score / len(questions)) * 100}%.")

if __name__ == "__main__":
    main()


