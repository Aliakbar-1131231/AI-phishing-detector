import sys

suspicious_keywords = [
    "login", "verify", "update", "banking", "secure", 
    "account", "confirm", "signin", "support", "ebayisapi"
]

def check_phishing(url):
    url_lower = url.lower()
    threat_score = 0
    
    for word in suspicious_keywords:
        if word in url_lower:
            threat_score += 1
            
    print(f"\n--- Analysis Results for URL: {url} ---")
    if threat_score > 0:
        print(f"⚠️ Warning: Found {threat_score} suspicious pattern(s) related to phishing.")
        print("This URL might be unsafe. Proceed with caution.")
    else:
        print("✅ No obvious phishing patterns detected based on basic keywords.")
        print("However, always remain vigilant.")
    print("-" * 45 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_url = sys.argv[1]
    else:
        try:
            print("AI Phishing Detector Active")
            user_url = input("Enter the URL you want to check: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(1)
            
    if user_url.strip():
        check_phishing(user_url.strip())
    else:
        print("No URL entered. Exiting.")
