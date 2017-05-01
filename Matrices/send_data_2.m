function []=send_data_2(sr,action,value)
    if(action==1)
        value=value*10;
    end
    value;
    value=int16(value)
    dis = value;
    angle = value;
    stop = '(';
    x = action;
    %x = arr(idx);
    d = num2str(x);
    c = num2str(dis);
    e = num2str(angle);
    if(x==1 || x==2)
        out = strcat(d,c);
    else
        out = strcat(d,e);
    end
    for i=1:length(out)
        fprintf(sr, '%c', out(i));
       % out(i)
    end
    fprintf(sr,'%c',stop);
   pause(0);
     g = input('');
end