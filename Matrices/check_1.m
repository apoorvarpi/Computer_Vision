function [curr_x,curr_y]=check_1()
    fileid = fopen('Pa.txt','r');
    filespec = '%d %d';
    A = fscanf(fileid, filespec);
    fclose(fileid);
    curr_x=A(1);
    curr_y=A(2);
end