#include <python2.7/Python.h>
#include <pyconfig.h>
#include <iostream>
//#include <boost/python.hpp>
#include <cstdlib>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[]) {

    Py_Initialize();
    PySys_SetArgv(argc,argv);

    char const * filename2 = "graph3.py";

    FILE * graphFile = fopen ("graph3.py", "r+");

    PyRun_SimpleFileEx(graphFile, filename2, 1);


    Py_Finalize();

    return 0;
}
