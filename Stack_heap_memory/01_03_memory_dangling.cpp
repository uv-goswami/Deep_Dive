int main(){
    int* p2 = new int(20);
    int* p3 = p2;

    delete p2;  //Line A
    p2 = nullptr;   //Line B

    *p3 = 50;

    return 0;   //Line C
}