# How to

Żeby prompt mógł być użyty w zadaniu musi być zdefiniowany w pliku o rozszerzeniu `.md` w katalogu `./prompts`.

Prompt musi mieć nadaną unikalną nazwę, która definiowana jest w typie markdownowego code blocku.

Prompty interpolowane są jako pythonowe stringi.

Przykładowy prompt:

    ```ease_prompt=example_name
    This is an example prompt with {variable} and {another_variable}.
    ```

