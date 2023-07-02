import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from typing import Union, Optional, Literal

st.set_page_config(page_title="Michael Xu's Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
                    
local_css("style/style.css")

lottie_coding=load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_cmd8kh2q.json")

img_contact_form=Image.open("assets/0001.png")
img_lottie_animation=Image.open("assets/0002.png")

with st.container():
    st.subheader("Hi, I am Michael :wave:")
    st.title("An AI specilalist working hard to change the world")
    st.write("I am pasionate about finding ways to use AI technology to make practices tools and applications.")
    st.write("[Learn More>](https://aiinfoall.com/)")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Hello, my name is Michael and I am an AI technology scientist and Professor of Practice. I have spent my entire career working in the field of artificial intelligence, developing new technologies and applications that can be used to solve real-world problems.

As a Professor of Practice, I am passionate about sharing my knowledge and experience with the next generation of AI professionals. I teach courses on topics such as machine learning, natural language processing, computer vision, and robotics, and work closely with my students to help them develop the skills they need to succeed in this fast-paced and rapidly-evolving field.

In addition to my work as a teacher, I am also a dedicated researcher. I have published numerous papers on topics ranging from deep learning and neural networks to reinforcement learning and computer vision. My research has been cited in academic journals and industry publications around the world, and I am constantly striving to push the boundaries of what is possible with AI technology.

Overall, I am deeply committed to advancing the field of artificial intelligence and helping others to understand and harness the power of this exciting technology. Whether I am teaching, researching, or working with industry partners, I am always looking for new ways to make a positive impact on the world through AI.
            """)
        st.write("[YouTube Channel>](https://www.youtube.com/@epicax6352/videos)")
    
    with right_column:
      st_lottie(lottie_coding,height=580,key="Coding")
                             
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Using AI to predict the lottery results")
        st.write(
            """
            In this lesson, we will explore how artificial intelligence (AI) can be used to predict lottery results. We will discuss the various techniques and algorithms used in lottery prediction and examine the potential benefits and limitations of using AI for this purpose. By the end of this lesson, you will have a basic understanding of how AI can be applied to lottery prediction and its implications for the future of gambling and gaming industries.
            """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=-7Pv6z3RO-w)")
with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Using AI to predict the coming financial crisis")
        st.write(
            """
            In this lesson, we will explore how artificial intelligence (AI) can be used to predict the next financial crisis. We will discuss the various data sources and algorithms used in financial crisis prediction and examine the potential benefits and limitations of using AI for this purpose. By the end of this lesson, you will have a basic understanding of how AI can be applied to financial crisis prediction and its implications for the future of finance and risk management.In this lesson, we will explore how artificial intelligence (AI) can be used to predict lottery results. We will discuss the various techniques and algorithms used in lottery prediction and examine the potential benefits and limitations of using AI for this purpose. By the end of this lesson, you will have a basic understanding of how AI can be applied to lottery prediction and its implications for the future of gambling and gaming industries.
            """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=I5xa7irrzes)")
        
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/michaelxwh@gmail.com" method="POST">
     <input type="hidden" name="value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
         st.empty()
