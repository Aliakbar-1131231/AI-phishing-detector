import sys

suspicious_keywords = [
    "login", "verify", "update", "banking", "secure", 
    "account", "confirm", "signin", "support", "ebayisapi",
    "free", "bonus", "gift", "auth", "portal"
]

def print_warning_banner():
    print(r"""
  ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
  ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
  ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
  ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
   ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """)

def print_safe_banner():
    print(r"""
   ███████╗ █████╗ ███████╗███████╗
   ██╔════╝██╔══██╗██╔════╝██╔════╝
   ███████╗███████║█████╗  █████╗  
   ╚════██║██╔══██║██╔══╝  ██╔══╝  
   ███████║██║  ██║██║     ███████╗
   ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝
    """)

def check_phishing(url):
    url_lower = url.lower()
    threat_score = 0
    
    for word in suspicious_keywords:
        if word in url_lower:
            threat_score += 1
            
    if "@" in url_lower:
        threat_score += 2  
        
    print(f"\n[*] Analyzing URL: {url}")
    print("-" * 60)
    
    if threat_score > 0:
        print_warning_banner()
        print(f"⚠️  WARNING: Detected {threat_score} high-risk indicator(s)!")
        print("⚠️  Status: This URL is highly suspicious and resembles a phishing attack.")
    else:
        print_safe_banner()
        print("✅ STATUS: SECURE / SAFE")
        print("No obvious phishing patterns or malicious keywords detected.")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_url = sys.argv[1]
    else:
        try:
            print("=== AI PHISHING DETECTOR v2.1 ===")
            user_url = input("Enter the URL to scan: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(1)
            
    if user_url.strip():
        check_phishing(user_url.strip())
    else:
        print("[-] Error: No URL provided.")
