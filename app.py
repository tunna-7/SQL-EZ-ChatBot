from dotenv import load_dotenv
load_dotenv() ## loading all env var

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function Load Google Gemini Model & provide SQL Query as Response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from SQL Database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(sql)
    rows = curr.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name PLAYER and has the following columns - NAME, CLUB, 
    COUNTRY and GOALS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM PLAYER ;
    \nExample 2 - Tell me all the players playing for Brazil?, 
    the SQL command will be something like this SELECT * FROM PLAYER 
    where COUNTRY="Brazil"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Rretrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

## On clicking of submit
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"player.db")
    st.subheader("The Response is ")
    for row in data:
        print(row[0])
        st.header(row[0])