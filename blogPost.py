import feedparser

blog_url = "https://kdn0325.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

# 'updated_parsed' 필드를 사용하여 업데이트 날짜를 기준으로 정렬
entries_sorted_by_update = sorted(rss_feed['entries'], key=lambda x: x['updated_parsed'], reverse=True)

for idx, entry in enumerate(entries_sorted_by_update):
    if idx >= MAX_NUM:
        break
    updated_date = entry['updated_parsed']
    latest_posts += f" - [{updated_date.tm_mon}/{updated_date.tm_mday} - {entry['title']}]({entry['link']})\n"

print(latest_posts)


preREADME = """


## Profile
- 🙂Portfolio : [PORTFOLIO](https://nextjs-abel-frontelio.vercel.app/)
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
  
 #### CSS
 <p align="left">
<img src="https://img.shields.io/badge/styledcomponents-DB7093.svg?style=for-the-badge&logo=styledcomponents&logoColor=white" />
<img src="https://img.shields.io/badge/sass-CC6699.svg?style=for-the-badge&logo=sass&logoColor=white" />
<img src="https://img.shields.io/badge/tailwindcss-06B6D4.svg?style=for-the-badge&logo=tailwindcss&logoColor=white" />
 
 
 #### Backend
 <p align="left">
<img src="https://img.shields.io/badge/nodejs-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/django-092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/firebase-FFCA28.svg?style=for-the-badge&logo=firebase&logoColor=white" />
 
 
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

## Git Hits
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fkdn0325%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Git Stats
[![kdn0325's Github stats](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=kdn0325&theme=vue)]((https://github.com/codeisneverodd?tab=repositories))

## Latest Blog Post
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
