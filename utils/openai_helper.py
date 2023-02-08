import os
import openai


class OpenAI():

    def __init__(self):
        openai.organization = 'org-GwscIdlNDH1tNF6kJYobePUh'
        openai.api_key = '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'

    def translate(self, fromLanguage, language, text):
        prompt = "translate this from {} into {}: {}".format(
            fromLanguage, language, text)
        translation = self.completion(prompt=prompt)
        return translation[0].text

    def completion(self, prompt):
        data = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.3,
                                        max_tokens=500, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
        return data.choices
