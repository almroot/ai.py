# ai.py
Command line utility tweaked to deliver bash-one liners to your question, based on the GPT-3 artificial intelligence.

## Usage

Basic character substitution in your shell:
```
almroot@x:~(main)$ ai replace comma with linebreak
tr ',' '\n'
```

SysOps help for your ansible needs:
```
almroot@x:~(main)$ ai deploy with ansible to all hosts except A
ansible-playbook site.yml --limit '!A'
```

Internet-wide recon:
```
almroot@x:~(main)$ ai find exposed ssh on the internet using masscan
sudo masscan 0.0.0.0/0 -p22 --rate=1000
```

Bug bounty hunting and pentesting:
```
almroot@x:~(main)$ ai download common wordlists used for pentesting and bug bounty hunting
git clone https://github.com/danielmiessler/SecLists
```

## Installation

1. Clone the repository like so `git clone git@github.com:almroot/ai.py.git`
2. You must have an [OpenAI account](https://openai.com/blog/openai-api/) to get access to [GPT-3](https://www.youtube.com/watch?v=Te5rOTcE4J4)
3. Sign in and grab your [API key](https://beta.openai.com/account/api-keys)
4. In order to use the script, set the environment variable `OPENAI_API_KEY` to the key

## Recommended Python Version

The script currently supports Python 3.

## Dependencies

The script depends on the `openai` and `numpy` python modules.

These dependencies can be installed using the requirements file:

```
almroot@x:~(main)$ ai install python dependencies
pip install -r requirements.txt
```

