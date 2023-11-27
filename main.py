import prompts

MENU = """
1 ) addieren
2 ) subtrahieren
3 ) multiplizieren
4 ) dividieren
q ) Quit
"""

menu_dict = {
    "1": prompts.prompt_addieren,
    "2": prompts.prompt_subtrahieren,
    "3": prompts.prompt_multiplizieren,
    "4": prompts.prompt_dividieren,
    "69": prompts.prompt_69
}

print(MENU)
while (a := input("Was darf es sein? ")) != "q":
    try:
        menu_dict[a]()
    except KeyError:
        print("Ungültige Eingabe")

    print(MENU)
