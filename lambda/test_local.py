import os
from dotenv import load_dotenv
from main import lambda_handler

# Load environment variables
load_dotenv()

# Verify environment variables
required_vars = ["HF_TOKEN", "FACEBOOK_PAGE_ID", "FACEBOOK_TOKEN"]
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}")
    exit(1)

print("✅ All environment variables loaded")
print("\n" + "="*50)
print("TESTING CONTENT GENERATION")
print("="*50 + "\n")

# Run the handler
result = lambda_handler({}, {})

print("\n" + "="*50)
print("TEST COMPLETE")
print("="*50)