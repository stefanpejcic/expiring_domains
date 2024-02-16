import whois
import sys
import os

def check_whois(domain):
    try:
        # Fetch WHOIS information
        whois_info = whois.whois(domain)

        # Count characters before the dot and extract extension
        length = len(domain.split('.')[0])
        extension = domain.split('.')[-1]

        # Create the directory structure if it doesn't exist
        output_folder = os.path.join(extension, str(length))
        os.makedirs(output_folder, exist_ok=True)

        # Save WHOIS information to a file
        output_file = os.path.join(output_folder, f"{domain}.whois")
        with open(output_file, 'w') as file:
            file.write(str(whois_info))
        
        print(f"WHOIS information for {domain} saved to {output_file}")
    except Exception as e:
        print(f"Error fetching WHOIS information for {domain}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_whois.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    check_whois(domain)
