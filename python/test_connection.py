#!/usr/bin/env python3
"""
Test connection to Azure OpenAI and Azure Cognitive Search
"""

import os
import sys
from dotenv import load_dotenv
from openai import AzureOpenAI

def test_openai_connection():
    """Test Azure OpenAI connection"""
    print("🔍 Testing Azure OpenAI connection...")
    
    # Load environment variables
    load_dotenv()
    
    # Get required environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_endpoint = os.getenv("OPENAI_ENDPOINT")
    chat_model = os.getenv("CHAT_MODEL")
    
    if not all([openai_api_key, openai_endpoint, chat_model]):
        print("❌ Missing required environment variables:")
        if not openai_api_key:
            print("   - OPENAI_API_KEY")
        if not openai_endpoint:
            print("   - OPENAI_ENDPOINT")
        if not chat_model:
            print("   - CHAT_MODEL")
        return False
    
    try:
        # Clear proxy environment variables
        proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']
        for var in proxy_vars:
            if var in os.environ:
                del os.environ[var]
        
        # Create client (type assertions for linter)
        client = AzureOpenAI(
            api_version="2023-12-01-preview",
            azure_endpoint=str(openai_endpoint),
            api_key=str(openai_api_key)
        )
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model=str(chat_model),
            messages=[
                {"role": "user", "content": "Hello! Please respond with 'Connection successful!'"}
            ],
            max_tokens=50
        )
        
        print("✅ Azure OpenAI connection successful!")
        print(f"📝 Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Azure OpenAI connection failed: {e}")
        return False

def test_search_connection():
    """Test Azure Cognitive Search connection"""
    print("\n🔍 Testing Azure Cognitive Search connection...")
    
    # Get required environment variables
    search_api_key = os.getenv("SEARCH_API_KEY")
    search_endpoint = os.getenv("SEARCH_ENDPOINT")
    index_name = os.getenv("INDEX_NAME")
    
    if not all([search_api_key, search_endpoint, index_name]):
        print("❌ Missing required environment variables:")
        if not search_api_key:
            print("   - SEARCH_API_KEY")
        if not search_endpoint:
            print("   - SEARCH_ENDPOINT")
        if not index_name:
            print("   - INDEX_NAME")
        return False
    
    try:
        from azure.search.documents import SearchClient
        from azure.core.credentials import AzureKeyCredential
        
        # Create search client (type assertions for linter)
        search_client = SearchClient(
            endpoint=str(search_endpoint),
            index_name=str(index_name),
            credential=AzureKeyCredential(str(search_api_key))
        )
        
        # Test search
        results = search_client.search(search_text="zodiac", top=1)
        count = 0
        for result in results:
            count += 1
            break
        
        print("✅ Azure Cognitive Search connection successful!")
        print(f"📊 Found {count} document(s) in search test")
        return True
        
    except Exception as e:
        print(f"❌ Azure Cognitive Search connection failed: {e}")
        return False

def main():
    """Main test function"""
    print("🌟 Testing Backend Connections")
    print("=" * 40)
    
    # Test OpenAI connection
    openai_success = test_openai_connection()
    
    # Test Search connection
    search_success = test_search_connection()
    
    print("\n" + "=" * 40)
    if openai_success and search_success:
        print("🎉 All connections successful! Your backend is ready.")
        print("💡 You can now run: python rag-app.py")
    else:
        print("❌ Some connections failed. Please check your environment variables.")
        print("📝 Make sure your .env file is properly configured.")

if __name__ == '__main__':
    main() 