---ESTE PROCEDURE ES PARA INSERTAR EN EL INFORME VISITA Y ASI PODER GENERAR MEDIDAS QUE MEJORAR


create or replace procedure prc_insertar_informe_visita(
    v_introduccion                  varchar2,
    v_RESULTADOS_EVALUACION         varchar2,
    v_AUTOEVALUACION                varchar2,
    v_DOC_ACTUALIZADOS              varchar2,
    v_REG_INTERNO                   varchar2,
    v_DOC_SEREMI_TRABAJO            varchar2,
    v_COPIA_DOCUMENTOS              varchar2,
    v_INFORMA_RIESGOS               varchar2,
    v_INFORMA_MEDIDAS               varchar2,
    v_PROGRAMA_ORDEN                varchar2,
    v_EXTINTORES                    varchar2,
    v_CAPACITACION_EXTINTOR         varchar2,
    v_EPP_INVENTARIO                varchar2,
    v_EPP_CERTIFICADOS              varchar2,
    v_ID_VISITA_ID                  number,
    v_salida                        out number

)is
begin


insert into informe_visita (introduccion,RESULTADOS_EVALUACION,AUTOEVALUACION,DOC_ACTUALIZADOS,REG_INTERNO,
                            DOC_SEREMI_TRABAJO,COPIA_DOCUMENTOS,INFORMA_RIESGOS,INFORMA_MEDIDAS,PROGRAMA_ORDEN,EXTINTORES,
                            CAPACITACION_EXTINTOR,EPP_INVENTARIO,EPP_CERTIFICADOS,ID_VISITA_ID) 

                    values (v_introduccion,v_RESULTADOS_EVALUACION,v_AUTOEVALUACION,v_DOC_ACTUALIZADOS,v_REG_INTERNO,
                            v_DOC_SEREMI_TRABAJO,v_COPIA_DOCUMENTOS,v_INFORMA_RIESGOS,v_INFORMA_MEDIDAS,v_PROGRAMA_ORDEN,
                            v_EXTINTORES,v_CAPACITACION_EXTINTOR,v_EPP_INVENTARIO,v_EPP_CERTIFICADOS,v_ID_VISITA_ID);
commit;
    v_salida:=1;


    exception 
    when others then 
        v_salida:=0;

end;



