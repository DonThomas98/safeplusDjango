BEGIN
  DBMS_SCHEDULER.create_job (
     job_name          => 'cron_pagos',
     job_type          => 'STORED_PROCEDURE',
     job_action        => 'prc_pagos ',
     repeat_interval   => 'FREQ=MONTHLY;',
     enabled           => TRUE,
     comments          => 'Procedimiento almacenado que se ejecuta el primer dia de cada mes , para revisar pagos e inhabilitar clientes en morosidad');
END;