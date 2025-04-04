import feedparser

blog_url = "https://kdn0325.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 6

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

print(latest_posts)

preREADME = """


## Profile
- 🙂Portfolio : [dongnyeong.dev](https://www.dongnyeong.com)
- 📧E-Mail : dn10003@gmail.com
- 🌟Blog : [DONGNYEONG-FRONTELIO](https://kdn0325.github.io/)

## 최근 포스트
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
