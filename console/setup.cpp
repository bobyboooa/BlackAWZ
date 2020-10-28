/* system example : DIR */
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* system, NULL, EXIT_FAILURE */
#include <string>
#include <iostream>
using namespace std;


int main() {
  string file[4] = {"console.rb", "banner.py", "setup.cpp", "setup"};
  for(int i = 0; i < 4; i++) {
    cout << i << ": " << file[i] << "\n";
  }    
for(int i = 0; i < 4; i++) {
    if(file[i].length() == 5)
    {
        printf("all files found\n");
    }
  }    

  return 0;
}
/Psyrens Team
/KerNix3 & FOX1EN
/psyrens@protonmail.com
/2020_28_oct
/setup.cpp file on console folder
