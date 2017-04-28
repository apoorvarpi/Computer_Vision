function []=send_data(s,action,value)
    if(action==1)
        value=value*10;
    end
    value=int16(value);
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
        fprintf(s, '%c', out(i));
       % out(i)
    end
    fprintf(s,'%c',stop);
   pause(2);
   s = input('');
end