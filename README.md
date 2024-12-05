# Ideas Identification

A sophisticated text analysis tool powered by Llama 3.1-8b through Groq's API, built with Chainlit. This application helps analyze text content by identifying core ideas, relationships, analogies, and generating insights.

## Features

- 🔍 Comprehensive text analysis following a structured framework:
  - Core Ideas identification (Main, Supporting, Context, Counterpoints)
  - Relationship mapping between ideas
  - Analogy analysis
  - Insight generation
- 🚀 Real-time streaming responses
- 💬 Persistent chat history within sessions
- 🎯 Focused analysis prompts
- ⚡ High-performance inference using Groq's API
- 🛡️ Secure environment variable handling

## Analysis Framework

The tool analyzes text using the following structured approach:

1. **Core Ideas**
   - Main Ideas: Central propositions or themes
   - Supporting Ideas: Details, examples, or evidence
   - Contextual Elements: Background and framing devices
   - Counterpoints: Risks, challenges, or opposing views

2. **Relationships**
   - Causal relationships
   - Contrast/Comparison
   - Sequential progression
   - Hierarchical connections
   - Associative links

3. **Analogies**
   - Comparative elements
   - Supporting concepts
   - Implications and risks

4. **Updated Insights**
   - Evolution of ideas
   - Key takeaways
   - Trade-offs and considerations

## Prerequisites

- Python 3.9+
- A Groq API key (get it from [Groq Console](https://console.groq.com/keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/quietrags/ideas_identification.git
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

3. Paste any text you want to analyze into the chat interface
4. The system will provide a structured analysis following the framework

## Example Analysis

Input any text, such as articles, papers, or documents, and receive a structured analysis that includes:

```
1. Core Ideas
   - Main Ideas: [Key themes and central arguments]
   - Supporting Ideas: [Evidence and examples]
   - Context: [Background information]
   - Counterpoints: [Challenges and opposing views]

2. Relationships
   - [Identified connections between ideas]
   - [Cause-effect relationships]
   - [Comparisons and contrasts]

3. Analogies
   - [Analysis of comparative elements]
   - [Implications and insights]

4. Updated Insights
   - [Key takeaways]
   - [Synthesized understanding]
   - [Practical implications]
```

## Configuration

The application can be configured through:
- `.env`: Environment variables including API keys
- `prompt.txt`: System prompt defining the analysis framework
- `app.py`: Model parameters and application settings

## Model Parameters

Current configuration:
- Model: `llama3-8b-8192`
- Temperature: 0.7
- Max Tokens: 2048
- Top P: 1.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Chainlit](https://github.com/Chainlit/chainlit)
- Powered by [Groq](https://groq.com/)
- Uses [Llama 3.1](https://arxiv.org/abs/2402.17764) model