import os
import random
import string
from colorama import init, Fore, Style
from pyfiglet import Figlet
from tqdm import tqdm
import time

init()  # Initialize colorama for cross-platform color support

output = []
path = os.path.realpath(os.path.dirname(__file__))


def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for _ in range(length))
    return result_str


def validate_email(email):
    if "@gmail.com" not in email:
        print(Fore.RED + "Oops! That doesn't look like a Gmail address. Try again, Gmail wizard!" + Style.RESET_ALL)
        return False
    return True


def prefixgen(export_amount, email):
    email_core = email.replace("@gmail.com", "")
    for _ in tqdm(range(export_amount), desc="Brewing Suffixes", unit="pinch"):
        random_id = get_random_string(random.randint(5, 10))
        final = f"{email_core}+{random_id}@gmail.com"
        output.append(final)
        time.sleep(0.1)  # Simulate processing time for visual effect
    print(Fore.GREEN + "\nSuffixes brewed to perfection!" + Style.RESET_ALL)
    export_prefixes(path)


def export_prefixes(export_dir):
    try:
        directory = os.path.join(export_dir, "GmailSuffixes.txt")
        with open(directory, 'w') as file:
            file.write("\n".join(output))
        print(Fore.GREEN + f"Suffixes exported to: {directory}" + Style.RESET_ALL)
        print(Fore.CYAN + "Now you can create email addresses that are as unique as a unicorn's fingerprint!" + Style.RESET_ALL)
    except IOError:
        print(Fore.RED + "Oops! The suffix exporter took a wrong turn. Please try again!" + Style.RESET_ALL)


def display_banner():
    figlet = Figlet(font='slant')
    banner = figlet.renderText("Gmail Suffix Wizard")
    colored_banner = Fore.MAGENTA + banner + Style.RESET_ALL
    print(colored_banner)
    print(Fore.CYAN + "Crafted by: tnkrueckergreen, the Suffix Sorcerer" + Style.RESET_ALL)
    print(Fore.YELLOW + "Prepare to be amazed by the magic of unique email suffixes!" + Style.RESET_ALL)


def display_animation():
    animation = ["🌟", "✨", "💫", "🔮", "🪄"]
    for i in range(20):
        time.sleep(0.1)
        print(Fore.MAGENTA + f"\rConjuring magic... {animation[i % len(animation)]}", end="", flush=True)
    print(Fore.GREEN + "\nWelcome to the Gmail Suffix Wizard's Lair!" + Style.RESET_ALL)


def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        display_animation()

        print(Fore.CYAN + """
[1] Conjure Suffixes
[2] Vanish
""" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "Choose your destiny: " + Style.RESET_ALL)

        if choice == "1":
            while True:
                email = input(Fore.YELLOW + "Reveal your Gmail address, mortal: " + Style.RESET_ALL)
                if validate_email(email):
                    break
            
            while True:
                gen_amount = input(Fore.YELLOW + "How many suffixes shall I summon? " + Style.RESET_ALL)
                if gen_amount.isdigit() and int(gen_amount) > 0:
                    gen_amount = int(gen_amount)
                    break
                else:
                    print(Fore.RED + "Invalid incantation! Please provide a positive integer." + Style.RESET_ALL)

            prefixgen(gen_amount, email)
            print(Fore.GREEN + "Suffixes conjured and exported with mystical prowess!" + Style.RESET_ALL)
            print(Fore.CYAN + "Prepare to unleash the power of unparalleled email sorcery!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue your suffix quest..." + Style.RESET_ALL)

        elif choice == "2":
            print(Fore.GREEN + "May the power of suffixes be with you always. Until next time, email wizard!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid spell! Please try again, mighty suffix conjurer." + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to resume your suffix journey..." + Style.RESET_ALL)


if __name__ == "__main__":
    main_menu()
