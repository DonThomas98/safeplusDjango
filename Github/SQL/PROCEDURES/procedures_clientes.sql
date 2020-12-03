
--1
---ESTE PROCEDURA LISTA LOS CLIENTES  QUE AUN NO HAN SIDO EXTENDIDOS (IS_STAFF=0 AND ID_SUPERUSER=0)
--- 0 =ID DE AUTH_USER 
--- 1 =USERNAME DE AUTH_USER
create or replace procedure prc_listar_clientes(clientes_datos out SYS_REFCURSOR)
is

begin
open clientes_datos for  select auth_user.id,auth_user.username 
from auth_user left join account_userprofile
 on auth_user.id=account_userprofile.user_id
   where account_userprofile.user_id is null and is_staff=0 ;

end;






--2
--Este procedure INSERTA CLIENTES en la tabla auth_user y controla errores


create or replace procedure prc_insertar_cliente(
    v_usuario      varchar2,
    v_pass         varchar2,
    v_nombre       varchar2,
    v_apellido     varchar2,
    v_correo       varchar2,
    v_salida      out number
)is
begin

    insert into auth_user  (USERNAME,IS_SUPERUSER,PASSWORD, FIRST_NAME, LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED)
    VALUES                  (v_usuario,0,v_pass, v_nombre, v_apellido, v_correo,0,1,CURRENT_DATE); 
    commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;
end;




--INSERTA DATOS DE LOS CLIENTES , LOS EXTIENDE

create or replace procedure prc_insertar_datos_cliente(
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



---PROCEDURE QUE INSERTA CLIENTE , PENSADO PARA .NET

create or replace procedure prc_insertar_cliente_sin_salida(
    v_usuario      varchar2,
    v_pass         varchar2,
    v_nombre       varchar2,
    v_apellido     varchar2,
    v_correo       varchar2

)is
begin

    insert into auth_user  (USERNAME,IS_SUPERUSER,PASSWORD, FIRST_NAME, LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED)
    VALUES                  (v_usuario,0,v_pass, v_nombre, v_apellido, v_correo,0,1,CURRENT_DATE); 
    commit;



end;

---PROCEDURE QUE EXTIENDE CLIENTE , PENSADO PARA .NET


create or replace procedure prc_insertar_datos_cliente_sin_salida(
    v_rut         number,
    v_sueldo      number,
    v_edad        number,
    v_userid       number

)is
begin

insert into account_userprofile  (rut,sueldo,edad, user_id)
VALUES (v_rut,v_sueldo, v_edad, v_userid); 
commit;
 

end;
