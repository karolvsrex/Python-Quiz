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
        "What is the name of the most decorated US Navy ship of all time?": "USS New Jersey"
    }

    # Creating input fields for each question
    user_answers = {}
    for q in questions:
        user_answers[q] = st.text_input(q, key=q)

    # Submit button for the entire quiz
    if st.button("Submit Quiz"):
        st.session_state.answers_submitted = True
        st.session_state.score = sum(user_answers[q].lower() == answer.lower() for q, answer in questions.items())

    # Display the score and the correct answers after the quiz has been submitted
    if st.session_state.answers_submitted:
        st.write(f"You received {st.session_state.score} out of {len(questions)} questions correct.")
        st.write(f"Your score is {(st.session_state.score / len(questions)) * 100}%.")

        st.subheader("Review Answers")
        for question, correct_answer in questions.items():
            user_answer = user_answers[question]
            if user_answer.lower() == correct_answer.lower():
                st.markdown(f"**{question}**\nYour answer: *{user_answer}*\n✅ Correct!")
            else:
                st.markdown(f"**{question}**\nYour answer: *{user_answer}*\n❌ Incorrect! The correct answer was: *{correct_answer}*")

if __name__ == "__main__":
    main()


