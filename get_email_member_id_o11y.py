import requests

# Configuration
API_TOKEN = "<Session User API Access Token>"
BASE_URL = "https://api.jp0.signalfx.com"
HEADERS = {
    "X-SF-TOKEN": API_TOKEN,
    "Content-Type": "application/json"
}

def get_all_members():
    members = []
    offset = None

    while True:
        params = {"limit": 100}
        if offset:
            params["offset"] = offset

        response = requests.get(
            f"{BASE_URL}/v2/organization/member",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            print(f"❌ Error fetching members: {response.status_code} - {response.text}")
            break

        data = response.json()
        members.extend(data.get("results", []))

        offset = data.get("offset")
        if not offset:
            break

    return members

def main():
    members = get_all_members()
    print(f"✅ Total members found: {len(members)}\n")

    for member in members:
        email = member.get("email", "N/A")
        member_id = member.get("id", "N/A")
        print(f"📧 Email: {email}   🆔 ID: {member_id}")

if __name__ == "__main__":
    main()