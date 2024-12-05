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

def create_analysis_prompt(text_to_analyze):
    return f"""Please analyze the following text according to the provided framework:

TEXT TO ANALYZE:
{text_to_analyze}

Please provide a structured analysis following these steps:
1. Identify Core Ideas (Main Ideas, Supporting Ideas, Context, Counterpoints)
2. Identify Relationships between ideas (Causal, Contrast/Comparison, Sequential, Hierarchical, Associative)
3. Unpack any Analogies present
4. Generate Updated Insights

Please format your response clearly with appropriate headings and bullet points."""

@cl.on_chat_start
async def start():
    """Initialize the chat session."""
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
        
        # Create analysis prompt with the user's text
        analysis_request = create_analysis_prompt(message.content)
        
        # Set up the messages for the API call
        api_messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": analysis_request}
        ]
        
        # Create the chat completion
        completion = client.chat.completions.create(
            messages=api_messages,
            model=MODEL,
            temperature=0.7,
            max_tokens=2048,  # Increased for longer analyses
            top_p=1,
            stream=True
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

        # Add the interaction to chat history
        messages.extend([
            {"role": "user", "content": message.content},
            {"role": "assistant", "content": full_response}
        ])
        
        # Update chat history in session
        cl.user_session.set("messages", messages)

        # Send the final streaming message
        await response_message.send()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

if __name__ == "__main__":
    print("Starting the Chainlit app...")
