create or replace procedure prc_insertar_multa(
    v_monto   number,
    v_descripcion varchar2,
    v_fecha      date,
    v_cliente number,
    v_salida      out number


)is
begin

  insert into multa ( monto_multa,descripcion,fecha_multa,multa_cliente_id) 
                            values (v_monto,v_descripcion,v_fecha,v_cliente);
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;