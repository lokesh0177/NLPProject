#
# Import
import paralleldots
# Setting your API key
class API:
    def __init__(self):
        paralleldots.set_api_key('6XV8Jg1iD3OBs1ZbA0i55zyWunZXHQGbDQeQnbBfdjs')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def emotion_analysis(self,text):
        response = paralleldots.emotion(text)
        return response

    def ner_analysis(self,text):
        response = paralleldots.ner(text)
        return response