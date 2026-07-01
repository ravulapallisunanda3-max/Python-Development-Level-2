# ============================================================
# Project      : API Integration – Command-Line Application
# API Used     : JSONPlaceholder (https://jsonplaceholder.typicode.com)
# Description  : Fetches live Posts, Users & Comments data
#                from a public REST API and presents it in
#                a clean, menu-driven terminal interface.
# Python       : 3.x  |  Library: requests
# ============================================================

import requests          # For making HTTP requests to the REST API
import sys               # For clean program exit
import time              # For simulating loading delays

# ─────────────────────────────────────────────
#  CONSTANTS  – single place to update URLs
# ─────────────────────────────────────────────
BASE_URL     = "https://jsonplaceholder.typicode.com"
POSTS_URL    = f"{BASE_URL}/posts"
USERS_URL    = f"{BASE_URL}/users"
COMMENTS_URL = f"{BASE_URL}/comments"

REQUEST_TIMEOUT = 10   # seconds before giving up on a slow network


# ══════════════════════════════════════════════
#  SECTION 1 – DISPLAY / UI HELPERS
# ══════════════════════════════════════════════

def print_banner():
    """Print a decorative welcome banner when the program starts."""
    print("\n" + "═" * 58)
    print("   ██████╗ ██╗      █████╗ ███████╗███████╗██╗ ██████╗")
    print("  ██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██║██╔════╝")
    print("  ██║     ██║     ███████║███████╗███████╗██║██║     ")
    print("  ██║     ██║     ██╔══██║╚════██║╚════██║██║██║     ")
    print("  ╚██████╗███████╗██║  ██║███████║███████║██║╚██████╗")
    print("   ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝")
    print("═" * 58)
    print("       🌐  API INTEGRATION – Data Explorer v1.0")
    print("       📡  Source : JSONPlaceholder REST API")
    print("═" * 58)


def print_menu():
    """Display the main navigation menu."""
    print("\n" + "─" * 40)
    print("          📋  MAIN MENU")
    print("─" * 40)
    print("  1. 📰  View Posts")
    print("  2. 👤  View Users")
    print("  3. 💬  View Comments")
    print("  4. 🔍  Search Post by ID")
    print("  5. 🔍  Search User by ID")
    print("  6. 🔄  Refresh / Test Connection")
    print("  7. ❌  Exit")
    print("─" * 40)


def loading(message="  ⏳ Fetching data, please wait"):
    """Print an animated loading message."""
    print(f"\n{message}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()   # newline after dots


def print_divider(char="─", width=58):
    """Print a horizontal divider line."""
    print(char * width)


def success(message):
    """Print a green-style success message."""
    print(f"\n  ✅  {message}")


def error(message):
    """Print an error message with a warning icon."""
    print(f"\n  ❌  ERROR: {message}")


def warn(message):
    """Print a warning/info message."""
    print(f"\n  ⚠️   {message}")


# ══════════════════════════════════════════════
#  SECTION 2 – NETWORK / API LAYER
# ══════════════════════════════════════════════

def fetch_data(url):
    """
    Make a GET request to the given URL and return parsed JSON data.

    Handles all common network and HTTP errors gracefully so the
    rest of the program never needs to deal with raw exceptions.

    Parameters:
        url (str): The full API endpoint URL to call.

    Returns:
        dict | list | None: Parsed JSON on success, None on any failure.
    """
    try:
        # Send the GET request with a timeout to avoid hanging forever
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        # Raise an HTTPError for 4xx and 5xx status codes
        response.raise_for_status()

        # Parse and return the JSON body
        return response.json()

    except requests.exceptions.ConnectionError:
        # No internet or DNS resolution failed
        error("No internet connection. Please check your network.")

    except requests.exceptions.Timeout:
        # Server did not respond within REQUEST_TIMEOUT seconds
        error(f"Request timed out after {REQUEST_TIMEOUT} seconds.")

    except requests.exceptions.HTTPError as http_err:
        # Server returned 4xx / 5xx status
        status = http_err.response.status_code
        if status == 404:
            error(f"Resource not found (HTTP 404). Check the ID and try again.")
        elif status == 500:
            error("Server error (HTTP 500). The API may be down.")
        else:
            error(f"HTTP error received: {http_err}")

    except requests.exceptions.JSONDecodeError:
        # Response body is not valid JSON
        error("Invalid response received from the API (not valid JSON).")

    except requests.exceptions.RequestException as req_err:
        # Catch-all for any other requests-related issues
        error(f"Unexpected network error: {req_err}")

    # Return None signals to the caller that something went wrong
    return None


# ══════════════════════════════════════════════
#  SECTION 3 – DATA DISPLAY FUNCTIONS
# ══════════════════════════════════════════════

def display_posts(posts):
    """
    Neatly format and print a list of post objects.

    Parameters:
        posts (list): List of post dicts from the API.
    """
    if not posts:
        warn("No posts to display.")
        return

    print(f"\n{'═' * 58}")
    print(f"  📰  POSTS  ({len(posts)} records)")
    print(f"{'═' * 58}")

    for post in posts:
        print(f"\n  ID     : {post.get('id')}")
        print(f"  User   : #{post.get('userId')}")
        # Capitalise the first letter of the title for clean display
        title = post.get('title', 'N/A').capitalize()
        print(f"  Title  : {title}")
        # Truncate long bodies to keep output readable
        body = post.get('body', '').replace('\n', ' ')
        if len(body) > 80:
            body = body[:80] + "..."
        print(f"  Body   : {body}")
        print_divider("·", 58)


def display_users(users):
    """
    Neatly format and print a list of user objects.

    Parameters:
        users (list): List of user dicts from the API.
    """
    if not users:
        warn("No users to display.")
        return

    print(f"\n{'═' * 58}")
    print(f"  👤  USERS  ({len(users)} records)")
    print(f"{'═' * 58}")

    for user in users:
        # Safely drill into nested dicts using .get() with defaults
        address  = user.get('address', {})
        company  = user.get('company', {})
        geo      = address.get('geo', {})

        print(f"\n  ID       : {user.get('id')}")
        print(f"  Name     : {user.get('name', 'N/A')}")
        print(f"  Username : @{user.get('username', 'N/A')}")
        print(f"  Email    : {user.get('email', 'N/A')}")
        print(f"  Phone    : {user.get('phone', 'N/A')}")
        print(f"  Website  : {user.get('website', 'N/A')}")
        print(f"  City     : {address.get('city', 'N/A')}")
        print(f"  Company  : {company.get('name', 'N/A')}")
        print(f"  Lat/Lng  : {geo.get('lat', 'N/A')}, {geo.get('lng', 'N/A')}")
        print_divider("·", 58)


def display_comments(comments):
    """
    Neatly format and print a list of comment objects.

    Parameters:
        comments (list): List of comment dicts from the API.
    """
    if not comments:
        warn("No comments to display.")
        return

    # Show only the first 10 comments to avoid flooding the terminal
    displayed = comments[:10]

    print(f"\n{'═' * 58}")
    print(f"  💬  COMMENTS  (showing {len(displayed)} of {len(comments)})")
    print(f"{'═' * 58}")

    for comment in displayed:
        print(f"\n  ID      : {comment.get('id')}")
        print(f"  Post    : #{comment.get('postId')}")
        print(f"  Name    : {comment.get('name', 'N/A').capitalize()}")
        print(f"  Email   : {comment.get('email', 'N/A')}")
        body = comment.get('body', '').replace('\n', ' ')
        if len(body) > 80:
            body = body[:80] + "..."
        print(f"  Comment : {body}")
        print_divider("·", 58)


def display_single_post(post):
    """
    Display one post in a detailed card format.

    Parameters:
        post (dict): A single post object from the API.
    """
    print(f"\n{'═' * 58}")
    print(f"  📰  POST DETAIL")
    print(f"{'═' * 58}")
    print(f"  ID      : {post.get('id')}")
    print(f"  User ID : {post.get('userId')}")
    title = post.get('title', 'N/A').capitalize()
    print(f"  Title   : {title}")
    print(f"\n  Body:")
    # Print the full body indented for readability
    for line in post.get('body', '').split('\n'):
        print(f"    {line}")
    print_divider("═", 58)


def display_single_user(user):
    """
    Display one user's full profile card.

    Parameters:
        user (dict): A single user object from the API.
    """
    address = user.get('address', {})
    company = user.get('company', {})
    geo     = address.get('geo', {})

    print(f"\n{'═' * 58}")
    print(f"  👤  USER PROFILE")
    print(f"{'═' * 58}")
    print(f"  ID        : {user.get('id')}")
    print(f"  Name      : {user.get('name', 'N/A')}")
    print(f"  Username  : @{user.get('username', 'N/A')}")
    print(f"  Email     : {user.get('email', 'N/A')}")
    print(f"  Phone     : {user.get('phone', 'N/A')}")
    print(f"  Website   : {user.get('website', 'N/A')}")
    print(f"\n  📍 Address:")
    print(f"     Street  : {address.get('street', 'N/A')}")
    print(f"     Suite   : {address.get('suite', 'N/A')}")
    print(f"     City    : {address.get('city', 'N/A')}")
    print(f"     Zipcode : {address.get('zipcode', 'N/A')}")
    print(f"     Lat/Lng : {geo.get('lat', 'N/A')}, {geo.get('lng', 'N/A')}")
    print(f"\n  🏢 Company:")
    print(f"     Name    : {company.get('name', 'N/A')}")
    print(f"     Catch   : {company.get('catchPhrase', 'N/A')}")
    print(f"     BS      : {company.get('bs', 'N/A')}")
    print_divider("═", 58)


# ══════════════════════════════════════════════
#  SECTION 4 – MENU ACTION HANDLERS
# ══════════════════════════════════════════════

def handle_view_posts():
    """Fetch all posts from the API and display them."""
    loading("  ⏳ Loading posts")
    posts = fetch_data(POSTS_URL)
    if posts is not None:
        success(f"Loaded {len(posts)} posts successfully!")
        display_posts(posts)


def handle_view_users():
    """Fetch all users from the API and display them."""
    loading("  ⏳ Loading users")
    users = fetch_data(USERS_URL)
    if users is not None:
        success(f"Loaded {len(users)} users successfully!")
        display_users(users)


def handle_view_comments():
    """Fetch all comments from the API and display the first 10."""
    loading("  ⏳ Loading comments")
    comments = fetch_data(COMMENTS_URL)
    if comments is not None:
        success(f"Loaded {len(comments)} comments. Displaying first 10.")
        display_comments(comments)


def handle_search_post():
    """
    Ask the user for a Post ID, validate it, then fetch and show that post.
    IDs on JSONPlaceholder range from 1 to 100.
    """
    print("\n  Enter Post ID to search (1 – 100):")
    raw = input("  → ").strip()

    # ── Input validation ──────────────────────
    if not raw.isdigit():
        warn("Invalid input. Please enter a numeric ID.")
        return

    post_id = int(raw)
    if post_id < 1 or post_id > 100:
        warn("Post ID must be between 1 and 100.")
        return
    # ─────────────────────────────────────────

    loading(f"  ⏳ Searching for Post #{post_id}")
    url  = f"{POSTS_URL}/{post_id}"
    post = fetch_data(url)
    if post is not None:
        success(f"Post #{post_id} found!")
        display_single_post(post)


def handle_search_user():
    """
    Ask the user for a User ID, validate it, then fetch and show that user.
    IDs on JSONPlaceholder range from 1 to 10.
    """
    print("\n  Enter User ID to search (1 – 10):")
    raw = input("  → ").strip()

    # ── Input validation ──────────────────────
    if not raw.isdigit():
        warn("Invalid input. Please enter a numeric ID.")
        return

    user_id = int(raw)
    if user_id < 1 or user_id > 10:
        warn("User ID must be between 1 and 10.")
        return
    # ─────────────────────────────────────────

    loading(f"  ⏳ Searching for User #{user_id}")
    url  = f"{USERS_URL}/{user_id}"
    user = fetch_data(url)
    if user is not None:
        success(f"User #{user_id} found!")
        display_single_user(user)


def handle_refresh():
    """Ping the API base URL to verify connectivity and response time."""
    loading("  ⏳ Testing API connection")
    start = time.time()
    data  = fetch_data(f"{BASE_URL}/posts/1")    # lightweight single-item call
    elapsed = round((time.time() - start) * 1000)   # convert to ms

    if data is not None:
        success(f"API is reachable! Response time: {elapsed} ms")
        print(f"  🌐  Endpoint : {BASE_URL}")
    else:
        warn("Could not reach the API. Check your connection and try again.")


# ══════════════════════════════════════════════
#  SECTION 5 – MAIN PROGRAM LOOP
# ══════════════════════════════════════════════

def main():
    """
    Entry point – display banner, then loop the menu until user exits.
    All routing from user input to handler functions happens here.
    """
    print_banner()
    print("\n  Welcome! This app fetches live data from JSONPlaceholder.")
    print("  Make sure you are connected to the internet.")

    # Map each valid menu choice to its handler function
    menu_actions = {
        "1": handle_view_posts,
        "2": handle_view_users,
        "3": handle_view_comments,
        "4": handle_search_post,
        "5": handle_search_user,
        "6": handle_refresh,
    }

    while True:
        print_menu()
        choice = input("  Enter your choice (1–7): ").strip()

        if choice == "7":
            # User chose to exit – print goodbye and break the loop
            print("\n" + "═" * 58)
            print("  👋  Thank you for using the API Integration App!")
            print("  🌐  Stay Connected. Goodbye!")
            print("═" * 58 + "\n")
            sys.exit(0)

        elif choice in menu_actions:
            # Call the function mapped to this choice
            menu_actions[choice]()

        else:
            # Any other input is invalid
            warn("Invalid choice. Please enter a number between 1 and 7.")


# ── Run only when executed directly (not imported) ──
if __name__ == "__main__":
    main()
