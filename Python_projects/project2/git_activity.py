import http.client
import json
import sys
from datetime import datetime

def fetch_github_activity(username):
    """Fetch recent activity for a GitHub user."""
    try:
        # Establish connection to GitHub API
        conn = http.client.HTTPSConnection("api.github.com")
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "github-activity-cli"
        }
        
        # Make request to the events endpoint
        conn.request("GET", f"/users/{username}/events", headers=headers)
        response = conn.getresponse()
        
        # Check response status
        if response.status != 200:
            if response.status == 404:
                print(f"Error: User '{username}' not found.")
                return None
            elif response.status == 403:
                print("Error: API rate limit exceeded.")
                return None
            else:
                print(f"Error: Received status code {response.status}")
                return None
        
        # Parse JSON response
        data = json.loads(response.read().decode())
        conn.close()
        return data
    
    except http.client.HTTPException as e:
        print(f"Error: Failed to connect to GitHub API - {str(e)}")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to parse API response.")
        return None

def format_timestamp(timestamp):
    """Format ISO timestamp to readable date."""
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return timestamp

def format_activity(event):
    """Format a single GitHub event into a readable string."""
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name", "unknown")
    created_at = format_timestamp(event.get("created_at", "unknown"))
    
    if event_type == "PushEvent":
        commit_count = len(event.get("payload", {}).get("commits", []))
        return f"- Pushed {commit_count} commit{'s' if commit_count != 1 else ''} to {repo_name} at {created_at}"
    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action", "unknown").capitalize()
        return f"- {action} an issue in {repo_name} at {created_at}"
    elif event_type == "WatchEvent":
        return f"- Starred {repo_name} at {created_at}"
    elif event_type == "PullRequestEvent":
        action = event.get("payload", {}).get("action", "unknown").capitalize()
        return f"- {action} a pull request in {repo_name} at {created_at}"
    elif event_type == "CreateEvent":
        ref_type = event.get("payload", {}).get("ref_type", "unknown")
        return f"- Created {ref_type} in {repo_name} at {created_at}"
    else:
        return f"- Performed {event_type} in {repo_name} at {created_at}"

def main():
    """Main function to handle CLI execution."""
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    events = fetch_github_activity(username)
    
    if events is None:
        sys.exit(1)
    
    if not events:
        print(f"No recent activity found for user '{username}'.")
        return
    
    print(f"\nRecent activity for {username}:\n")
    for event in events[:10]:  # Limit to 10 most recent events
        print(format_activity(event))

if __name__ == "__main__":
    main()
