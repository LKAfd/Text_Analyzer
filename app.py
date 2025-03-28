# app.py
import streamlit as st
import pyperclip
from utils.text_analysis import (
    count_words,
    count_characters,
    count_vowels,
    search_and_replace,
    contains_python,
    average_word_length
)

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="wide")
    st.title("🔍Text Analyzer")
    st.markdown("---")
    
    # Initialize session state
    if 'analyzed' not in st.session_state:
        st.session_state.analyzed = False

    # User input section
    with st.container():
        st.header("Input Text")
        text = st.text_area("Enter your paragraph here:", height=200, key="input_text")
        analyze_clicked = st.button("🚀 Analyze Text", type="primary")

    if analyze_clicked:
        if not text.strip():
            st.error("⛔ Error: Please enter some text to analyze!")
            st.session_state.analyzed = False
        else:
            st.session_state.analyzed = True
            st.success("✅ Analysis completed successfully!")

    if st.session_state.analyzed and text.strip():
        st.markdown("---")
        with st.container():
            st.header("📊 Basic Statistics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Words", f"{count_words(text):,}", help="Includes all whitespace-separated elements")
            with col2:
                st.metric("Total Characters", f"{count_characters(text):,}", help="Including spaces and punctuation")
            with col3:
                st.metric("Vowel Count", f"{count_vowels(text):,}", help="A, E, I, O, U (case insensitive)")

        st.markdown("---")
        with st.expander("🔍 Advanced Text Analysis", expanded=True):
            tab1, tab2, tab3 = st.tabs(["Text Manipulation", "Word Insights", "Special Features"])

            with tab1:
                st.subheader("Search & Replace")
                col_search, col_replace = st.columns(2)
                with col_search:
                    search_word = st.text_input("Search term:")
                with col_replace:
                    replace_word = st.text_input("Replacement term:")
                
                if search_word and replace_word:
                    modified_text = search_and_replace(text, search_word, replace_word)
                    if modified_text != text:
                        st.success("Replacement successful!")
                        st.code(modified_text, language="text")
                    else:
                        st.warning("⚠️ Search term not found in text")

                st.subheader("Case Conversion")
                upper_col, lower_col = st.columns(2)
                with upper_col:
                    with st.container():
                        st.markdown("**UPPERCASE VERSION**")
                        upper_text = text.upper()
                        st.code(upper_text, language="text")
                        if st.button("📋 Copy UPPERCASE", key="upper_copy"):
                            try:
                                pyperclip.copy(upper_text)
                                st.toast("Copied to clipboard!", icon="✅")
                            except:
                                st.error("Clipboard access not supported")

                with lower_col:
                    with st.container():
                        st.markdown("**lowercase version**")
                        lower_text = text.lower()
                        st.code(lower_text, language="text")
                        if st.button("📋 Copy lowercase", key="lower_copy"):
                            try:
                                pyperclip.copy(lower_text)
                                st.toast("Copied to clipboard!", icon="✅")
                            except:
                                st.error("Clipboard access not supported")

            with tab2:
                st.subheader("Word Insights")
                avg_len = average_word_length(text)
                st.metric("Average Word Length", f"{avg_len:.2f} characters", 
                        help="Calculated as total characters (including spaces) divided by word count")
                
                python_check = contains_python(text)
                st.metric("Contains 'Python'", 
                         "✅ Found" if python_check else "❌ Not Found",
                         help="Case-sensitive search for 'Python'")

            with tab3:
                st.subheader("Text Preview")
                with st.container():
                    st.markdown("**Original Text Preview**")
                    st.text(text[:500] + ("..." if len(text) > 500 else ""))

                st.subheader("Vowel Distribution")
                vowels = {'a', 'e', 'i', 'o', 'u'}
                vowel_counts = {vowel: text.lower().count(vowel) for vowel in vowels}
                st.bar_chart(vowel_counts)

if __name__ == "__main__":
    main()