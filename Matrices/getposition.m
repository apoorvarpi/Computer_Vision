function [x,y]=getposition(obstacle,robot,goal,curr_x,curr_y)
    dt=20;
    force_att_x=goal(1)-curr_x;
    force_att_y=goal(2)-curr_y;
    d_star = 80;
    eta = 2;
    mag = 0;
    dis = sqrt(force_att_x*force_att_x+force_att_y);
    if(dis<20)
        x = curr_x;
        y = curr_y;
        return
    end
    if(dis>d_star)
        mag = d_star*eta;
    else
        mag = eta*dis*dis;
    end
    force_att_x = force_att_x * mag;
    force_att_y = force_att_y * mag;
    force_rep_x=0;
    force_rep_y=0;
    curr_pos=[curr_x,curr_y];
    eps=50;
    neta=700;
    no_of_obstacles=numel(obstacle)/2;
    for i=1:no_of_obstacles
        d=dist(obstacle,i,curr_pos);
        if(d<eps)
            force_rep_x=force_rep_x+neta*(curr_x-obstacle(i,1));
            force_rep_y=force_rep_y+neta*(curr_y-obstacle(i,2));
        end
    end
   dx_rep_robot = 0;
   dy_rep_robot = 0;
   epsi = 40;
   con = 800;
   for i=1:numel(robot)/2
       d=dist(robot,i,curr_pos);
       if(d<epsi)
           magnitude = d*10;
           dx_rep_robot = dx_rep_robot+magnitude*(curr_x-robot(i,1));
           dy_rep_robot = dy_rep_robot+magnitude*(curr_y-robot(i,2));
       else if(d>epsi && d<80)
          magnitude = d*con*0.001;
          dx_rep_robot = dx_rep_robot-magnitude*(curr_x-robot(i,1));
          dy_rep_robot = dy_rep_robot-magnitude*(curr_y-robot(i,2));
           end
       end
   end
%     force_rep_x;
%     force_rep_y;
%     force_att_x;
%     force_att_y;
    force_net_x = force_rep_x+force_att_x+dx_rep_robot;
    force_net_y = force_rep_y+force_att_y+dy_rep_robot;
    theta = atan2(force_net_y,force_net_x);
    
    if(sqrt(force_net_y*force_net_y+force_net_x*force_net_x)==0)
        x=curr_x;
        y=curr_y;
   %     theta=theta+pi/2;  
    end
    x=curr_x+cos(theta)*dt;
    y=curr_y+sin(theta)*dt;
end