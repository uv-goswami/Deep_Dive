#include <iostream>
#include <exception>
#include <vector>

using std::cout;
using std::endl;
using std::vector;
using std::cerr;

struct Particle{
    char data[1024];
    bool active;
};

class ParticlePool{
    vector<Particle> pool;

public:
    ParticlePool(size_t size){
        pool.resize(size);
        for(auto& p : pool){
            p.active = false;
        }
    }

    Particle* spawn(){
        for(auto& p : pool){
            if(!p.active){
                p.active = true;
                return &p;
            }
        }
        return nullptr;
    }

    void kill(Particle* p){
        p->active = false;
    }


};

int main(){

    ParticlePool mypool(1024);

    vector<Particle*> activeParticles;

    for(int i =0 ; i< 200*1024; i++){
        Particle* p=  mypool.spawn();
        if(p){
            activeParticles.push_back(p);
        }
    }

    cout<<"Success"<<endl;



    return 0;
}