import pandas as pd
import random

def generate_dataset(num_samples=500):
    data = []
    
    for _ in range(num_samples):
        followers = random.randint(0, 1000000)
        following = random.randint(0, 5000)
        posts = random.randint(0, 500)
        has_profile_pic = random.choice([True, False])
        
        # Label the account as Fake (0) or Real (1)
        if (followers < 100 and following > 500) or not has_profile_pic or posts < 5:
            label = 0  # Fake account
        else:
            label = 1  # Real account
        
        data.append([followers, following, posts, has_profile_pic, label])
    
    df = pd.DataFrame(data, columns=["Followers", "Following", "Posts", "Has_Profile_Pic", "Label"])
    df.to_csv("instagram_fake_accounts.csv", index=False)
    print("Dataset saved as instagram_fake_accounts.csv")

# Generate and save the dataset
generate_dataset()