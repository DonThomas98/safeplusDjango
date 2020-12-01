create or replace trigger trg_crearcontrato
after insert on auth_user
for each row

begin
    if  :NEW.is_staff=0 then
        insert into contrato (descripcion,costo,fecha_contratacion,rut_cliente_id) 
                     values ('Plan Universal',150000,CURRENT_DATE,:NEW.id);
    end if;

end;

