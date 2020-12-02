---ESTE PROCEDURA LISTA LOS TRABAJADORES (IS_STAFF=1 AND ID_SUPERUSER=0) QUE AUN NO HAN SIDO EXTENDIDOS
---0 = Id 
---1 = username
create or replace procedure prc_listar_trabajadores(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select auth_user.id,auth_user.username 
from auth_user left join account_userprofile
 on auth_user.id=account_userprofile.user_id
   where account_userprofile.user_id is null and is_staff=1 and is_superuser=0 ;

end;



----PROCEDURE QUE INSERTA TRABAJADORES EN LA TABLA AUTH_USER y controla errores


create or replace procedure prc_insertar_trabajadores(
    v_usuario      varchar2,
    v_pass         varchar2,
    v_nombre       varchar2,
    v_apellido     varchar2,
    v_correo       varchar2,
    v_salida      out number
)is
begin

    insert into auth_user  (USERNAME,IS_SUPERUSER,PASSWORD, FIRST_NAME, LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED)
    VALUES                  (v_usuario,0,v_pass, v_nombre, v_apellido, v_correo,1,1,sysdate); 
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;



----INSERTA LOS DATOS DE TRABAJADORES EXTENDIDOS
create or replace procedure prc_insertar_datos_trabajador(
    v_rut         number,
    v_sueldo      number,
    v_edad        number,
    v_userid       number,
    v_salida      out number

)is
begin

insert into account_userprofile  (rut,sueldo,edad, user_id)
VALUES (v_rut,v_sueldo, v_edad, v_userid); 
commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;

end;

---PROCEDURE QUE LISTA LOS TRABAJADORES  YA ESTAN EXTENDIDOS

create or replace procedure prc_listar_trabajadores_extendidos(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select auth_user.id,auth_user.username 
from auth_user  join account_userprofile
 on auth_user.id=account_userprofile.user_id
   where auth_user.is_staff =1 and auth_user.is_active=1  ;

end;