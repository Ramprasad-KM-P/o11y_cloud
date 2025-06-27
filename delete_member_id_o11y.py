import requests
import time

# --- CONFIGURATION ---
API_TOKEN = "<Session User API Access Token>"
BASE_URL = "https://api.jp0.signalfx.com"
HEADERS = {
    "X-SF-TOKEN": API_TOKEN,
    "Content-Type": "application/json"
}

# Path to the file containing member IDs (one per line)
MEMBER_ID_FILE = "member_ids.txt"

def read_member_ids(file_path):
    """Read member IDs from a text file, one per line."""
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def delete_member(member_id):
    """Delete a single organization member by ID."""
    url = f"{BASE_URL}/v2/organization/member/{member_id}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"✅ Deleted member: {member_id}")
    else:
        print(f"❌ Failed to delete {member_id} | {response.status_code} - {response.text}")

def main():
    member_ids = read_member_ids(MEMBER_ID_FILE)
    print(f"📋 Found {len(member_ids)} member IDs to delete.\n")

    for member_id in member_ids:
        delete_member(member_id)
        time.sleep(0.2)  # Prevent hitting rate limits

if __name__ == "__main__":
    main()