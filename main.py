# AI Phishing Detector - Basic URL Checker
# This script performs a simple keyword check on a provided URL to identify potentially suspicious patterns.

def check_phishing(url):
    # Define a list of keywords commonly found in phishing URLs.
    suspicious_keywords = [
        "login", "verify", "update", "free", "account", "security",
        "signin", "password", "confirm", "reward", "banking"
    ]
    
    # Initialize a threat score.
    threat_score = 0
    
    # Convert the URL to lowercase for case-insensitive comparison.
    url_lower = url.lower()
    
    # Iterate through the keyword list and count matches in the URL.
    for word in suspicious_keywords:
        if word in url_lower:
            threat_score += 1
            
    # Output the initial analysis results.
    print(f"\n--- Analysis Results for URL: {url} ---")
    if threat_score > 0:
       print(f"⚠️ Warning: Found {threat_score} suspicious pattern(s) related to phishing.")
       print("This URL might be unsafe. Proceed with caution.")
    else:
        print("✅ No obvious phishing patterns detected based on basic keywords.")
        print("However, always remain vigilant.")
    print("-------------------------------------------\n")

# --- Main execution part ---
if __name__ == "__main__":
    try:
        user_url = input("Enter the URL you want to check: ")
        if user_url.strip():
            check_phishing(user_url)
        else:
            print("No URL entered. Exiting.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
