from django.shortcuts import render
from email import contentmanager
import requests
import json
from googletrans import Translator
import random

def convertText(text,src,dest):
    translator = Translator()
    translation = translator.translate(text,src=src,dest=dest)
    return translation.text

# Create your views here.
def home(request):
    return render(request,"home.html")

def getHadis(request):
    if request.method == "POST":
        hadistext = request.POST["hadisText"]
        source = request.POST["source"]
        print(hadistext,source)
        context = {}
        context["en_text"] = hadistext
        ar_text = convertText(hadistext,src="ar",dest="en")
        context["ar_text"] = ar_text
        context["hi_text"] = convertText(hadistext,src="ar",dest="hi")
        context["source"] = source
        return render(request,"hadis.html",context)