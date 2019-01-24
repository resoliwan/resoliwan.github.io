#include <iostream>
#include <fstream>
#include <string>
#include "addressbook.pb.h"

using namespace std;
int main(void)
{
    tutorial::AddressBook address_book;
    fstream input("address.data", ios::in | ios::binary);
    address_book.ParseFromIstream(&input);

    int i = 0;
    for (; i < address_book.people_size(); ++i) {
        const tutorial::Person& person = address_book.people(i);
        cout << person.DebugString() << endl;
    }

    tutorial::Person* p = address_book.add_people();
    (*p).set_name("name");
    (*p).set_id(i);

    fstream output("address.data", ios::out | ios::binary);
    address_book.SerializeToOstream(&output);

    return 0;
}

// protoc --cpp_out=./ ./addressbook.proto
// clang++ -std=c++11 -Wno-c++11-extensions test.cpp addressbook.pb.cc -lprotobuf
