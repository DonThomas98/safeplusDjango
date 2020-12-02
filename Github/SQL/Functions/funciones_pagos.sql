---FUNCION QUE VA A BUSCAR CUANTO PAGA CADA EMPLEADO POR SU CONTRATO , NO SE HARDCODEO DEBIDO A QUE ES MAS DINAMICO IR A BUSCARLO ASI
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




--FUNCION QUE VA A BUSCAR TODOS LOS MONTOS ADICIONALES DE EL MES ANTERIOR
create or replace function fn_montos_adicionales
(identificacion auth_user.id%TYPE)
return number is 
monto_pago contrato.costo%TYPE:=0;
begin

select sum(monto_adicional) into monto_pago
from costo_adicional
full join contrato 
on costo_adicional.id_contrato_id=contrato.id
where rut_cliente_id=identificacion
and to_char(fecha_costoadicional,'mm/yyyy')=to_char(add_months(sysdate,-1),'mm/yyyy') ;

return monto_pago ;
end fn_montos_adicionales;

---FUNCION QUE VA A BUSCAR TODO LO PAGADO EN EL MES ANTERIOR
create or replace function fn_monto_pagado
(identificacion auth_user.id%TYPE)
return number is 
monto_pago contrato.costo%TYPE:=0;
begin


select sum(monto_pago) into monto_pago
from registro_pagos 
join contrato 
on registro_pagos.id_contrato_id=contrato.id
where to_char(fecha_pago,'mm/yyyy')=to_char(add_months(sysdate,-1),'mm/yyyy')
and contrato.rut_cliente_id=identificacion;
return monto_pago ;
end fn_monto_pagado;



----ESTA FUNCION JUNTA LAS DEMAS FUNCIONES Y DEVUELVE TRUE SI LA ID ENTREGADA ESTA AL DIA CON LOS PAGOS Y FALSE SI LE FALTA PAGAR

create or replace function fn_se_pago
(identificacion auth_user.id%TYPE)
return varchar2 is 
monto_pago contrato.costo%TYPE:=0;
v_valor varchar2(10);
begin


if (fn_monto_pagado(identificacion)-(fn_montos_adicionales(identificacion)+fn_monto_contrato(identificacion))) = 0 then

v_valor:='TRUE';
else 
v_valor:='FALSE';
end if;
return v_valor ;
end fn_se_pago;


--COMANDOS PARA PROBAR LAS FUNCIONES

select fn_monto_pagado(162),fn_montos_adicionales(162),fn_monto_contrato(162) from dual

--DEVUELVE CUANTO LE FALTA PAGAR
select (fn_monto_pagado(162)-(fn_montos_adicionales(162)+fn_monto_contrato(162))) from dual