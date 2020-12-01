---PROCEDURE PARA QUE EL CLIENTE REPORTE ACCIDETNES
create or replace procedure prc_reportar_accidente(
    v_naturaleza   varchar2,
    v_partes_accidentadas      varchar2,
    v_fuente_accidente_id varchar2,
    v_fecha_accidente date,
    v_rut_cliente_id number,
    v_salida      out number


)is
begin

  insert into accidente ( naturaleza,partes_accidentadas,fuente_accidente,fecha_accidente,rut_cliente_id) 
                            values (v_naturaleza,v_partes_accidentadas,v_fuente_accidente_id,v_fecha_accidente,v_rut_cliente_id);
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;
----------------------

-----PROCEDURE QUE LISTA LOS ACCIDENTES

create or replace procedure prc_listar_accidentes(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select * from accidente;

end;


-----PROCEDURE QUE LISTA LOS ACCIDENTES DE ACUERDO A LA ID DEL CLIENTE

create or replace procedure prc_listar_accidentes_por_id(clientes_datos out SYS_REFCURSOR,
v_rut_cliente_id number

)
is

begin
open clientes_datos for  select * from accidente where rut_cliente_id=v_rut_cliente_id;

end;

