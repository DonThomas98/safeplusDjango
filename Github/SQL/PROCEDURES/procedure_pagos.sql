create or replace procedure prc_pagos
is
begin
declare

cursor cur_clientes_sin_pagar is
    select auth_user.id from auth_user 
    join account_userprofile
    on auth_user.id=account_userprofile.user_id
    where is_staff =0;
    
id_cliente auth_user.id%TYPE;

begin

open cur_clientes_sin_pagar;
    loop
    fetch cur_clientes_sin_pagar into id_cliente; 
    exit when cur_clientes_sin_pagar%notfound;
    
    if fn_monto_pagado(id_cliente) != fn_montos_adicionales(id_cliente)+fn_monto_contrato(id_cliente) then
    
    update auth_user set is_active=0 
    where id=id_cliente;
    
    end if;
    end loop;
close cur_clientes_sin_pagar;
end cur_clientes_sin_pagar;

end prc_pagos ;