# Import necessary libraries
import streamlit as st
import openai

# Streamlit app title
st.set_page_config(page_title="Blog Generator Chatbot")
st.title("Blog Generator Chatbot")

# Sidebar to input OpenAI API key
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")


# Function to generate the blog using OpenAI API
def generate_blog(topic, description, num_headings, num_paragraphs, total_word_count):
    openai.api_key = api_key
    prompt = f"""
                You are an expert content writer \\
                your task is to write a blog, the details of the blog is mentioned below \\
                the details of the blog is delimated in triple back ticks \\
                ```
                the topic of the blog is "{topic}" \\
                the description of the blog is "{description}" \\
                the number of headings in the blog is {num_headings} \\
                the number of paragraphs in the blog is {num_paragraphs} \\
                the total word count of the blog is {total_word_count} \\
                ```
        """

    messages = [{"role": "system", "content": "You are an expert content creator, your task is to write a blog for the user based on the topic and description provided by the user."},
                {"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )

    blog_text = response.choices[0].text
    return blog_text


# Input fields for the user
topic = st.text_input("Enter the topic of the blog")
description = st.text_area("Enter a description about the topic")
num_headings = st.number_input("Number of Headings", min_value=1, value=3)
num_paragraphs = st.number_input("Number of Paragraphs", min_value=1, value=5)
total_word_count = st.number_input("Total Word Count", min_value=50, value=300)


def main():
    # Button to generate the blog
    if st.button("Generate Blog"):
        # Validate user inputs
        if not api_key:
            st.error("Please enter your OpenAI API key.")
        elif not topic:
            st.error("Please enter the topic of the blog.")
        elif not description:
            st.error("Please enter a description about the topic.")
        elif not num_headings:
            st.error("Please enter the number of headings.")
        elif not num_paragraphs:
            st.error("Please enter the number of paragraphs.")
        elif not total_word_count:
            st.error("Please enter the total word count.")
        else:
            # Generate the blog
            generated_blog = generate_blog(
                topic, description, num_headings, num_paragraphs, total_word_count)

            # Display the generated blog
            st.subheader("Generated Blog:")
            st.write(generated_blog)


if __name__ == "__main__":
    main()
