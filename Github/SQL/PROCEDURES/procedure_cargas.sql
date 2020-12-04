create or replace procedure prc_listar_carga_visitas(clientes_datos out SYS_REFCURSOR,
v_rut_cliente_id number

)
is

begin
open clientes_datos for 
select   username ,to_char(fecha_visita,'dd/mm/yyyy'),motivo_visita from auth_user 
        join visita_terreno 
        on auth_user.id=visita_terreno.rut_trabajador_id 
        where to_char(fecha_visita,'mm/yyyy')=to_char(CURRENT_DATE ,'mm/yyyy') 
        and
        rut_trabajador_id=v_rut_cliente_id
        order by fecha_visita asc;
end;



----LISTA LAS CAPACITACIONES Y SU DIA


create or replace procedure prc_listar_carga_capacitaciones(clientes_datos out SYS_REFCURSOR,
v_rut_cliente_id number

)
is

begin
open clientes_datos for 
select  username ,to_char(fecha_capacitacion,'dd/mm/yyyy'),hora_capacitacion
        from auth_user 
        join capacitacion 
        on auth_user.id=capacitacion.rut_trabajador_id 
        where to_char(fecha_capacitacion,'mm/yyyy')=to_char(CURRENT_DATE ,'mm/yyyy') 
        and
        rut_trabajador_id=v_rut_cliente_id
        order by fecha_capacitacion asc;
end;

