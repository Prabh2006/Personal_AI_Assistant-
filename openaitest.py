import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt= "Write an email to my boss for resignation",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

"""{
  "choices": [
    {
      "text": "\n\nSubject: Resignation\n\nDear [Your Boss' Name],\n\nThis message is to inform you that I have made the difficult decision to resign from my position as [Your Position] at [Your Company].\n\nMy last day of work will be [Date]. I truly appreciate the opportunity I have had to work here and the knowledge that I have gained during my time with the company.\n\nI want to thank you for the opportunity to work at [Your Company] and I wish you and the company ongoing success. If there is anything I can do to help with the transition, please let me know.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 139,
    "total_tokens": 147
  }
}"""

print(response)
