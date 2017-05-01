function [curr_x,curr_y]=check_2()
    fileid = fopen('Pb.txt','r');
    filespec = '%d %d';
    A = fscanf(fileid, filespec);
    fclose(fileid);
    curr_x=A(1);
    curr_y=A(2);
end

