import feedparser

blog_url = "https://kdn0325.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

print(latest_posts)

preREADME = """


## Profile
- 🙂Portfolio : [Abel-Frontelio](https://portfolio-abel.netlify.app/)
- 📧E-Mail : dn10003@gmail.com
- 🌟Blog : [Abel-Frontelio](https://kdn0325.github.io/)


## Tech Stack


 #### Web Applications
 <p align="left">
<img src="https://img.shields.io/badge/html5-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/javascript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=white" />
<img src="https://img.shields.io/badge/typescript-3178C6.svg?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/react-61DAFB.svg?style=for-the-badge&logo=react&logoColor=white" />
<img src="https://img.shields.io/badge/nextjs-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white" />
</p>
 
 #### Mobile Applications
 <p align="left">
<img src="https://img.shields.io/badge/reactnative-282c35.svg?style=for-the-badge&logo=react&logoColor=white" />
  
 #### State management
 <p align="left">
<img src="https://img.shields.io/badge/redux-764ABC.svg?style=for-the-badge&logo=redux&logoColor=white" />
<img src="https://img.shields.io/badge/recoil-3578E5.svg?style=for-the-badge&logo=recoil&logoColor=white" />
<img src="https://img.shields.io/badge/reactquery-FF4154.svg?style=for-the-badge&logo=reactquery&logoColor=white" />
<img src="https://img.shields.io/badge/redux-764ABC.svg?style=for-the-badge&logo=redux&logoColor=white" />
  
 #### CSS
 <p align="left">
<img src="https://img.shields.io/badge/styledcomponents-DB7093.svg?style=for-the-badge&logo=styledcomponents&logoColor=white" />
<img src="https://img.shields.io/badge/sass-CC6699.svg?style=for-the-badge&logo=sass&logoColor=white" />
<img src="https://img.shields.io/badge/tailwindcss-06B6D4.svg?style=for-the-badge&logo=tailwindcss&logoColor=white" />
 
 
 #### Backend
 <p align="left">
<img src="https://img.shields.io/badge/nodejs-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/django-092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
 
 
 #### DevOps
 <p align="left">
<img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/mongodb-47A248.svg?style=for-the-badge&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-232F3E.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"  />
 
 
 #### Build Tools
<p align="left">
<img src="https://img.shields.io/badge/eslint-4B32C3.svg?style=for-the-badge&logo=eslint&logoColor=white" />
<img src="https://img.shields.io/badge/prettier-F7B93E.svg?style=for-the-badge&logo=prettier&logoColor=white" />
<img src="https://img.shields.io/badge/webpack-8DD6F9.svg?style=for-the-badge&logo=webpack&logoColor=white" />
</p>

## Git Stats
![kdn0325](https://github-readme-stats.vercel.app/api?username=kdn0325&show_icons=true)

## Latest Blog Post
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)