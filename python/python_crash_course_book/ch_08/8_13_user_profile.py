def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Alex', 'Martinez', location='Heaven', field='Mafia', net_worth="1,000,000,000")
print(user_profile)
