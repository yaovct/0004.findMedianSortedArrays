# g++ -g -std=gnu++11 index.cpp index_unittest.cc index_main.cc -o index -L/usr/local/lib/ -lgtest -lgtest_main -pthread
#

# compiler
CC = g++

INCLUDE = -I/usr/lcoal/include/
LIBPATH = -L/usr/local/lib/

SRC = index.cpp index_unittest.cc index_main.cc
OBJ = $(SRC:.c=.o)
OUT = index

CFLAGS = -g -std=gnu++11
TFLAGS = -lgtest -lgtest_main -pthread

$(OUT): $(OBJ)
	$(CC) $(CFLAGS) $(SRC) -o $@ $(LIBPATH) $(TFLAGS)

clean:
	rm -f $(OUT) *.o *.exe