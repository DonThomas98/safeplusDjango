--CURSOR QUE TRAE LOS CLIENTES
declare
id_cliente auth_user.id%TYPE;
cursor cur_clientes_sin_pagar is
    select auth_user.id from auth_user 
    join account_userprofile
    on auth_user.id=account_userprofile.user_id
    where is_staff =0;

begin 

open cur_clientes_sin_pagar;
    loop
    fetch cur_clientes_sin_pagar into id_cliente; 
     exit when cur_clientes_sin_pagar%notfound;
    dbms_output.put_line(id_cliente);
    
    end loop;
close cur_clientes_sin_pagar;
end;
