# How to

Żeby prompt mógł być użyty w zadaniu musi być zdefiniowany w pliku `prompts.md`.

Prompt musi mieć nadaną unikalną nazwę, która definiowana jest w typie markdownowego code blocku.

Prompty interpolowane są jako pythonowe stringi.

Przykładowy prompt:

    ```ease_prompt=example_name
    This is an example prompt with {variable} and {another_variable}.
    ```


---

## Dla każdego rozdziału:

Prompt przygotowujący źródła:

```ease_prompt=sources
Wykonaj jedynie poniższe polecenie.

dla każdego punktu znajdz po 3-4 przydatne źródła linki z różnych stron

{chapter_title}
{chapter_points}

output w postaci:
{chapter_point}
źródła:
    - {link}
    - {link}
    - {link}
```

## Dla każdego podrozdziału:

Przygotowanie podzadań:

```ease_prompt=tasks
Wykonaj jedynie poniższe polecenie.

Wyznacz 3-4 podzadania do wykonania przez agenta w kontekscie napisania treści podrozdziału.
W tym celu dla każdego źródła wyznacz 1-2 podzadanie.

{sources}

output:
podzadania:
    {source}:
        - {link}
    {source}:
        - {link}
    {source}:
        - {link}
```


Znalezienie obrazów
```ease_prompt=images
Wykonaj jedynie poniższe polecenie.

Znajdź 3-4 przydatne obrazy. Do obrazków napisz opis oraz tytuł i podaj adres obrazu.
W tym celu przejrzyj podane źródła. Jeśli nie znajdziesz adekwatnych obrazów w źródłach - szukaj w internecie.

{sources}

output:
obrazy:
    - tytuł: {title}
      opis: {description}
      adres: {link}
```

## Dla każdego podzadania

```ease_prompt=chapter
Na podstawie podzadania przygotuj część treśći podrozdziału. W tym celu wykorzystaj podane źródła.
Tworzysz tylko część dot. podzadania, natomiast ma ona być integralna z pozostałymi częściami.
Nie odnoś się tego, że działasz na podstawie podzadań/części.

{source}
{task}
```