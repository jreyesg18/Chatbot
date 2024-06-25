import openai

openai.api_key = 'Ingrese key'

def chat_gpt(pregunta):
    consulta = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= [{"role":"user","content":"Que es Python"}])
    return consulta.choices[0].message.content.strip()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    consulta = chat_gpt(user_input)
    print("chatbot: ", consulta)