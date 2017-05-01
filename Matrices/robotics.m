 clear s
 clear d
 s = serial('COM5','BaudRate',9600);
 d = serial ('COM4','BaudRate',9600);
 fopen(s);
 fopen(d);
%obstacles = obstacle();
obstacles = [103 74; 186 53; 253 131];
robots = [0,0;0,0];
[curr_x,curr_y]=check_1();
robots(1,1)=curr_x;
robots(1,2)=curr_y;
[curr_x,curr_y]=check_2();
robots(2,1) = curr_x;
robots(2,2) = curr_y;
goal=[300,300];
robots_theta=[0,0];
i=1;
while(1)
    stop = 0;
    for k=1:numel(robots)/2
        if(k==1)
            [curr_x,curr_y]=check_1()
        else
            [curr_x,curr_y]=check_2()
        end
        curr_theta = robots_theta(k)
        [next_x, next_y]=getposition(obstacles,robots,goal,curr_x,curr_y)
        
        if(k==1)
            result_x(i)=next_x;
            result_y(i)=next_y;
        end
        if(k==2)
            wake_x(i) = next_x;
            wake_y(i) = next_y;
        end
        i=i+1;
        dx=next_x-curr_x;
        dy=next_y-curr_y;
        next_theta=atan2(dy,dx)*180/pi
        theta_robot=next_theta-curr_theta;
        if(abs(theta_robot)>5)       
         if(theta_robot<0)
            if(k==1)
               send_data_1(s,4,abs(theta_robot));
            else      
               send_data_2(d,4,abs(theta_robot));
            end
         else
            if(k==1)
               send_data_1(s,3,abs(theta_robot));
            else
                send_data_2(d,3,abs(theta_robot));
            end
         end 
        end
        
        linear=sqrt((dx*dx+dy*dy));
        if(k==1)
           send_data(s,1,linear);
        else
             send_data(d,1,linear);
        end
        curr_x=next_x;
        curr_y=next_y;
        curr_theta=next_theta;
        robots_theta(k) = curr_theta;
        robots(k,1)=curr_x;
        robots(k,2)=curr_y;
         h = input('ff');
        stop=each_reached_goal(goal,robots);
        if(stop==1)
            break;
        end
    end
    if(stop==1)
        break;
    end 
end 
clf('reset');
plot(result_x,result_y,'g x');hold on;
plot(wake_x,wake_y,'r x');hold on;
no_of_obstacles=numel(obstacles)/2;
for i=1:no_of_obstacles
    x=obstacles(i,1);
    y=obstacles(i,2);
    plot(x,y,'r *');
    th = 0:pi/50:2*pi;
    r=40;
    xunit = r * cos(th) + x;
    yunit = r * sin(th) + y;
    h = plot(xunit, yunit);
end
hold off;
fclose(s);
fclose(d);