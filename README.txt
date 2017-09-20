Build instruction
Install BOOST
wget -O boost_1_55_0.tar.gz http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz/download
wget -O https://dl.bintray.com/boostorg/release/1.64.0/source/
tar xzvf boost_1_55_0.tar.gz
tar xzvf 1.64.0
cd boost_1_55_0/

Install Cmake
wget https://cmake.org/files/v3.8/cmake-3.8.1.tar.gz
tar xzvf cmake*.tar.gz
cd cmake*
./configure --prefix=$HOME
make
make install

Build boost

./bootstrap.sh --prefix=/usr/local
./b2

The whole process might take at least 1 hour -- see below for to simply test algorithm

To Build After installing boost and boost libraries 

g++ -o Algorithms3 main.cpp -I/usr/include/python2.7 -lpython2.7

::To run 
Unzip file and run 
./Algorithms3 filename 

if that fails or want to quickly check run and check output contents without using boost and cmake 
just type 
python graph3.py filename 

Report under: GraphModel.pdf

