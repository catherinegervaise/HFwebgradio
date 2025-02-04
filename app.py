import openai
import gradio as gr

# 🟢 Set up OpenAI API Key (replace with your actual key)
openai.api_key = "your-api-key"

def greet(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

def chatbot_response(user_query):
    """
    Generates an IT support response using OpenAI's GPT model.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an IT support assistant."},
                  {"role": "user", "content": user_query}],
        max_tokens=150,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()

# 🟢 Create Gradio Web Interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="IT Support Chatbot",
    description="Ask any IT-related question, and the chatbot will assist you."
)

# 🟢 Run the Chatbot
if __name__ == "__main__":
    iface.launch()
