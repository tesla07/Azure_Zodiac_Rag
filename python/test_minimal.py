#!/usr/bin/env python3
"""
Minimal test to isolate the proxies issue
"""

import os
import sys
from dotenv import load_dotenv

def test_minimal_openai():
    """Test minimal OpenAI client creation"""
    print("🔍 Testing minimal OpenAI client creation...")
    
    # Load environment variables
    load_dotenv()
    
    # Get required environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_endpoint = os.getenv("OPENAI_ENDPOINT")
    chat_model = os.getenv("CHAT_MODEL")
    
    if not all([openai_api_key, openai_endpoint, chat_model]):
        print("❌ Missing required environment variables")
        return False
    
    try:
        # Clear proxy environment variables
        proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'NO_PROXY', 'no_proxy']
        for var in proxy_vars:
            if var in os.environ:
                print(f"  - Clearing {var}")
                del os.environ[var]
        
        # Check openai version
        import openai
        print(f"📦 OpenAI version: {openai.__version__}")
        
        # Try different approaches
        print("\n🔧 Testing Approach 1: Direct import")
        try:
            from openai import AzureOpenAI
            client1 = AzureOpenAI(
                api_version="2023-12-01-preview",
                azure_endpoint=str(openai_endpoint),
                api_key=str(openai_api_key)
            )
            print("✅ Approach 1 successful")
        except Exception as e:
            print(f"❌ Approach 1 failed: {e}")
        
        print("\n🔧 Testing Approach 2: Module import")
        try:
            import openai
            client2 = openai.AzureOpenAI(
                api_version="2023-12-01-preview",
                azure_endpoint=str(openai_endpoint),
                api_key=str(openai_api_key)
            )
            print("✅ Approach 2 successful")
        except Exception as e:
            print(f"❌ Approach 2 failed: {e}")
        
        print("\n🔧 Testing Approach 3: Minimal parameters")
        try:
            from openai import AzureOpenAI
            client3 = AzureOpenAI(
                azure_endpoint=str(openai_endpoint),
                api_key=str(openai_api_key)
            )
            print("✅ Approach 3 successful")
        except Exception as e:
            print(f"❌ Approach 3 failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == '__main__':
    test_minimal_openai() 