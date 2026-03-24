users = {
    "alice": "admin",
    "bob": "user"
}

def admin_panel():
    print("\n[Admin Panel] You can view logs, manage users, and change system settings.")

def user_dashboard():
    print("\n[User Dashboard] You can view your profile and update your preferences.")

def authentication():
    username = input("Username: ")
    if username in users:
        return username
    else:
        print("Authentication failed: unknown user.")
        return None

def authorize_and_act(username):
    role = users[username]
    print(f"\nWelcome {username}! Your role: {role}")

    if role == "admin":
        print("\n--- Admin Access Granted ---")
        admin_panel()
        user_dashboard
    elif role == "user":
        print("\n--- User Access Granted ---")
        user_dashboard()
        print("\n[Access Denied] Only administrators can access the admin panel.")
    else:
        print("Unknown role. Access denied.")

def main():
    print("=== RBAC Demonstration ===\n")
    user = authentication()
    if user:
        authorize_and_act(user)

if __name__ == "__main__":
    main()