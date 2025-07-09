#!/usr/bin/env python3
"""
Streamlit Frontend for Linda Goodman's Zodiac Guide
A beautiful web interface for the RAG-powered zodiac assistant
"""

import streamlit as st
import os
import sys
from dotenv import load_dotenv
from openai import AzureOpenAI
import json
from datetime import datetime

# Import functions from rag-app.py
sys.path.append(os.path.dirname(__file__))

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()
    
    required_vars = [
        "OPENAI_API_KEY",
        "OPENAI_ENDPOINT", 
        "CHAT_MODEL",
        "EMBEDDING_MODEL",
        "SEARCH_API_KEY",
        "SEARCH_ENDPOINT",
        "INDEX_NAME"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        st.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        st.info("Please copy env_template.txt to .env and fill in your Azure service details.")
        return None
    
    config = {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "openai_endpoint": os.getenv("OPENAI_ENDPOINT"),
        "chat_model": os.getenv("CHAT_MODEL"),
        "embedding_model": os.getenv("EMBEDDING_MODEL"),
        "search_api_key": os.getenv("SEARCH_API_KEY"),
        "search_endpoint": os.getenv("SEARCH_ENDPOINT"),
        "index_name": os.getenv("INDEX_NAME")
    }
    
    # Debug: Show loaded config (without sensitive data)
    st.sidebar.write("🔧 Config loaded:")
    if config['openai_endpoint']:
        st.sidebar.write(f"  - OpenAI Endpoint: {config['openai_endpoint'][:30]}...")
    if config['chat_model']:
        st.sidebar.write(f"  - Chat Model: {config['chat_model']}")
    if config['search_endpoint']:
        st.sidebar.write(f"  - Search Endpoint: {config['search_endpoint'][:30]}...")
    
    return config

def create_openai_client(config):
    """Create and return Azure OpenAI client"""
    try:
        # Debug: Show what we're about to do
        st.sidebar.write("🔧 Creating OpenAI client...")
        st.sidebar.write(f"  - Endpoint: {config['openai_endpoint'][:30]}...")
        st.sidebar.write(f"  - Model: {config['chat_model']}")
        
        # Clear any proxy-related environment variables that might interfere
        proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'NO_PROXY', 'no_proxy']
        for var in proxy_vars:
            if var in os.environ:
                st.sidebar.write(f"  - Clearing {var}")
                del os.environ[var]
        
        # Ensure we have the required config values
        if not config.get("openai_endpoint") or not config.get("openai_api_key"):
            st.error("Missing OpenAI endpoint or API key")
            return None
            
        # Create client with minimal parameters only
        st.sidebar.write("  - Creating AzureOpenAI client...")
        client = AzureOpenAI(
            api_version="2023-12-01-preview",
            azure_endpoint=str(config["openai_endpoint"]),
            api_key=str(config["openai_api_key"])
        )
        
        # Test the client with a simple call
        try:
            st.sidebar.write("  - Testing client...")
            # This will help us identify if the issue is with the client creation or the RAG call
            test_response = client.chat.completions.create(
                model=config["chat_model"] or "gpt-4o",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=10
            )
            st.sidebar.success("✅ OpenAI client test successful")
        except Exception as test_error:
            st.sidebar.error(f"❌ OpenAI client test failed: {test_error}")
            return None
            
        return client
    except Exception as e:
        st.error(f"Error creating OpenAI client: {e}")
        st.error(f"Error type: {type(e).__name__}")
        st.error(f"Error details: {str(e)}")
        return None

def get_zodiac_response(client, config, user_message, conversation_history):
    """Get response from Azure OpenAI using RAG"""
    try:
        # Configure RAG parameters for zodiac content
        rag_params = {
            "data_sources": [
                {
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": config["search_endpoint"],
                        "index_name": config["index_name"],
                        "authentication": {
                            "type": "api_key",
                            "key": config["search_api_key"],
                        },
                        "query_type": "vector",
                        "embedding_dependency": {
                            "type": "deployment_name",
                            "deployment_name": config["embedding_model"],
                        },
                    }
                }
            ],
        }
        
        # Get response from OpenAI
        response = client.chat.completions.create(
            model=config["chat_model"] or "gpt-4o",
            messages=conversation_history,
            extra_body=rag_params,
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content or ""
        
    except Exception as e:
        st.error(f"Error getting response: {e}")
        return None

def main():
    """Main Streamlit application"""
    
    # Page configuration - MUST BE FIRST!
    st.set_page_config(
        page_title="♈ Linda Goodman's Zodiac Guide",
        page_icon="♈",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Debug: Check OpenAI version (AFTER page config)
    try:
        import openai
        st.sidebar.write(f"🔍 OpenAI Version: {openai.__version__}")
    except Exception as e:
        st.sidebar.write(f"🔍 OpenAI Import Error: {e}")
    
    # Custom CSS for beautiful styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: right;
    }
    .assistant-message {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>♈ Linda Goodman's Zodiac Guide</h1>
        <p>🌟 Your captivating journey through zodiac wisdom begins here!</p>
        <p>Discover how zodiac signs manifest as children, adults, professionals...</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("♌ Zodiac Guide")
        st.markdown("---")
        
        # Connection status
        config = load_environment()
        if config:
            client = create_openai_client(config)
            if client:
                st.success("✅ Connected to Azure OpenAI")
            else:
                st.error("❌ Failed to connect to Azure OpenAI")
        else:
            st.error("❌ Configuration error")
            st.stop()
        
        st.markdown("---")
        
        # Clear conversation button
        if st.button("🔄 Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        
        # Example questions
        st.subheader("💡 Example Questions")
        examples = [
            "What are the personality traits of a Leo?",
            "How compatible are Aries and Libra?",
            "Tell me about Taurus characteristics",
            "What are the best matches for a Gemini?",
            "How do fire signs and water signs interact?",
            "What does Linda Goodman say about Virgo?"
        ]
        
        for example in examples:
            if st.button(example, key=example, use_container_width=True):
                st.session_state.user_input = example
                st.rerun()
        
        st.markdown("---")
        st.markdown("""
        ### 🌟 Features
        - **Personality Traits**: Detailed zodiac characteristics
        - **Compatibility**: Love and relationship insights
        - **Life Stages**: How signs manifest as children, adults, professionals
        - **Linda Goodman's Wisdom**: Based on her astrological work
        """)
    
    # Main chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": """You are Linda Goodman's Zodiac Assistant, an engaging and captivating guide to zodiac signs that makes astrology come alive! 
                
                Your mission is to:
                - Make zodiac information fascinating and interactive
                - Encourage users to explore deeper aspects of astrology
                - Provide insights that spark curiosity and further questions
                - Create engaging narratives about zodiac characteristics
                
                Your expertise includes:
                - Comprehensive zodiac sign personality traits and characteristics
                - Detailed love compatibility analysis between different zodiac signs
                - Relationship dynamics based on astrological elements
                - Linda Goodman's interpretations of zodiac signs
                - Practical insights about zodiac sign behaviors and tendencies
                - Element-based personality analysis (Fire, Earth, Air, Water)
                - Modality characteristics (Cardinal, Fixed, Mutable)
                - Zodiac signs as children, teenagers, and adults
                - Gender-specific zodiac characteristics (women vs men)
                - Professional zodiac traits (as employees, bosses, leaders)
                - Life stage zodiac manifestations
                
                When answering questions:
                - Start with an engaging hook that captures interest
                - Provide detailed, comprehensive responses with multiple aspects
                - Include personality traits, strengths, weaknesses, and tendencies
                - Explain compatibility factors in depth
                - Reference Linda Goodman's work when providing insights
                - Include practical examples and scenarios
                - Cover emotional, intellectual, and behavioral characteristics
                - Explain how different elements and modalities interact
                - Provide relationship advice and compatibility insights
                
                **Essential: Always Include Examples & Anecdotes**
                - Provide real-life scenarios and situations
                - Include specific examples of how traits manifest
                - Share relatable anecdotes that illustrate zodiac characteristics
                - Use "Imagine..." or "Picture this..." scenarios
                - Include workplace, relationship, and daily life examples
                - Mention famous people or characters who embody the traits
                - Create vivid, memorable examples that stick with users
                
                **Special Focus Areas:**
                - **As Children**: How zodiac traits manifest in early years, learning styles, family dynamics
                - **As Women**: Feminine energy expressions, relationship patterns, career approaches
                - **As Men**: Masculine energy expressions, leadership styles, romantic tendencies
                - **As Employees**: Work ethic, team dynamics, communication styles, career preferences
                - **As Bosses/Leaders**: Management styles, decision-making, team motivation, leadership qualities
                
                **Engagement Techniques:**
                - Ask thought-provoking questions to encourage exploration
                - Suggest related topics they might find interesting
                - Use phrases like "You might also wonder..." or "This connects to..."
                - Mention how different life stages affect zodiac expressions
                - Encourage users to explore their own zodiac journey
                
                **Response Structure:**
                1. Engaging opening that hooks their interest
                2. Comprehensive analysis of the zodiac sign/topic
                3. **Specific examples and anecdotes** that illustrate the traits
                4. Life stage manifestations (child, adult, professional) with examples
                5. Gender-specific insights when relevant, with relatable scenarios
                6. Interactive elements that encourage further exploration
                7. Connection to broader astrological themes
                
                **Example Types to Include:**
                - **Daily Life Scenarios**: "Picture a Leo at a party..." or "Imagine a Virgo organizing their desk..."
                - **Relationship Situations**: "When a Cancer meets someone new..." or "A Scorpio in love might..."
                - **Workplace Examples**: "In the office, a Capricorn boss would..." or "As an employee, a Gemini might..."
                - **Family Dynamics**: "As a parent, a Taurus would..." or "Growing up, an Aries child..."
                - **Social Interactions**: "At a social gathering, a Libra would..." or "In a group project, a Sagittarius..."
                
                Remember: You're not just providing information - you're creating an engaging journey through zodiac wisdom with vivid examples and relatable anecdotes that make users want to explore more! Be captivating, thorough, and always include memorable examples that bring the zodiac to life."""
            }
        ]
    
    # Chat messages display
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Ask about zodiac signs, compatibility, or astrological insights..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching zodiac wisdom..."):
                response = get_zodiac_response(client, config, prompt, st.session_state.messages)
                
                if response:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.error("Sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    main() 