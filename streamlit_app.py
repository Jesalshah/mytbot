#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from langchain import OpenAI
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
import openai
import sys
import streamlit as st
import os


# In[ ]:


os.environ["OPENAI_API_KEY"] = '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'


# In[ ]:


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
#st.sidebar.header('Training Bot')
st.header("Welcome to Training World")


# In[ ]:


import streamlit as st
_emp = st.empty()
text = _emp.text_input("Enter Something here! ")
if text:
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(text, response_mode="compact")
    st.write(response.response)

