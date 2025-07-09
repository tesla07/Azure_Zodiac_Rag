<<<<<<< HEAD
# ♈ Linda Goodman's Zodiac Guide

A powerful Retrieval Augmented Generation (RAG) application that provides detailed zodiac insights based on Linda Goodman's astrological work. Built with Azure AI services and available as both a command-line tool and a beautiful web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-GPT--4o-green.svg)
![Azure Search](https://img.shields.io/badge/Azure%20Search-Vector%20Search-orange.svg)

## 🌟 Features

- **♈ Comprehensive Zodiac Analysis**: Detailed personality traits, characteristics, and behaviors
- **♌ Love Compatibility**: In-depth relationship analysis between different zodiac signs
- **📚 Linda Goodman's Wisdom**: Grounded responses based on her astrological interpretations
- **💬 Dual Interface**: Both command-line and beautiful web interface
- **⚡ Real-time RAG**: Powered by Azure OpenAI and Azure Cognitive Search
- **🎨 Beautiful UI**: Modern Streamlit interface with zodiac-themed design
- **🔄 Conversation Memory**: Maintains context across multiple interactions

## 🏗️ Architecture

```
User Interface (CLI/Web) → RAG Engine → Azure OpenAI + Azure Cognitive Search
```

- **Frontend**: Streamlit web interface + Command-line interface
- **Backend**: Python RAG application
- **AI Services**: Azure OpenAI (GPT-4o) + Azure Cognitive Search
- **Data**: Linda Goodman's zodiac content indexed for vector search

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure subscription with:
  - Azure OpenAI Service (GPT-4o deployed)
  - Azure AI Search Service (with zodiac content indexed)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd linda-goodman-zodiac-guide
   ```

2. **Navigate to the Python directory**
   ```bash
   cd python
   ```

3. **Run the setup script**
   ```bash
   python setup.py
   ```

4. **Configure your Azure services**
   ```bash
   # Copy environment template
   copy env_template.txt .env
   
   # Edit .env with your Azure credentials
   notepad .env
   ```

5. **Activate virtual environment and install dependencies**
   ```bash
   # Windows
   .\labenv\Scripts\activate
   
   # macOS/Linux
   source labenv/bin/activate
   
   pip install -r requirements.txt
   ```

### Usage

#### 🌐 Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```
Then open http://localhost:8501 in your browser.

#### 💻 Command Line Interface
```bash
python rag-app.py
```

#### 🧪 Test Connections
```bash
python test_connection.py
```

## 📁 Project Structure

```
linda-goodman-zodiac-guide/
├── python/
│   ├── rag-app.py              # Command-line RAG application
│   ├── streamlit_app.py        # Web interface using Streamlit
│   ├── test_connection.py      # Azure service connection testing
│   ├── setup.py               # Automated setup script
│   ├── requirements.txt       # Python dependencies
│   ├── env_template.txt       # Environment variables template
│   ├── README.md              # Detailed setup instructions
│   └── QUICKSTART.md          # Quick start guide
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `python/` directory:

```ini
# Azure OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
CHAT_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-ada-002

# Azure AI Search Configuration
SEARCH_API_KEY=your_search_api_key_here
SEARCH_ENDPOINT=https://your-search-service.search.windows.net
INDEX_NAME=zodiac-index
```

### Azure Setup

1. **Azure OpenAI Service**
   - Deploy GPT-4o model
   - Deploy text-embedding-ada-002 model
   - Get API key and endpoint

2. **Azure AI Search**
   - Create search service with vector search
   - Create index for zodiac content
   - Upload Linda Goodman's books/content
   - Get API key and endpoint

## 💡 Example Questions

- "What are the personality traits of a Leo?"
- "How compatible are Aries and Libra?"
- "Tell me about Taurus characteristics"
- "What are the best matches for a Gemini?"
- "How do fire signs and water signs interact?"
- "What does Linda Goodman say about Virgo?"

## 🎨 Features in Detail

### Web Interface
- **Beautiful Design**: Zodiac-themed gradients and styling
- **Interactive Chat**: Real-time conversation with the AI
- **Example Questions**: Quick-access buttons for common queries
- **Connection Status**: Real-time Azure service status
- **Conversation Management**: Clear and reset functionality

### Command Line Interface
- **Interactive Mode**: Engaging terminal-based experience
- **Conversation History**: Maintains context across sessions
- **Clear Commands**: Easy navigation and control
- **Rich Output**: Formatted responses with examples

### RAG Capabilities
- **Vector Search**: Semantic search through zodiac content
- **Context-Aware**: Understands conversation flow
- **Source Grounding**: Responses based on Linda Goodman's work
- **Comprehensive Coverage**: Personality, compatibility, life stages

## 🔍 Troubleshooting

### Common Issues

1. **Missing Environment Variables**
   - Ensure all variables in `.env` are filled in
   - Check file permissions and location

2. **Azure Connection Errors**
   - Verify API keys are correct
   - Ensure resources are in the same region
   - Check model deployments are active

3. **Virtual Environment Issues**
   - Use CMD instead of PowerShell for activation
   - Reinstall packages if needed: `pip install -r requirements.txt`

### Getting Help

- Check Azure Portal for service status
- Run `python test_connection.py` to diagnose issues
- Verify your virtual environment is activated

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Linda Goodman**: For her comprehensive astrological work
- **Azure AI Services**: For providing the AI infrastructure
- **Streamlit**: For the beautiful web framework
- **OpenAI**: For the powerful language models

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the detailed README in the `python/` directory
3. Open an issue on GitHub

---

**🌟 Ready to explore the fascinating world of zodiac signs? Start your journey with Linda Goodman's wisdom!** 
=======
# Azure_Zodiac_Rag
>>>>>>> 095754c48b916a5e1a05f88dfcf6ddf6d69f7308
