#include <iostream>
#include <vector>

void fregmentation_scenerio(){
    std::vector<void*> ptrs;
    std:: cout<<"Allocating 1million 1Kb objects";

    for(int i =0; i<1000000; i++){
        ptrs.push_back(new char[1024]);
    }

    for(int i = 0; i<1000000; i+=2){
        delete[] (char*)ptrs[i];
    }

    try{
        char* NewBlock = new char[200*1024*1024];
        std::cout<<"success"<<std::endl;
        delete[] NewBlock;

    }catch (const std::bad_alloc& e){
        std::cerr<<"Crash"<<e.what()<<std::endl;
        

    }
}

int main(){
    fregmentation_scenerio();
    
    return 0;
}