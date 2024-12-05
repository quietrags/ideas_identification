import chainlit as cl
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama3-8b-8192"  # This is the model identifier for Llama 3.1-8b on Groq

# Load system prompt
with open("prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

@cl.on_chat_start
async def start():
    """Initialize the chat session."""
    # Initialize chat history in the user session with system prompt
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    cl.user_session.set("messages", messages)
    welcome_message = """👋 Hello! I'm your text analysis assistant powered by Llama.

I'm configured to help you analyze text and extract:
- Core Ideas (Main ideas, Supporting ideas, Context, Counterpoints)
- Relationships between ideas
- Analogies and their implications
- Updated insights and key takeaways

Simply paste the text you'd like to analyze, and I'll break it down for you following this structured approach."""

    await cl.Message(content=welcome_message).send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses using Groq."""
    try:
        # Get chat history
        messages = cl.user_session.get("messages")
        
        # Add user message to history
        messages.append({"role": "user", "content": message.content})
        
        # Create the chat completion
        completion = client.chat.completions.create(
            messages=messages,
            model=MODEL,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=True  # Enable streaming for better UX
        )

        # Initialize response message
        response_message = cl.Message(content="")
        await response_message.send()

        # Stream the response
        full_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                await response_message.stream_token(content)

        # Add assistant's message to history
        messages.append({"role": "assistant", "content": full_response})
        
        # Update chat history in session
        cl.user_session.set("messages", messages)

        # Send the final streaming message
        await response_message.send()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

if __name__ == "__main__":
    print("Starting the Chainlit app...")
