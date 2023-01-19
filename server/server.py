from fastapi import FastAPI
from eli5.app import summarize

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
