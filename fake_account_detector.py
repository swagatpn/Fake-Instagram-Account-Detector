import instaloader

def fetch_instagram_data(username):
    loader = instaloader.Instaloader()
    try:
        # Load the profile
        profile = instaloader.Profile.from_username(loader.context, username)
        
        # Extract profile data
        data = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Post Count": profile.mediacount,
            "Has Profile Picture": profile.profile_pic_url is not None
        }
        return data
    except Exception as e:
        return {"error": f"Unable to fetch data: {str(e)}"}

def is_fake_account(data):
    if "error" in data:
        return data["error"]

    # Simple rules to detect fake accounts
    if data["Followers"] < 100:
        return "Suspicious: Very few followers."
    if data["Following"] > data["Followers"] * 10:
        return "Suspicious: Following far more than followers."
    if not data["Has Profile Picture"]:
        return "Suspicious: No profile picture."
    if data["Post Count"] < 5:
        return "Suspicious: Very few posts."
    
    return "Looks genuine!"
