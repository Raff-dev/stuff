import os
import re


def load_prompts_from_directory(directory):
    prompts = {}

    # Listowanie wszystkich plików w katalogu
    for filename in os.listdir(directory):
        # Sprawdzenie, czy plik ma rozszerzenie .md
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)

            with open(filepath, "r") as f:
                lines = f.readlines()

            in_code_block = False
            current_prompt_name = None
            current_prompt_content = []

            # Czytanie linii z pliku
            for line in lines:
                if line.startswith("```"):
                    if in_code_block:
                        in_code_block = False
                        if current_prompt_name:
                            prompts[current_prompt_name] = "".join(current_prompt_content).strip()
                        current_prompt_name = None
                        current_prompt_content = []
                    else:
                        in_code_block = True
                        match = re.search(r"ease_prompt=([a-zA-Z0-9_]+)", line)
                        if match:
                            current_prompt_name = match.group(1)
                elif in_code_block:
                    current_prompt_content.append(line)

    return prompts


if __name__ == "__main__":
    prompts = load_prompts_from_directory("prompts")
    for name, content in prompts.items():
        print(f"Prompt Name: {name}")
        print(f"Prompt Content:\n {content}\n")
