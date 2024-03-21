# ArknightsDialog
Extracting character conversations in Arknights

## Usage

First, git clone [ArknightsData](https://github.com/Dimbreath/ArknightsData)

(Thanks to Dimbreath's project!)

Simply run parse.py after specifying ArknightsData directory path and lang:

~~~
line 8: repo = "D:/code/github/ArknightsData"
line 9: lang = "en-US"
~~~

This results in story.jsonl in data folder.
Each line is a JSON dict, containing the following fields:

~~~
context: description of story context
conversation: ChatGPT-message-like list of dict, with role, content fields 
meta: meta info
~~~

### Example

~~~
{
  "context": "混入龙门的整合运动数量远超想象，并且他们的行动越来越不掩饰。\n在碎骨的带领下，他们竟然主动向罗德岛发起进攻。",
  "conversation": [
    {
      "role": "雷蛇",
      "content": "——"
    },
    {
      "role": "雷蛇",
      "content": "怎么有这么多整合运动！"
    },
    {
      "role": "整合运动成员",
      "content": "诶呀！"
    },
    {
      "role": "芙兰卡",
      "content": "......"
    },
    ...
    {
      "role": "阿米娅",
      "content": "（趁他们不敢继续进攻的时候，向低层转移！）"
    },
    {
      "role": "阿米娅",
      "content": "（现在必须要扩大战场！）"
    },
    {
      "role": "芙兰卡",
      "content": "（知道了，那就边跑边打吧！）"
    },
    {
      "role": "阿米娅",
      "content": "与你有什么关系？"
    },
    {
      "role": "碎骨",
      "content": "......你！"
    },
    {
      "role": "碎骨",
      "content": "......"
    },
    {
      "role": "碎骨",
      "content": "我的同胞，动手吧！"
    }
  ],
  "meta": {
    "source": "obt/main\\level_main_02-09_beg.txt",
    "characters": [
      "碎骨",
      "雷蛇",
      "芙兰卡",
      "整合运动成员",
      "阿米娅"
    ]
  }
}
~~~
