import openai

from eli5.secrets import OPENAI_API_KEY

# OpenAI
openai.api_key = OPENAI_API_KEY


def summarize(text: str) -> str:
    try:
        response = openai.Completion.create(max_tokens=60, engine='text-davinci-003',
                                            prompt=text + " Explain this like I am five in less than 200 characters.")
        output = response.choices[0].text

        return output
    except Exception as e:
        print(f'Unable to summarize {text}')
        print(e)


if __name__ == '__main__':
    summarized_text = summarize("@JagHeterEdd Could you ELI5 what OpenAI ChatGPT is?")
    print(summarized_text)
