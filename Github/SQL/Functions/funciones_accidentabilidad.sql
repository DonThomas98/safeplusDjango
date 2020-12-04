--devuelve el total de clientes
create or replace function fn_total_clientes
return number is 
monto_pago number:=0;
begin


select count(id) into monto_pago
from auth_user WHERE is_staff=0 and is_active=1 ;
return monto_pago ;
end fn_total_clientes;