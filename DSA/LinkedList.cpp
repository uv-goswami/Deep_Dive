#include <iostream>

using std::cout;
using std::cin;
using std::endl;


class Node{
public:
    int val;
    Node* next;

    Node(int value){
        val = value;
        next = nullptr;

    }
    
};

class LinkedList{
public:
    Node* head;

public:
    LinkedList(){
        head= nullptr;
    }

    Node* traverse(){
        Node* temp = head;
        while(temp->next != nullptr){
            temp = temp->next;
        }
        return temp;
    }

    Node* traverse(int t_value){
        Node* temp = head;
        while(temp->next != nullptr && temp != nullptr){
            
            if(temp->next->val == t_value){
                return temp;
            }
            temp = temp->next;
        }

        return nullptr;
    }


    void insertAtEnd(int value){
        Node* newNode = new Node(value);
        
        if(head == nullptr){
            head = newNode;
            return;
        }
        
        Node* tail = traverse();
        tail->next = newNode;
    }

    void delete_(int value){
        if(head->val == value){
            Node* temp = head;
            head = temp->next;
            delete temp;
        }
        
        if(traverse(value) == nullptr){
            return;
        }

        Node* p_Node = traverse(value);
        
        if(p_Node != nullptr){
            Node * temp = p_Node->next;
            p_Node->next = temp->next;
            delete temp;
        }
    }

    void delete_(){
        while(head != nullptr){
            Node* temp = head;
            head = temp->next;
            delete temp;
        }

        return;
    }

    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->val << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }

    void display_head(){
        cout << "Head:::::::::::::::   " << head->val << endl;
    }

    ~LinkedList(){
        delete_();
    }

};




int main(){
    LinkedList list;
    list.insertAtEnd(1);
    list.display_head();
    list.insertAtEnd(2);
    list.display_head();
    list.insertAtEnd(3);
    list.insertAtEnd(4);

    list.display_head();
    list.display();
    
    list.delete_(2);
    list.display_head();
    list.display();
    return 0;
}