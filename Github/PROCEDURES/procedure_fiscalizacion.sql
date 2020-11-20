----INSERTA EN LA TABLA DE FISCALIZACION

create or replace procedure prc_insertar_fiscalizacion(
    v_doc_revisados             varchar2,
    v_descripcion_documento     varchar2,
    v_documento                 varchar2,
    v_rut_cliente_id            varchar2,
    v_salida                    out number

)is
begin

insert into fiscalizacion (doc_revisados,descripcion_documento,documento,rut_cliente_id) 
                    values (v_doc_revisados,v_descripcion_documento,v_documento,v_rut_cliente_id);
commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;

end;


----LISTA LAS FISCALIZACIONES REALIZADAS

create or replace procedure prc_listar_fiscalizaciones(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select * from fiscalizacion;

end;