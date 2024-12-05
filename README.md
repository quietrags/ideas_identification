# Ideas Identification

A modern chat interface powered by Llama 3.1-8b through Groq's API, built with Chainlit. This application provides a responsive and intuitive way to interact with the Llama language model.

## Features

- Real-time streaming responses
- Persistent chat history within sessions
- Modern, responsive UI powered by Chainlit
- High-performance inference using Groq's API
- Secure environment variable handling

## Prerequisites

- Python 3.9+
- A Groq API key (get it from [Groq Console](https://console.groq.com/keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ideas_identification.git
cd ideas_identification
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```
Then edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the application:
```bash
chainlit run app.py -w
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Start chatting with the model!

## Configuration

The application can be configured through the following files:
- `.env`: Environment variables including API keys
- `chainlit.md`: Customize the welcome message and chat interface
- `app.py`: Adjust model parameters like temperature and max tokens

## Model Parameters

Current configuration:
- Model: `llama3-8b-8192`
- Temperature: 0.7
- Max Tokens: 1024
- Top P: 1.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Chainlit](https://github.com/Chainlit/chainlit)
- Powered by [Groq](https://groq.com/)
- Uses [Llama 3.1](https://arxiv.org/abs/2402.17764) model