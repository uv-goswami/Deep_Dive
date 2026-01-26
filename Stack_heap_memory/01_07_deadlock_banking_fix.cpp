#include <iostream>
#include <thread>
#include <mutex>

struct Account{
    int id;
    int balance;
    std::mutex m;
};

void transfer(Account& from, Account& to, int amount){

    std::mutex *first, *second;

    if (from.id < to.id){
        first = &from.m;
        second = &to.m;
    } else {
        first = &to.m;
        second = &from.m;
    }

    first->lock();

    std::this_thread::sleep_for(std::chrono::milliseconds(10)); 

    second->lock();


    from.balance -= amount;
    to.balance += amount;

    first->unlock();
    second->unlock();
}

int main(){
    Account A{1, 1000};
    Account B{2, 500};

    std::thread t1(transfer, std::ref(A), std::ref(B), 100);
    std::thread t2(transfer, std::ref(B), std::ref(A), 50);

    t1.join();
    t2.join();

    std::cout <<"Done\n";
}