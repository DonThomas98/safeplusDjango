--ESTE TRIGGER SE INVOCA AL MOMENTO DE CREAR UN CLIENTE , SE LE CREA UN CONTRATO
create or replace trigger trg_crearcontrato
after insert on auth_user
for each row

begin
    if  :NEW.is_staff=0 then
        insert into contrato (descripcion,costo,fecha_contratacion,rut_cliente_id) 
                     values ('Plan Universal',150000,CURRENT_DATE,:NEW.id);
    end if;

end;


--TRIGGER INVOCADO AL MOMENTO DE HACER UN INSERT DE UN PAGO , INVOCA EL PROCEDURE QUE VERIFICA LOS PAGOS CON EL MES
CREATE  OR REPLACE  TRIGGER trg_pago_realizado
AFTER INSERT
   ON registro_pagos
    FOR EACH ROW 

DECLARE



BEGIN
    prc_pagos();
    
END;
