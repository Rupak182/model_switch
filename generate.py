
import json
import os
import time
from datetime import datetime
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from transformers import AutoTokenizer
load_dotenv()  # Loads variables from .env



def count_output_tokens(prompt, model):
    try:
        tokenizer =AutoTokenizer.from_pretrained(model)
        tokens = tokenizer.encode(prompt)
        return len(tokens)
    except Exception as e:
        print(f"Error counting tokens for model {model}: {e}")
        return -1

def count_input_tokens(messages, model):
    try:
        tokenizer =AutoTokenizer.from_pretrained(model)

        total_tokens = 0
        for message in messages:
            role_tokens = tokenizer.encode(message['role'])
            total_tokens += len(role_tokens)

            content_tokens = tokenizer.encode(message['content'])
            total_tokens += len(content_tokens)
    
        return total_tokens
    except Exception as e:
        print(f"Error counting tokens for model {model}: {e}")
        return -1


def generate(prompt,model):
    client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

    start=time.time()
    messages=[
                {"role": "system", "content": "You are a helpful assistant.You answer everuything in a single line."},
                {"role": "user", "content": prompt},
            ]
    output = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        max_tokens=1024,
        )
    end =time.time()
    generation_time = end - start

    timing_data = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "prompt": prompt,
        "generation_time_seconds": generation_time,
        "prompt_tokens": count_input_tokens(messages, model),
        "response_tokens": count_output_tokens(output.choices[0].message.content, model),
    }

    json_file = "log.json"
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(timing_data)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

    

    print(f"Time taken to generate response: {end-start} seconds")
    return output.choices[0].message.content
