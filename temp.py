import os

def main():
    os.environ["bearer_token"] = "AAAAAAAAAAAAAAAAAAAAAOeQlwEAAAAA776bbjDGhEVJ%2FpXQOw1%2Bn2Qp1dQ%3D9Fok70fT0N4KbD8RE2mL44xMzzx1mTiqF8jFYrAWv56RgfWeuC"
    os.environ["aws_access_key_id"] = "TTtPs5tQ12kQNXMgtWq5OZlXo"
    os.environ["aws_secret_access_key"] = "6yEx73EvjnE78pBWku4wQP4mfwlyHMxGwtHWwLeubN7lr2SCJ1"
    os.environ["aws_region"] = "eu-west-2"

def get_env(token_name):
    _field = os.environ.get(token_name)
    return _field

def main1():
    bearer_token = get_env("bearer_token")
    aws_access_key = get_env("aws_access_key")
    aws_secret_access_key = get_env("aws_secret_access_key")
    aws_region = get_env("aws_region")
    i = 0

if __name__ == "__main__":
    main1()