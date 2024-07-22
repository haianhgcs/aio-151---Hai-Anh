import streamlit as st
import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import ml_util

    print("Câu #1: A")
    print("Câu #2: C")
    options = st.multiselect("Your favorite colors:", [
                             "Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"])
    st.write("You selected:", options)

    print("Câu #3: D")
    print("Câu #4: A")
    st.image("aaa", caption="A cat", width=100, channels="RGB")

    print("Câu #5: A")
    print(ml_util.levenshtein_distance("elmets", "elements"))

    print("Câu #6: D")
    print("Câu #7: D")
    with st.form("my_form"):
        col1, col2 = st . columns(2)
        f_name = col1.text_input('First Name')
        l_name = col2.text_input('Last Name')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("First Name: ", f_name, " - Last Name: ", l_name)

    print("Câu #8: A")
    print("Câu #9: D")
    print("Câu #10: B")
