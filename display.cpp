#include <string>
#include <stdio.h>
#include <stdlib.h>
#include "display.h"
#include <iostream>
namespace display {
    void TestLib::display(){
        cout<<"First display"<<endl;  
    }  
    void TestLib::display(int a){
        cout<<"Second display"<<endl;  
    }
}
