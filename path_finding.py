#Finding path from every node , i.e node 0
import numpy as np
import cv2

def find_path(graph,start,end, path=[]) :
    path=path+[start]
    if start==end :
        return path
    if start not in graph :
        return None
    else :
        for node in graph[start] :
                 if node not in path:
                    newpath = find_path(graph, node, end, path)
                 if newpath :
                    return newpath
        return None

def obtain_graph(M,size):
    graph = {}
    for i in range(1,size):
        node = i;
        adj = []
        for j in range(0,size-1):
            if(M[i][j]==1):
                adj.append(j)
        graph[node] = adj
    return graph

def convert_path(path1):
    path = []
    for i in range(0,len(path1)):
        path.append(path1[i]+1)
    return path

def save_path(M,size):
    graph = obtain_graph(M,size)
    visited = {}
    for i in graph.keys():
        visited[i] = False
    for i in range(1, size):
        start = i
        end = 0
        #print(i+1," to 1")
        path = convert_path(find_path(graph,start,end))
        #print(path)
        if(len(path)>2):
            create_matrix(path)

def create_matrix(path):
    im_nm1 = "C"+str(path[0])
    im_nm2 = "C"+str(path[1])
    for i in range(2,len(path)):
        im_nm3 = "C"+str(path[i])
        im_file1 = "./Matrices/"+im_nm1+"_"+im_nm2+".npy"
        im_file2 = "./Matrices/"+im_nm2+"_"+im_nm3+".npy"
        M1 = np.load(im_file1)
        M2 = np.load(im_file2)
        M = M1*M2
        file_name = "./Matrices/"+im_nm1+"_"+im_nm3
        np.save(file_name,M)
        print("Saved file ",im_nm1,"_",im_nm3)

        im_src1 = cv2.imread("input/C1/calib.jpg")
        im_nm2 = "input/"+im_nm1+"/calib.jpg"
        im_src2 = cv2.imread(im_nm2)
        rows,cols,ch = im_src1.shape
        im_dst = cv2.warpPerspective(im_src2, M, (cols,rows))
        cv2.imshow("Final Image",im_dst)
        cv2.waitKey(0)

        im_nm2 = im_nm3

def final_matrices(size):
    file_name = "./Matrices/adjacency_matrix.npy"
    M = np.load(file_name)
    save_path(M,size)
