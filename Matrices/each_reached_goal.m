function flag=each_reached_goal(goal,robots)
    ct =0;
    flag=0;
    for m=1:numel(robots)/2
        df_x = goal(1)-robots(m,1);
        df_y = goal(2)-robots(m,2);
        dis = sqrt(df_x*df_x+df_y*df_y);
        if(dis<40)
            ct = ct+1;
            %break;
        end
    end
    if(ct==(numel(robots)/2))
        flag=1;
    end
end