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
    if(file[i].length() == 3)
    {
        printf("ok");
    }
  }    
for(int i = 0; i < 4; i++) {
    if(file[i].length() == 5)
    {
        printf("all files found\n");
    }
  }    

  return 0;
}
