import feedparser
from datetime import datetime
from time import mktime

blog_url = "https://kdn0325.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

for idx, entry in enumerate(rss_feed['entries']):
    if idx >= MAX_NUM:
        break

    feed_date = entry['published_parsed']
    formatted_date = datetime.fromtimestamp(
        mktime(feed_date)
    ).strftime('%Y년 %m월 %d일')

    latest_posts += f" - [📆{formatted_date} / {entry['title']}]({entry['link']})\n"

print(latest_posts)

preREADME = """

<div align="center">
  
[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=kdn0325)](https://solved.ac/kdn0325)
<img src="http://mazandi.herokuapp.com/api?handle=kdn0325&theme=warm"/>

</div>
<img src="https://raw.githubusercontent.com/kdn0325/terminal-for-github-profile-readme/1adccd811a108350e5dbe91c5e4911c04bd6f289/github_stats.svg" />




## 최근 포스트
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
