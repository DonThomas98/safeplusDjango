----PROCEDURE QUE CREA LA VISITA A TERRENO


create or replace procedure prc_insertar_visita(
    v_motivo         varchar2,
    v_visita_fecha      date,
    v_rut_cliente        number,
    v_rut_trabajador       number,
    v_salida      out number

)is
begin

insert into visita_terreno  (motivo_visita,fecha_visita,rut_cliente_id, rut_trabajador_id)
VALUES (v_motivo,v_visita_fecha, v_rut_cliente, v_rut_trabajador); 
commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;

end;


---

