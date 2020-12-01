
create or replace function fn_monto_contrato
(identificacion auth_user.id%TYPE)
return number is 
monto_pago contrato.costo%TYPE:=0;
begin

select costo into monto_pago 
from contrato 
where rut_cliente_id=identificacion;
return monto_pago ;
end fn_monto_contrato;


