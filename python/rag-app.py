import os
import sys
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

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
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please copy env_template.txt to .env and fill in your values.")
        print("🔗 See README.md for setup instructions.")
        sys.exit(1)
    
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "openai_endpoint": os.getenv("OPENAI_ENDPOINT"),
        "chat_model": os.getenv("CHAT_MODEL"),
        "embedding_model": os.getenv("EMBEDDING_MODEL"),
        "search_api_key": os.getenv("SEARCH_API_KEY"),
        "search_endpoint": os.getenv("SEARCH_ENDPOINT"),
        "index_name": os.getenv("INDEX_NAME")
    }

def create_openai_client(config):
    """Create and return Azure OpenAI client"""
    try:
        client = AzureOpenAI(
            api_version="2023-12-01-preview",
            azure_endpoint=config["openai_endpoint"],
            api_key=config["openai_api_key"]
        )
        return client
    except Exception as e:
        print(f"❌ Error creating OpenAI client: {e}")
        sys.exit(1)

def format_response_with_sources(response_text, sources=None):
    """Format the response with source citations"""
    formatted_response = response_text
    
    if sources:
        formatted_response += "\n\n📚 **Sources:**\n"
        for i, source in enumerate(sources, 1):
            if isinstance(source, dict):
                # Extract relevant information from source
                title = source.get('title', 'Unknown')
                content = source.get('content', '')[:200] + "..." if len(source.get('content', '')) > 200 else source.get('content', '')
                formatted_response += f"{i}. **{title}**\n   {content}\n\n"
            else:
                formatted_response += f"{i}. {str(source)}\n"
    
    return formatted_response

def main():
    """Main application function"""
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("♈ Linda Goodman's Zodiac Guide")
    print("=" * 50)
    print("🌟 Your captivating journey through zodiac wisdom begins here!")
    print("Discover how zodiac signs manifest as children, adults, professionals...")
    print("Explore the fascinating world of astrological personalities!\n")
    
    try:
        # Load configuration
        print("📋 Loading configuration...")
        config = load_environment()
        print("✅ Configuration loaded successfully")
        
        # Create OpenAI client
        print("🔗 Connecting to Azure OpenAI...")
        client = create_openai_client(config)
        print("✅ Connected to Azure OpenAI")
        
        # Initialize conversation history with zodiac-focused system message
        conversation = [
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
        
        print("\n♌ Ready to explore the fascinating world of zodiac signs!")
        print("Ask about any sign as a child, adult, professional, or in relationships...")
        print("Type 'quit' to exit, 'clear' to start a new exploration.")
        print("-" * 50)
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = input("\n♈ You: ").strip()
                
                if user_input.lower() == "quit":
                    print("👋 Thanks for exploring the zodiac! Goodbye!")
                    break
                    
                if user_input.lower() == "clear":
                    conversation = [conversation[0]]  # Keep system message
                    print("🔄 Starting a new zodiac reading...")
                    continue
                    
                if not user_input:
                    print("❌ Please ask me about zodiac signs!")
                    continue
                
                # Add user message to conversation
                conversation.append({"role": "user", "content": user_input})
                
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
                
                print("🔍 Searching zodiac information...")
                
                # Get response from OpenAI
                response = client.chat.completions.create(
                    model=config["chat_model"] or "gpt-4o",  # Provide fallback if None
                    messages=conversation,  # type: ignore
                    extra_body=rag_params,
                    temperature=0.7,  # Balanced for informative responses
                    max_tokens=2000  # Increased for more verbose responses
                )
                
                # Extract response content
                assistant_response = response.choices[0].message.content
                
                # Add assistant response to conversation
                conversation.append({"role": "assistant", "content": assistant_response or ""})
                
                # Display formatted response
                print(f"\n♌ Zodiac Guide: {assistant_response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for exploring the zodiac! Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again or type 'quit' to exit.")
                # Remove the last user message from conversation to retry
                if conversation and conversation[-1]["role"] == "user":
                    conversation.pop()
    
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()