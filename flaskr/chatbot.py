from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer




from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('chatbot', __name__)


# Creating ChatBot Instance
chatbot = ChatBot('CoronaBot')

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 

@bp.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@bp.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return "I am sorry, my developer is dealing with semantic errors!"

