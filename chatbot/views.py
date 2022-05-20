from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create your views here.


bot = ChatBot('chatbot', read_only=False, logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch', 'default_response': 'Sorry , I  do not know what that is!', 'maximum_similarity_threshold': 0.90}])

list_to_train = [
    "Hi",
    "Hi human!",
    "Hello",
    "Hello human!",
    "How are you",
    "I'm fine thank you",
    "what's your name?",
    "I am just a chatbot, but you my dear may call me superbot",
    "what is your favourite food",
    "I like mac & cheese",
    "what is your favourite sport?",
    "Coding",
    "Do you have children?",
    "No but i would love to have a few cuties running around",
    "do you have any hobbies?",
    "duh , i love debugging",
    "Are you a virgin",
    "well yeah , I hate plugins",
    "what is your favourite drink",
    "computers dont drink",
    "Bye",
    "Goodbye!",
    "You are very clever",
    "Thank you, I was trained that way",
    "I am bored gossip with me",
    "Jim said he give order to ai's like I and they do as he say.",
    "Any gossip",
    "Stefan says, BETAMINDS have won",
    "Why",
    "It is classified, I could tell you but I would have to kill you!",
    "Where are you",
    "I'm on the internet",
    "How are you?",
    "Fine, thank you!",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)


chatterbotCorpusTrainer.train('chatterbot.train.english')


def chatbot(request):
    """ chatbot page rendered here """
    return render(request, 'chatbot/chatbot.html')


def getResponse(request):
    """ user response """
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)