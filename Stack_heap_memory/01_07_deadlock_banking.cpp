#include <iostream>
#include <thread>
#include <mutex>

struct Account{
    int id;
    int balance;
    std::mutex m;
};

void transfer(Account& from, Account& to, int amount){

    from.m.lock();

    std::this_thread::sleep_for(std::chrono::milliseconds(10)); //used to get forced deadlock

    to.m.lock();


    from.balance -= amount;
    to.balance += amount;

    to.m.unlock();
    from.m.unlock();
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