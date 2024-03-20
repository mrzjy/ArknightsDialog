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
