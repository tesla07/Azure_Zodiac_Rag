# Quick Start Guide - Linda Goodman's Zodiac Guide

Get your zodiac sign assistant running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to:
  - Azure OpenAI Service (with GPT-4o and text-embedding-ada-002 deployed)
  - Azure AI Search Service (with zodiac content indexed)

## Quick Setup

### 1. Run the Setup Script
```bash
python setup.py
```

This will:
- ✅ Check Python version
- ✅ Create virtual environment (`labenv`)
- ✅ Install dependencies
- ✅ Create `.env` file from template

### 2. Configure Your Azure Services

Edit the `.env` file with your actual Azure service details:

```ini
# Replace these with your actual values from Azure Portal
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
CHAT_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-ada-002
SEARCH_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SEARCH_ENDPOINT=https://your-search-service.search.windows.net
INDEX_NAME=zodiac-index
```

### 3. Activate Environment and Run

**Windows:**
```bash
.\labenv\Scripts\activate
python rag-app.py
```

**macOS/Linux:**
```bash
source labenv/bin/activate
python rag-app.py
```

### 4. Start Your Zodiac Consultation!

Once the guide is running, you can:
- Ask about zodiac sign personality traits
- Explore compatibility between different signs
- Get relationship insights based on Linda Goodman's work
- Type `clear` to start a new zodiac reading
- Type `quit` to exit

## Getting Your Azure Credentials

### Azure OpenAI Service
1. Go to Azure Portal → Your OpenAI resource
2. Navigate to "Keys and Endpoint"
3. Copy Key 1 and Endpoint URL

### Azure AI Search
1. Go to Azure Portal → Your Search service
2. Navigate to "Keys"
3. Copy Admin key
4. Note the Search service URL

## Example Zodiac Questions

- "What are the key traits of a Cancer?"
- "How compatible are Gemini and Sagittarius?"
- "What does Linda Goodman say about Virgo personality?"
- "Tell me about Aries characteristics"
- "What are the best matches for an Aquarius?"

## Need Help?

- 📖 See [README.md](README.md) for detailed instructions
- 🔧 Run `python setup.py` again if you encounter issues
- 🧪 Run `python test_connection.py` to test your Azure connections
- 💡 Check that your Azure resources are in the same region 