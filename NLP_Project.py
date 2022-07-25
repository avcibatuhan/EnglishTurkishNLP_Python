from textblob import TextBlob
import webbrowser
import re
import sys
import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from turkishnlp import detector
from spellchecker import SpellChecker
from typing import List

#TurkishNLP kütüphanesinin dokümantasyonunun indirilmesi
obj = detector.TurkishNLP()
obj.download()
obj.create_word_set()

def TurnToRightSentence(text):
    misspelled=[]
    
    if language.get() == 1:
        blob = TextBlob(text)
        spell = SpellChecker()
        #Cümle kelimelerine ayrılır
        misspelled = list(spell.unknown(text.split()))
        #Yanlış kelimenin bulunması
        correctedBlob = blob.correct()

        if(len(correctedBlob) > 43):
            newline = '\n'            
            correctedBlob = correctedBlob[:43] + newline + correctedBlob[43:]

        if(len(correctedBlob) > 86):
            newline = '\n'            
            correctedBlob = correctedBlob[:86] + newline + correctedBlob[86:]

        if(len(correctedBlob) > 135):
            newline = '\n'            
            correctedBlob = correctedBlob[:129] + newline + correctedBlob[129:]

        wrong_word_text2.config(text=misspelled)
        title.config(text="Doğru yazım")
        return correctedBlob

    elif language.get() == 2:
        lwords = obj.list_words(text)
        corrected_words = obj.auto_correct(lwords)
        changedWords = []
        lenLwords = len(lwords)

        # Yanlış kelimenin bulunması
        for i in range(lenLwords):
            if (lwords[i] != corrected_words[i]):
                changedWords.append(lwords[i])

        wrong_word_text2.config(text=changedWords)
        corrected_string = " ".join(corrected_words)

        if(len(corrected_string) > 40):
            newline = '\n'            
            corrected_string = corrected_string[:40] + newline + corrected_string[40:]
        return corrected_string

def know_more_clicked(event):
    instructions = (
        "https://github.com/avcibatuhan")
    webbrowser.open_new_tab(instructions)

def btn_clicked():
    input = token_entry.get()
    trueSentence = TurnToRightSentence(input)
    info_text.config(text=trueSentence)    
    
window = tk.Tk()
window.title('Doğal Dil İşlemeye Giriş')
window.geometry("862x519")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=719, width=1062,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")

token_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
token_entry.place(x=490.0, y=137+25, width=321.0, height=200)
token_entry.focus()

language = tk.IntVar() 
tk.Radiobutton(window, text='English', variable=language, value=1).place(x=27,y=27) 
tk.Radiobutton(window, text='Türkçe', variable=language, value=2).place(x=97, y=27)
language.set(1)

btn=tk.Button(window,text="Düzelt", width=50,height=5,command=btn_clicked)
btn.place(x=467,y=401)

canvas.create_text(
    490.0, 156.0, text="Cümle", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

canvas.create_text(
    573.5, 88.0, text="Bir cümle giriniz.",
    fill="#515486", font=("Arial-BoldMT", int(22.0)))
    
title = tk.Label(
    text="NLP", bg="#3A7FF6",
    fg="white", font=("Arial-BoldMT", int(20.0)))
title.place(x=27.0, y=120.0)

info_text = tk.Label(
    text="Sağda bulunan alana cümlenizi girerek \n doğru olup olmadığını görebilirsiniz.\n\n"
    "Türkçe için değişiklik yapabilirsiniz.\n",
    bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0)))

info_text.place(x=27.0, y=200.0)

wrong_word_text = tk.Label(
    text="Yanlış kelimeler", bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0))
    )

wrong_word_text.place(x=27.0,y=400)

wrong_word_text2 = tk.Label(
    text="", bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0))
    )
wrong_word_text2.place(x=37.0,y=450)

know_more = tk.Label(
    text="Created by Batuhan Avcı & Berk Soğukpınar",
    bg="#3A7FF6", fg="white", cursor="hand2")
    
know_more.place(x=27, y=500)
know_more.bind('<Button-1>', know_more_clicked)

window.resizable(False, False)
window.mainloop()