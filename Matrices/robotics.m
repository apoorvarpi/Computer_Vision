delete(instrfindall);
clear s
s = serial ('COM5');
set(s,'BaudRate',9600);
fopen (s);
obstacles=[80, 120; 160, 80];
robots=check();
goal=[300,200];
curr_x=0;
curr_y=0;
curr_theta=0;
i=1;
while(1)
    [curr_x,curr_y]=check();
    [next_x, next_y]=getposition(obstacles,robots,goal,curr_x,curr_y);
% %    pause(1);
%     if(next_x==curr_x && next_x==curr_y)
%         break;
%     end
    result_x(i)=next_x;
    result_y(i)=next_y;
    i=i+1;
    dx=next_x-curr_x;
    dy=next_y-curr_y;
    
    next_theta=atan2(dy,dx)*180/pi;
    theta_robot=next_theta-curr_theta
        next_x
        next_y
    if(abs(theta_robot)>5)       
     if(theta_robot<0)
              send_data(s,4,abs(theta_robot));
    else
               send_data(s,3,abs(theta_robot));
     end 
    end
    linear=sqrt((dx*dx+dy*dy));
 %   orientation=frombishnu();
    orientation=0;
    send_data(s,1,linear);

    curr_x=next_x;
    curr_y=next_y;
    curr_theta=next_theta;
    
    robot(1,1)=curr_x;
    robot(1,2)=curr_y;
    dx=abs(goal(1)-curr_x);
    dy=abs(goal(2)-curr_y);
    if(sqrt(dx*dx+dy*dy)<30)
        break;
    end  
end

clf('reset');
plot(result_x,result_y,'-o');hold on;
no_of_obstacles=numel(obstacles)/2;
for i=1:no_of_obstacles
    x=obstacles(i,1);
    y=obstacles(i,2);
    plot(x,y,'-r *');
    th = 0:pi/50:2*pi;
    r=50;
    xunit = r * cos(th) + x;
    yunit = r * sin(th) + y;
    h = plot(xunit, yunit);
end
hold off;

fclose(s);