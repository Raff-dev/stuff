## Dla każdego rozdziału:

Prompt przygotowujący źródła:

```ease_prompt=sources
Wykonaj jedynie poniższe polecenie.

dla każdego punktu znajdz po 3-4 przydatne źródła linki z różnych stron

{chapter_title}
{chapter_points}

output:
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
        - {task}
    {source}:
        - {task}
    {source}:
        - {task}
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
