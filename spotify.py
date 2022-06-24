
import spotipy.util as util
"""
get the value for these parameters from the spotify developers dashboard

"""
username = 'user_name'
client_id ='client_id'
client_secret = 'client_secret'
redirect_uri = 'http://localhost:7777/callback/'
scope = 'user-read-recently-played'
"""
to load the token every time you run your script.
"""
token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)
"""
use this link to know more about tokens and refresh tokens
https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/
"""                                   
print(token)
"""
this token will be valid only for an hour after which you have to use a new one. Spotify provides refresh tokens.
given below is the token generated at the time of running the code
"""
#BQCwIttXZtSJNX4dxlRARbWs4ECE2egRmpdoub63Tenk5g-jowDisKTk-VbMqeOhKT-jgYnarHXMxQwYfnAmAb3iU9s9LaLWYgX2GRpmndP0Fposcnuv5IjT-EhA3lKCo1_I3J_P2sfCQ1UCvVKMGF9yxZ28C-AZ0ePpApJYyEF-zttZP-HaCAofo6lJ5OEERGPesZc