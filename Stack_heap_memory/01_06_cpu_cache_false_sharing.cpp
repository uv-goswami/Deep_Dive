#include <iostream>
#include <thread>
#include <chrono>


struct PlayerStats{
    alignas(64) long health;
    alignas(64) long armor;
};
PlayerStats stats;

void updateHealth(){
    for(int i=0; i<100000000; i++){
        stats.health++;
    }
}

void updateArmor(){
    for(int i = 0; i<100000000; i++){
        stats.armor++;
    }
}

int main(){

    auto start = std::chrono::high_resolution_clock::now();

    std::thread t1(updateHealth);
    std::thread t2(updateArmor);

    t1.join();
    t2.join();

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end -start;

    std::cout<<"Time taken: "<< diff.count() << std::endl;

    return 0;
}