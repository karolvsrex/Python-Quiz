import streamlit as st

def check_answer(question_key, correct_answer):
    if st.session_state[question_key] == correct_answer:
        st.success("That is correct")
        st.session_state.score += 1
    else:
        st.error("That is incorrect")

def main():
    st.title("Welcome to my Quiz")

    # Initialize session state variables
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'submitted' not in st.session_state:
        st.session_state.submitted = {1: False, 2: False, 3: False, 4: False}

    if st.button("Start Quiz"):
        st.write("Brilliant, let us begin!")

        # Question 1
        q1_answer = st.text_input("In what year did the American Civil War begin?", key='q1')
        if st.button("Check Answer 1") and not st.session_state.submitted[1]:
            check_answer('q1', '1861')
            st.session_state.submitted[1] = True

        # Question 2
        q2_answer = st.text_input("In what year did the American Revolutionary War begin?", key='q2')
        if st.button("Check Answer 2") and not st.session_state.submitted[2]:
            check_answer('q2', '1775')
            st.session_state.submitted[2] = True

        # Question 3
        q3_answer = st.text_input("In what year did the Russian Revolution take place?", key='q3')
        if st.button("Check Answer 3") and not st.session_state.submitted[3]:
            check_answer('q3', '1917')
            st.session_state.submitted[3] = True

        # Question 4
        q4_answer = st.text_input("What is the name of the most decorated US Navy ship of all time?", key='q4')
        if st.button("Check Answer 4") and not st.session_state.submitted[4]:
            correct_answer = "uss new jersey"
            if q4_answer.lower() == correct_answer:
                st.success("That is correct")
                st.session_state.score += 1
            else:
                st.error("That is incorrect")
            st.session_state.submitted[4] = True

        # Show Final Score
        if all(st.session_state.submitted.values()):
            st.write(f'You received {st.session_state.score} questions correct out of 4.')
            st.write(f'You received {(st.session_state.score/4)*100}%.')

if __name__ == "__main__":
    main()
