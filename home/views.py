from django.shortcuts import render
from .forms import Ceaser
from .forms import follow
# Create your views here.


# rendered in urls
def ccpa(request):
    form = follow(request.POST or None)
    text = ''
    key = 0
    context = {
        'form': form
    }
    if form.is_valid():
        key = form.cleaned_data.get('key')
        text = form.cleaned_data.get('user_text')
        result = ceaser_ciphar(text, key)
        context = {'form': form, 'result': result}
    return render(request, 'index.html', context)


# ceasers formulae goes here
def ceaser_ciphar(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    cipher = ''
    for c in plaintext:
        if c.isalpha():
            cipher += alphabet[alphabet.index(c) + key]
        else:
            cipher += c
    return cipher


def index(request):
    form = Ceaser(request.POST or None)
    text = ''
    key = 0
    context = {
        'form': form
    }
    if form.is_valid():
        key = form.cleaned_data.get('key')
        text = form.cleaned_data.get('user_text')
        result = Ceasarcipher(text, key)
        context = {'form': form, 'result': result}
    return render(request, 'index.html', context)


def Ceasarcipher(string, num):
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        # "A", "B", "C", "D", "E", "F", "G", "H",
        # "I", "J", "K", "L", "M", "N", "O", "P",
        # "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    # Create our substitution dictionary
    dic = {}
    for i in range(0, len(alphabet)):
        dic[alphabet[i]] = alphabet[(i + num) % len(alphabet)]

    # Convert each letter of string to the corrsponding
    # encrypted letter in our dictionary creating the cryptext
    ciphertext = ""
    for x in string:
        if x in dic:
            x = dic[x]
        ciphertext += x

    return ciphertext
