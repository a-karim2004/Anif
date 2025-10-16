# Fichier: anniversaire_code_creatif.py

import time
import sys
    
# Codes ANSI pour les couleurs et le style
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

def taper(texte, delai=0.04):
    """Fonction qui simule la frappe de texte dans le terminal."""
    for caractere in texte:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delai)
    print()
    
def souhaiter_anniversaire_code():
    """Crée une animation de code qui se déploie pour souhaiter un joyeux anniversaire."""
        
    print(BOLD + CYAN + ">>> Initialisation du module 'celebration'...")
    time.sleep(1)
    
    taper(">>> import datetime", delai=0.08)
    taper(f">>> {BOLD}{CYAN}# Définition des paramètres de l'événement{RESET}", delai=0.05)
    
    taper(f"{BOLD}{MAGENTA}>>> def souhaiter_anniversaire à (Abdoul-Karim🥳):{RESET}")
    taper(f"...", delai=0.01)
    taper(f"......{BOLD}{YELLOW}age{RESET} = {BOLD}{GREEN}datetime.date.today().year{RESET} - {BOLD}{GREEN}200...{RESET}  ", delai=0.04)
    taper(f"......{BOLD}{RED}print{RESET}(f'Tu est toujours jeune hein tu na que😌 {BOLD}{BLUE}{{2..🥲 }} ans{RESET} !')", delai=0.04)
    taper(f"......{BOLD}{RED}print{RESET}('Bonne continuation dans tes projets !')", delai=0.04)
    taper("... ")
    
    taper(f">>> {BOLD}{MAGENTA}Alhamdulilah Allah na godé🙏🏻{RESET}('{BOLD}Développeur Incroyable{RESET}')")
    time.sleep(1.5)
    
    print()
    taper(f"{BOLD}{BLUE}Joyeux {RESET}{BOLD}{RED}anniversaire{RESET} {BOLD}Abdoul-Karim{BLUE}!", delai=0.1)
    taper(f"{BOLD}{YELLOW}Un an de plus, un million de lignes de code en plus🫠 !{RESET}", delai=0.05)
    print()
    
    print(BOLD + GREEN + "=================================================" + RESET)
    print(BOLD + GREEN + "==  Félicitations pour une année de plus de code ==" + RESET)
    print(BOLD + GREEN + "==            et de créativité !                 ==" + RESET)
    print(BOLD + GREEN + "=================================================" + RESET)
    
# Point d'entrée du programme
if __name__ == "__main__":
    souhaiter_anniversaire_code()