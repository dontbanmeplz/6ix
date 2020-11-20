from colorama import Fore
print(f'''{Fore.RESET}
                                            
                                              ██████  ██▓▒██   ██▒
                                            ▒██    ▒ ▓██▒▒▒ █ █ ▒░
                                            ░ ▓██▄   ▒██▒░░  █   ░
                                              ▒   ██▒░██░ ░ █ █ ▒ 
                                            ▒██████▒▒░██░▒██▒ ▒██▒
                                            ▒ ▒▓▒ ▒ ░░▓  ▒▒ ░ ░▓ ░
                                            ░ ░▒  ░ ░ ▒ ░░░   ░▒ ░
                                            ░  ░  ░   ▒ ░ ░    ░  
                                                ░   ░   ░    ░  
                                          
                      
                                                  
                                {Fore.RED}Loggin =>  {Fore.RED}{SIX.user.name}#{SIX.user.discriminator}{Fore.LIGHTYELLOW_EX}  ||{Fore.LIGHTYELLOW_EX}  {Fore.RED}ID => {Fore.RED}{SIX.user.id}   
                                {Fore.RED}Privnote => {Fore.RED}{privnote}{Fore.LIGHTYELLOW_EX} ||  {Fore.RED}Nitro => {Fore.RED}{nitro} 
                                {Fore.RED}Giveaway => {Fore.RED}{giveaway}{Fore.LIGHTYELLOW_EX}   ||  {Fore.RED}SlotBot => {Fore.RED}{slotbot}
                                {Fore.RED}Prefix => {Fore.GREEN}{prefix}{Fore.LIGHTYELLOW_EX}           ||  {Fore.RED}6ix =>{Fore.LIGHTYELLOW_EX} v{SELFBOT.__version__}                                                     
     '''.replace('░', f'{Fore.RED}░{Fore.RESET}').replace('▒', f'{Fore.RED}░{Fore.RESET}').replace('▓', f'{Fore.RED}░{Fore.RESET}')+Fore.RESET)
