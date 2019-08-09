from rasa.core.channels.socketio import SocketIOInput
from rasa.core.agent import Agent
from rasa.core.interpreter import NaturalLanguageInterpreter

# load your trained agent
interpreter = NaturalLanguageInterpreter.create('C:/Users/NJJainnew_ex/models/20190805-123059/nlu')
agent = Agent.load('C:/Users/NJJain/new_ex/models/20190805-123059', interpreter=interpreter)

input_channel = SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
    )

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5005)