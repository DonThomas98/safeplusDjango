--PROCEDURE QUE SE DEBERA EJECUTAR AL MOMENTO DE PAGAR Y INICIO DE MES PARA CONFIRMAR PAGOS Y ACTIVAR/DESACTIVAR USUARIOS MOROSOS
create or replace procedure prc_pagos
is
begin
declare

cursor cur_clientes_sin_pagar is
    select auth_user.id 
    from auth_user join contrato
    on auth_user.id=contrato.rut_cliente_id
    where is_staff =0
    order by auth_user.id asc;
    
id_cliente auth_user.id%TYPE;

begin

open cur_clientes_sin_pagar;
    loop
    fetch cur_clientes_sin_pagar into id_cliente; 
    exit when cur_clientes_sin_pagar%notfound;
    
    if fn_se_pago(id_cliente) ='TRUE' then
    
        update auth_user set is_active=1
    where id=id_cliente;
    

    
    else
    
    update auth_user set is_active=0 
    where id=id_cliente;

    
    end if;
    end loop;
close cur_clientes_sin_pagar;
end cur_clientes_sin_pagar;
exception when others then
    DBMS_OUTPUT.PUT_LINE('SE PRODUJO UN ERROR EN EL BLOQUE PL/SQL'||SQLCODE);


end prc_pagos ;



---PROCEDURE QUE INHABILITA LOS CLIENTES


create or replace procedure prc_inhabilitar_cliente(
v_user_id    in    auth_user.id%TYPE
)is
begin

UPDATE auth_user SET is_active = 0 where id = v_user_id;
commit;

end;


---PROCEDURE QUE HABILITA CLIENTES


create or replace procedure prc_habilitar_cliente(
v_user_id    in    auth_user.id%TYPE
)is
begin

UPDATE auth_user SET is_active = 1 where id = v_user_id;
commit;

end;


---INSERTA VALORES BASE (0) para poder ver cuanto han pagado y no salga nulo
--ESTO DEBERA CARGARSE CADA MES
create or replace procedure prc_pagos_base
is
begin
declare

cursor cur_clientes_sin_pagar is
    select auth_user.id ,contrato.id
    from auth_user join contrato
    on auth_user.id=contrato.rut_cliente_id
    where is_staff =0
    order by auth_user.id asc;
    
id_cliente auth_user.id%TYPE;
id_contrato contrato.id%TYPE;

begin

open cur_clientes_sin_pagar;
    loop
    fetch cur_clientes_sin_pagar into id_cliente,id_contrato; 
    exit when cur_clientes_sin_pagar%notfound;
    
    DBMS_OUTPUT.PUT_LINE('SE INSERTARON VALORES PARA EL CLIENTE NUMERO: '||id_cliente||'CON SU CONTRATO NUMERO:'||id_contrato);
    insert into costo_adicional (monto_adicional,fecha_costoadicional,id_contrato_id) 
                        values  (0,sysdate,id_contrato);
    insert into registro_pagos (monto_pago,fecha_pago,id_contrato_id)
                        values  (0,sysdate,id_contrato);
                        
    end loop;
close cur_clientes_sin_pagar;
end cur_clientes_sin_pagar;
exception when others then
    DBMS_OUTPUT.PUT_LINE('SE PRODUJO UN ERROR EN EL BLOQUE PL/SQL'||SQLCODE);


end prc_pagos_base ;

-----------

create or replace procedure prc_listar_contratos_por_id_cliente(clientes_datos out SYS_REFCURSOR,
v_rut_cliente_id number)
is

begin
open clientes_datos for  select * from contrato
                        where rut_cliente_id=v_rut_cliente_id;

end;

--PROCEDURE QUE INSERTA PAGOS


create or replace procedure prc_insertar_pago(
    v_monto   number,
    v_fecha      date,
    v_contrato number,
    v_salida      out number


)is
begin

  insert into registro_pagos ( monto_pago,fecha_pago,id_contrato_id) 
                            values (v_monto,v_fecha,v_contrato);
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;