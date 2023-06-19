from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    context={'message':'nothing'}
    if request.method=='POST':
        word=request.POST['word']
        api_url=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response=requests.get(api_url).json()
        try:
            word = response[0]['word']

        except Exception as e:
            context = {'message': 'No Definitions Found !'}

        else:
            try:
                pronoun = response[0]['phonetic']
            except Exception as e:

                pronoun = 'Phonetic Not Found !'

            audio_url = response[0]['phonetics'][0]['audio']
            meanings = list(response[0]['meanings'])

            context = {
                'word': word,
                'pronoun': pronoun,
                'audio_url': audio_url,
                'meanings': meanings,
                'message': '',
            }



    return render(request, 'home.html',context)