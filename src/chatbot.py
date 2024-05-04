from utils.helpers import get_completion_from_messages

def run_chatbot():
  messages =  [  
  {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
  {'role':'user', 'content':'tell me a joke'},   
  {'role':'assistant', 'content':'Why did the chicken cross the road'},   
  {'role':'user', 'content':'I don\'t know'}  ]
  
  messages1 =  [  
  {'role':'system', 'content':'You are friendly chatbot.'},    
  {'role':'user', 'content':'Hi, my name is Isa'}  ]
  
  messages2 =  [  
  {'role':'system', 'content':'You are friendly chatbot.'},    
  {'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
  
  messages =  [  
  {'role':'system', 'content':'You are friendly chatbot.'},
  {'role':'user', 'content':'Hi, my name is Isa'},
  {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
  Is there anything I can help you with today?"},
  {'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
  
  response = get_completion_from_messages(messages, temperature=1)
  print(response)