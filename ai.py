#!/usr/bin/python3.8

import os
import sys
import openai
import numpy as np

# Prepare the prompt to be sent to GPT-3
arr = np.array(sys.argv)
prompt = ' '.join(arr[1:])
context = "Convert this text to a programmatic shell command:\n\nExample: Ask Constance if we need some bread\nOutput: send-msg `find constance` Do we need some bread?\n\nExample: Read, sort and filter the file input.txt\nOutput: cat input.txt | sort | uniq\n\nExample: Show the PID for all open ports\nOutput: sudo lsof -i -P\n\nExample: {}\nOutput:".format(prompt)

# Prepare the API with our key
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=context,
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)

# Process and present the output
if len(response.choices) > 0:
  print(response.choices[0].text.strip())
  exit(0)

# Abort on failure
exit(1)
