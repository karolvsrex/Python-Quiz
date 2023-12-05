import streamlit as st

def main():
    st.title("Welcome to my Quiz")

    if st.button("Start Quiz"):
        st.write("Brilliant, let us begin!")
        score = 0

        # Question 1
        answer = st.text_input("In what year did the American Civil War begin?")
        if st.button("Check Answer 1"):
            if answer.lower() == "1861":
                st.success("That is correct")
                score += 1
            else:
                st.error("That is incorrect")

        # Question 2
        answer = st.text_input("In what year did the American Revolutionary War begin?")
        if st.button("Check Answer 2"):
            if answer == "1775":
                st.success("That is correct")
                score += 1
            else:
                st.error("That is incorrect")

        # Question 3
        answer = st.text_input("In what year did the Russian Revolution take place?")
        if st.button("Check Answer 3"):
            if answer == "1917":
                st.success("That is correct")
                score += 1
            else:
                st.error("That is incorrect")

        # Question 4
        answer = st.text_input("What is the name of the most decorated US Navy ship of all time?")
        if st.button("Check Answer 4"):
            if answer.lower() == "uss new jersey":
                st.success("That is correct")
                score += 1
            else:
                st.error("That is incorrect")

        # Show Final Score
        if st.button("Show My Score"):
            st.write(f'You received {score} questions correct out of 4.')
            st.write(f'You received {(score/4)*100}%.')

if __name__ == "__main__":
    main()
