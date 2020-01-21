import hashlib as hlib
from clint.textui import puts, indent, colored
import os, requests

hash_nb={1: 'md5', 2: 'sha1', 3: 'sha224', 4: 'sha256', 5: 'sha384', 6: 'sha512'}
hash_len={32: 'md5', 40: 'sha1', 56: 'sha224', 64: 'sha256', 96: 'sha384', 128: 'sha512'}
wordlist={1: ["CrackStation", "https://crackstation.net/files/crackstation.txt.gz"],
          2: ["CrackStation(Small)", "https://crackstation.net/files/crackstation-human-only.txt.gz"],
          3: ["Oxford", "http://ftp.icm.edu.pl/packages/wordlists/dictionaries/Unabr.dict.gz"]}

def display_wordlist():
    print()
    print(colored.green("These are some amazing wordlist!"))
    print()
    with indent(4):
        for n in wordlist:
            print(colored.blue(str(n)+". "+wordlist[n][0]))
            
    nb=get_choice("Wordlist?", True)
    try:
        t=wordlist[nb]
    except:
        puts(colored.red("Incorrect option"))
        home()
        
        
    with indent(5):
        puts(colored.green("=====>")+colored.blue(t[0])+colored.green(" =====>")+colored.red(t[1])+colored.green("<====="))
    home()
    
    
def hash_me(hash_f, text):
    a=hlib.new(hash_f)
    a.update(bytes(text.encode()))
    return a.hexdigest()

def online_crack(text_hash):
    url="https://md5decrypt.net/Api/api.php?code=f1a7cc545403e4ec&email=jonathantchuente@gmail.com"

    try:
        hash_f=hash_len[len(text_hash)]
        with indent(4):
            puts(colored.red(hash_f)+colored.yellow(" detected"))
            print()
    except:
        print(colored.red("Can't find hash function's"))
        return False

    url+="&hash_type="+hash_f+"&hash="+text_hash
    try:
        r=requests.get(url).text
       
    except:
        print(colored.red("An error occured (Check your internet connection first)"))
        return False

    if "CODE ERREUR" in r:
        print(colored.red("Sorry Can't crack this hash ")+colored.blue(text_hash))
        return False
    else:
        with indent(4, quote='*'):
            puts(colored.green("====>")+colored.blue(text_hash)+colored.green("<====")+colored.yellow("  =  ")+colored.green("====>")+colored.red(r)+colored.green("<===="))
        return True
    
def crack(file, text_hash):
    
    if not os.path.exists(file):
        puts(colored.red("File Not Found"))
        return False
    
    try:
        hash_f=hash_len[len(text_hash)]
        with indent(4):
            puts(colored.red(hash_f)+colored.yellow(" detected"))
            print()
    except:
        print(colored.red("Can't find hash function's"))
        return False
    
    a=hlib.new(hash_f)
    with open(file) as f:
        for word in f.readlines():
            word=word[0:-1]
            a.update(bytes(word.encode()))
            b=a.hexdigest()
            if b==text_hash:
                with indent(4):
                    print(colored.blue(text_hash)+colored.yellow("  =  ")+colored.red(word))
                return True

    puts(colored.red("Can't crack please use anoter wordlist or try online wordlist"))


def get_choice(t, to_int=False):
    print()
    nb=input(colored.yellow(t+":> "))
    if to_int:
        try:
            nb=int(nb)
            
        except:
            home()

    return nb
        
        
def display_hash():
    print()
    print(colored.green("What kind of hashing?"))
    print()
    with indent(4):
        for n in hash_nb:
            print(colored.blue(str(n)+". "+hash_nb[n]))
        
    nb=get_choice("Hashing", True)
    try:
        hash_f=hash_nb[nb]
    except:
        print()
        print(colored.red("Incorect Option"))
        print()
        home()
        
    text=get_choice("Enter text hash")

    text_hash=hash_me(hash_nb[nb], text)
    print()
    with indent(4):
        print(colored.blue(text)+colored.yellow("  =  ")+colored.red(text_hash))
    print()
    home()

def display_crack():
    print()
    print(colored.green("What kind of cracking?"))
    print()
    with indent(4):
        puts(colored.blue("1. Local word list"))
        puts(colored.blue("2. Online Crack"))

    nb=get_choice("Option", True)
    if nb == 1:
        text=get_choice("Enter hash to crack")
        file=get_choice("Enter location of wordlist")
        crack(file, text)
        home()

    if nb == 2:
        text=get_choice("Enter hash to crack")
        online_crack(text)
        home()
        
    

def home():
    print()
    puts(colored.yellow("Welcome In HASK@GEEK123"))
    print()
    puts(colored.green("What do you want to do?"))
    print()
    with indent(4):
        puts(colored.blue("1. Hash"))
        puts(colored.blue("2. Crack"))
        puts(colored.blue("3. Wordlist"))
        puts(colored.red("4. Exit"))
        
    nb=get_choice("Option", True)
    if(nb == 1):
        display_hash()
    if(nb == 2):
        display_crack()

    if(nb == 3):
        display_wordlist()

    if(nb == 4):
        puts(colored.red("I hope i have been helpfull bye bye!!!!"))
    
home()




