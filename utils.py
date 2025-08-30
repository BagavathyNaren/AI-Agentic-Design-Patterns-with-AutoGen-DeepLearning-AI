# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_anthropic_api_key():
    load_env()
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    return anthropic_api_key

def get_claude_sonnet_four_model():
    load_env()
    claude_sonnet_four_model = os.getenv("CLAUDE_SONNET_FOUR_MODEL")
    return claude_sonnet_four_model

def get_claude_sonnet_three_seven_model():
    load_env()
    claude_sonnet_three_seven_model = os.getenv("CLAUDE_SONNET_THREE_SEVEN_MODEL")
    return claude_sonnet_three_seven_model

def get_claude_haiku_model():
    load_env()
    claude_haiku_model = os.getenv("CLAUDE_HAIKU_MODEL")
    return claude_haiku_model
