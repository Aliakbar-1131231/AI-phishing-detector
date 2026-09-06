import sys
import re

def display_banner(status):
    if status == "WARNING":
        print(r"""
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██╔══██║██║╚██╗██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        """)
        print("\033[91m[!] WARNING: Detected high-risk indicators!\033[0m")
        print("\033[91m[*] Status: This URL is highly suspicious and resembles a phishing attack.\033[0m")
    else:
        print(r"""
 ██████╗  █████╗ ███████╗███████╗
██╔════╝ ██╔══██╗██╔════╝██╔════╝
╚█████╗  ███████║█████╗  █████╗  
 ╚═══██╗ ██╔══██║██╔══╝  ██╔══╝  
██████╔╝ ██║  ██║██║     ███████╗
╚═════╝  ╚═╝  ╚═╝╚═╝     ╚══════╝
        """)
        print("\033[92m[✓] STATUS: SECURE / SAFE\033[0m")
        print("\033[92mNo obvious phishing patterns or malicious keywords detected.\033[0m")

def analyze_url(url):
    tunnel_domains = ["trycloudflare.com", "ngrok-free.app", "loca.lt", "serveo.net"]
    keywords = ["login", "verify", "account", "signin", "update", "banking", "security", "confirm"]
    
    url_lower = url.lower()
    
    for domain in tunnel_domains:
        if domain in url_lower:
            return "WARNING"
            
    if url_lower.count('-') > 3:
        return "WARNING"

    for word in keywords:
        if word in url_lower:
            return "WARNING"
            
    return "SAFE"

def main():
    print("=== AI PHISHING DETECTOR v2.1 ===")
    url = input("Enter the URL to scan: ").strip()
    
    if not url:
        print("[-] Error: URL cannot be empty.")
        return
        
    print(f"\n[+] Analyzing URL: {url}")
    
    result = analyze_url(url)
    display_banner(result)

if __name__ == "__main__":
    main()
