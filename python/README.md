# Linda Goodman's Zodiac Guide

A Python-based Retrieval Augmented Generation (RAG) zodiac assistant that uses Azure AI services to provide practical insights about zodiac signs and compatibility based on Linda Goodman's astrological work.

## Features

- ♈ Provides detailed information about zodiac sign characteristics and personality traits
- ♌ Love compatibility analysis between different zodiac signs
- ♎ Relationship dynamics and astrological insights
- 📚 Grounded responses based on Linda Goodman's zodiac interpretations
- 💬 Interactive command-line zodiac consultation with conversation history
- ⚡ Real-time responses with practical astrological guidance

## Prerequisites

Before running this application, you need to set up the following Azure resources:

### 1. Azure OpenAI Service
- Deploy GPT-4o model
- Deploy text-embedding-ada-002 model
- Note down your endpoint URL and API key

### 2. Azure AI Search Service
- Create a search service
- Create an index containing Linda Goodman's zodiac content
- Upload and index astrology books, articles, or content
- Note down your search endpoint and API key

## Setup Instructions

### Step 1: Clone and Navigate
```bash
cd mslearn-ai-studio/labfiles/rag-app/python
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv labenv

# Activate virtual environment
# On Windows:
.\labenv\Scripts\activate
# On macOS/Linux:
source labenv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
1. Copy the environment template:
   ```bash
   copy env_template.txt .env
   ```

2. Edit the `.env` file and fill in your Azure service details:
   ```ini
   # Azure OpenAI Configuration
   OPENAI_API_KEY=your_actual_openai_api_key
   OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   CHAT_MODEL=gpt-4o
   EMBEDDING_MODEL=text-embedding-ada-002

   # Azure AI Search Configuration
   SEARCH_API_KEY=your_actual_search_api_key
   SEARCH_ENDPOINT=https://your-search-service.search.windows.net
   INDEX_NAME=zodiac-index
   ```

### Step 5: Run the Application
```bash
python rag-app.py
```

## Azure Resource Setup Guide

### Setting up Azure OpenAI Service

1. **Create Azure OpenAI Resource**
   - Go to Azure Portal → Create Resource
   - Search for "Azure OpenAI"
   - Create a new Azure OpenAI resource
   - Choose your subscription, resource group, and region

2. **Deploy Models**
   - Go to your Azure OpenAI resource
   - Navigate to "Model deployments"
   - Deploy GPT-4o model
   - Deploy text-embedding-ada-002 model
   - Note the deployment names

3. **Get API Key and Endpoint**
   - Go to "Keys and Endpoint" section
   - Copy Key 1 or Key 2
   - Copy the endpoint URL

### Setting up Azure AI Search for Zodiac Content

1. **Create Search Service**
   - Go to Azure Portal → Create Resource
   - Search for "Azure AI Search"
   - Create a new search service
   - Choose your subscription, resource group, and region

2. **Create Index**
   - Go to your search service
   - Navigate to "Indexes" → "Add index"
   - Name: `zodiac-index` (or your preferred name)
   - Add fields for zodiac content (title, content, sign, chapter, etc.)
   - Enable vector search capabilities

3. **Upload Zodiac Content**
   - Go to "Import data"
   - Choose your data source (Blob Storage with PDFs/books)
   - Upload Linda Goodman's books or zodiac content
   - Configure the import to extract text from documents
   - Run the import

4. **Get API Key and Endpoint**
   - Go to "Keys" section
   - Copy Admin key
   - Note the search service URL

## Usage

Once the application is running:

1. **Ask Zodiac Questions**: Type questions about zodiac signs, personality traits, or compatibility
2. **Get Zodiac Insights**: The bot will search Linda Goodman's teachings and provide practical answers
3. **Explore Compatibility**: Ask about relationships between different zodiac signs
4. **Clear Reading**: Type `clear` to start a new zodiac consultation
5. **Exit**: Type `quit` to exit the application

## Example Questions

- "What are the personality traits of a Leo?"
- "How compatible are Aries and Libra?"
- "What does Linda Goodman say about Scorpio characteristics?"
- "Tell me about Taurus personality"
- "What are the best matches for a Gemini?"
- "How do fire signs and water signs interact?"
- "What are the typical traits of a Virgo?"

## Troubleshooting

### Common Issues

1. **Missing Environment Variables**
   - Ensure all variables in `.env` are filled in
   - Check that the file is named exactly `.env`

2. **Authentication Errors**
   - Verify your API keys are correct
   - Ensure your Azure resources are in the same region

3. **Model Not Found**
   - Confirm your model deployments are active
   - Check the deployment names match your `.env` file

4. **Search Index Issues**
   - Verify your search index exists and has zodiac content
   - Check that vector search is enabled

### Getting Help

- Check Azure Portal for service status
- Verify your resource permissions
- Ensure your virtual environment is activated

## File Structure

```
python/
├── rag-app.py              # Main zodiac guide application (command-line)
├── requirements.txt        # Python dependencies
├── env_template.txt        # Environment variables template
├── .env                    # Your environment variables (create this)
├── setup.py               # Setup automation script
├── test_connection.py     # Connection testing script
├── README.md              # This file
└── QUICKSTART.md          # Quick start guide
```

## Content Recommendations

For the best experience, consider uploading these types of content to your Azure AI Search index:

- Linda Goodman's "Sun Signs"
- Linda Goodman's "Love Signs"
- Linda Goodman's "Star Signs"
- Other zodiac and astrology books
- Zodiac compatibility guides
- Personality trait descriptions

## Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure
- Use appropriate Azure RBAC permissions
- Consider using Azure Key Vault for production deployments 