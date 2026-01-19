#include <iostream>
int main(){
    int* p = new int(888);
    std::cout << "B: " << p << "= "<< *p << std::endl; 

    std::cin.get();
    return 0;
}