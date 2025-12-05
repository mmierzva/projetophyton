def menu():
    """Exibe o menu principal de escolha de playlist."""
    print("-" * 40)
    print("  BEM VINDO À GERAÇÃO DE PLAYLISTS!!!")
    print("            ESCOLHA SUA OPÇÃO:")
    print(" 1. Rock")
    print(" 2. Metal")
    print(" 3. Soft")
    print("-" * 40)

def escolhaV(opcVal):
    
    while True:
        escolha = input("Digite apenas o número de sua escolha: ")
        if escolha in opcVal:
            return escolha
        else:
            print("Valor inválido, digite APENAS o número de sua escolha.")

def printplay(escolha):
    
    playlists = {
        '1': [
            "1. Foo Fighters - Everlong",
            "2. Billy Idol - Rebel Yell",
            "3. The Rolling Stones - Gimme Shelter",
            "4. Def Leppard - Photograph",
            "5. Misfits - Dig Up Her Bones",
            "6. The Clash - Should I Stay or Should I Go",
            "7. Bon Jovi - Bad Medicine",
            "8. Joan Jett - I Hate Myself for Loving You",
            "9. Pat Benatar - Hit Me With Your Best Shot",
            "10. Twisted Sister - We're Not Gonna Take It"
        ],
        '2': [
            "1. Ozzy Osbourne - Bark at the Moon",
            "2. Slipknot - Psychosocial",
            "3. Metallica - Until It Sleeps",
            "4. Ozzy Osbourne - Road to Nowhere",
            "5. HIM - Wicked Game",
            "6. Ratt - Take a Chance",
            "7. System Of A Down - Toxicity",
            "8. Evanescence - Bring Me To Life",
            "9. Slipknot - Dead Memories",
            "10. Iron Maiden - Wasted Years"
        ],
        '3': [
            "1. Bob Dylan - Blowin' in the Wind",
            "2. David Bowie - Heroes",
            "3. Warrant - Heaven",
            "4. KISS - Shandi",
            "5. Led Zeppelin - Going to California",
            "6. The Rolling Stones - Angie",
            "7. The Beatles - Blackbird",
            "8. Kansas - Dust in the Wind",
            "9. The Cranberries - Dreams",
            "10. The Smiths - Back to the Old House"
        ]
    }
    
    nome = " "
    if escolha == '1': 
        nome = "ROCK"
    elif escolha == '2': 
        nome = "METAL"
    elif escolha == '3': 
        nome = "SOFT"
    
   
    print("\n" + "-" * 40)
    print(f"       PLAYLIST SELECIONADA: {nome}")
    print("-" * 40)

    
    for musica in playlists[escolha]:
        print(musica)
    
    print("-" * 40)
    print("Aproveite suas músicas!")


if __name__ == "__main__":
    opcoes_validas = ['1','2','3']
    
    
    menu()
    escolha = escolhaV(opcoes_validas)
    printplay(escolha)
