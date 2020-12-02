---INSERTA UNA CAPACITACION NUEVA
create or replace procedure prc_insertar_capacitacion(
    v_hora_capacitacion     varchar2,
    v_rut_cliente        number,
    v_rut_trabajador     number,
    v_salida      out number

)is
begin

insert into capacitacion (FECHA_SOLICITUD,FECHA_CAPACITACION,HORA_CAPACITACION,RUT_CLIENTE_ID,RUT_TRABAJADOR_ID)
            values       (sysdate,sysdate+15,v_hora_capacitacion,v_rut_cliente,v_rut_trabajador);
commit;
    v_salida:=1;



    exception 
    when others then 
        v_salida:=0;

end;






---PROCEDURE QUE LISTA CLIENTES YA EXTENDIDOS



create or replace procedure prc_listar_clientes_extendidos(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select auth_user.id,auth_user.username 
from auth_user  join account_userprofile
 on auth_user.id=account_userprofile.user_id
   where auth_user.is_staff =0 and auth_user.is_active=1  ;

end;


----MUESTRA LA FECHA EN LA QUE SE REALIZARA LA CAPACITACION
create or replace procedure prc_mostrar_dia_capacitacion(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select sysdate+15 from dual; 

end;

----INSERTA LOS NUEVOS MATERIALES A USAR EN CAPACITACIONES



create or replace procedure prc_insertar_materiales(
    v_material      varchar2,
    v_salida      out number


)is
begin

   insert into material_capacitaciones (material) values (v_material);
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;

----LISTA LOS MATERIALES EXISTENTES

create or replace procedure prc_listar_materiales(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select DISTINCT(material) from material_capacitaciones   ;

end;


--LISTA LOS MATERIALES PARA VINCULARLOS A MATERIALES SOLICITADOS


create or replace procedure prc_listar_material(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  SELECT ID,MATERIAL FROM material_capacitaciones ORDER BY ID ASC ;

end;





-----INSERTA EN LA TABLA MATERIALES SOLICITADOS
create or replace procedure prc_insertar_materiales_solicitados(
    v_id_material   number,
    v_cantidad      number,
    v_capacitacion_id number,
    v_salida      out number


)is
begin

  insert into material_solicitado ( id_material_id,cantidad,material_capacitacion_id) 
                            values (v_id_material,v_cantidad,v_capacitacion_id);
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;

---LISTA LAS CAPACITACIONES

create or replace procedure prc_listar_capacitaciones(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for select * from capacitacion ORDER BY ID ASC ;

end;



---LISTAR LAS CAPACITACIONES QUE HACE X EMPLEADO EN UN PERIODO DE TIEMPO (FECHA ACTUAL Y LA FECHA A REALIZAR CAPACITACION) ESTO DEBIDO A QUE NO SE PODRA MODIFICAR EL MISMO DIA 
create or replace procedure prc_listar_capacitaciones(clientes_datos out SYS_REFCURSOR,
v_rut_trabajador number)
is

begin
open clientes_datos for select capacitacion.id,capacitacion.fecha_solicitud,capacitacion.fecha_capacitacion,
                        capacitacion.hora_capacitacion,capacitacion.rut_cliente_id,capacitacion.rut_trabajador_id,
                        auth_user.username
                        
                        from capacitacion join auth_user
                        on capacitacion.rut_cliente_id=auth_user.id
                        where rut_trabajador_id=v_rut_trabajador AND capacitacion.fecha_capacitacion BETWEEN sysdate AND fecha_capacitacion  ORDER BY ID ASC ;

end;

