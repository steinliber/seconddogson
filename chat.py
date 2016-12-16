from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
deepThought = ChatBot("deepThought", logic_adapters=[
         {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'NO!'
        }
    ],)
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train("chatterbot.corpus.chinese")
deepThought.train("chatterbot.corpus.english")
