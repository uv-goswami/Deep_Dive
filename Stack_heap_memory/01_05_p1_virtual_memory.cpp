#include <iostream>

int main(){
    int* p = new int(999);

    std::cout<<"A:" << p << "=" << *p << std::endl ;
    std::cin.get();

    return 0;

}