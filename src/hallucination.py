from utils.helpers import get_completion

def hallucinate():
  """ --- Model Limitations: Hallucinations --- """

""" --- Boie is a real company, the product name is not real. --- """

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = get_completion(prompt)
print(response)