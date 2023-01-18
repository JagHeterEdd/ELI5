from fastapi import FastAPI
import openai

from secrets import OPENAI_API_KEY

# OpenAI
openai.api_key = OPENAI_API_KEY


def summarize(text: str) -> str:
    response = openai.Completion.create(max_tokens=60, engine='text-davinci-003',
                                        prompt=text + " Explain this like I am five in less than 200 characters.")
    output = response.choices[0].text

    return output


# FastAPI
app = FastAPI()


# Example Request
# curl http://127.0.0.1:8000/explain/hello+my+name+is+edd
@app.get("/explain/{text}")
def read_root(text):
    summarized_text = summarize(text)
    escapes = ''.join([chr(char) for char in range(1, 32)])
    formatted_response = summarized_text.translate(escapes).strip()
    return {"summarized_text": formatted_response}
