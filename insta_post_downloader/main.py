import instaloader
import re

download=instaloader.Instaloader()
url=input("Enter Url:")

shortcode = re.search("/p/(.*?)/", url).group(1)

post=instaloader.Post.from_shortcode(download.context,shortcode)
download.download_post(post, target=post.owner_username)


print(shortcode)