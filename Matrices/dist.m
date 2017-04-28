function d=dist(x,i,curr_pos)
    dx=abs(curr_pos(1)-x(i,1));
    dy=abs(curr_pos(2)-x(i,2));
    d=sqrt(dx*dx+dy*dy);
end