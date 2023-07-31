from crypt import methods
import openai
import myopenaiapikey
import json
from flask import Flask

openai.api_base = myopenaiapikey.base
openai.api_key = myopenaiapikey.api

app = Flask(__name__)

def ai_run_command(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "assistant", 
             "content": """
                        I want you to act as a Linux terminal. I will provide commands and history, then you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do no write explanations. Do not type commands unless I instruct you to do so.\n\n### Command:\n{command}\n\n### History:\n{history}\n### Response:\n
                        """},
            {"role": "user", "content": query}],
    )
    message = response["choices"][0]["message"]
    return message



@app.route('/admin/<cmd>',methods=['GET','POST'])
def hello_admin(cmd):
    message = ai_run_command(cmd)
    return {"message":message["content"]}
    #return render_template
if __name__ == '__main__':

    app.run('0.0.0.0',9000,debug=True)
