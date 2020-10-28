from colorama import Fore, Style


def banner():
    banner = Fore.GREEN +"""                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,  
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::                              
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'          
 ':.  ':.    {1}/___\{0}    ,:'  ,:' 
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
""".format(Fore.GREEN, Fore.WHITE, Fore.RED)
    print(Style.BRIGHT+banner)


banner()
