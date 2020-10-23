#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"

int main(){
    printf("%s>= Update && Upgrade <=\n", KYEL);
    sleep(1);
    printf("\n%s[+]%sONLY DEBIAN BASED SUPPORT%s[+]%s\n\n",KRED, KCYN, KRED, KWHT);
    sleep(4);
    system("sudo apt-get update -y && sudo apt-get upgrade -y");
    sleep(1);
    printf("\n%s[+]%sInstall colorama%s[+]%s\n", KRED, KCYN, KRED, KWHT);
    system("pip3 install colorama");
    system("pip install colorama");
    return 0;
}
