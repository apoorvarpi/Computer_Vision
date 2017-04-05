from perspective_new import *

def main(size):
    for i in range(1,size+1):
        name = "./input/C"+str(i)+"/bw.jpg"
        name1 = "./input/C"+str(i)+"/pers2.jpg"
        final_pers(name, name1)

main(4)
