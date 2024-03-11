#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request

import google.generativeai as palm
import replicate
import os

os.environ["REPLICATE_API_TOKEN"]="r8_LyUW2lM2Tyq3Iohj4ttUfuyaoJVu44j4B2v6f"

palm.configure(api_key="AIzaSyCxzmOoXnchOiVcbYE8ye5jZd7MuBgGEQM")
defaults = { 'model': "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/palm",methods=["GET","POST"])
def palm():
    return(render_template("palm.html"))

@app.route("/mj",methods=["GET","POST"])
def mj():
    return(render_template("mj.html"))

@app.route("/result_palm",methods=["GET","POST"])
def result_palm():
    q = request.form.get("q")
    import google.generativeai as palm
    r = palm.chat(**defaults,messages=q)
    return(render_template("result_palm.html",r=r.last))

@app.route("/result_mj",methods=["GET","POST"])
def result_mj():
    q = request.form.get("q")
    r = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={
        "prompt": q,
        }
    )
    return(render_template("result_mj.html",r=r[0]))

@app.route("/end",methods=["GET","POST"])
def end():
    print("end")
    return(render_template("end.html"))

if __name__ == "__main__":
    app.run()


# In[ ]:




