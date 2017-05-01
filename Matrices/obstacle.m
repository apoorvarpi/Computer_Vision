function [obs]=obstacle()
    fileid = fopen('obstacle.txt','r');
    %filespec = '%d %d';
    k = 1;
    while ~feof(fileid)
        obs_x = fscanf(fileid,'%d');
        obs_y = fscanf(fileid,'%d');
        obs(k,1) = obs_x;
        obs(k,2) = obs_y;
        if ~isempty(obs(k))
            k = k+1;
        end
    end
    fclose(fileid);   
end
