BEGIN
  DBMS_SCHEDULER.create_job (
     job_name          => 'cron_pagos',
     job_type          => 'STORED_PROCEDURE',
     job_action        => 'prc_pagos',
     repeat_interval   => 'FREQ=MONTHLY;',
     enabled           => TRUE,
     comments          => 'Procedimiento almacenado que se ejecuta el primer dia de cada mes , para revisar pagos e inhabilitar clientes en morosidad');
END;



BEGIN
  DBMS_SCHEDULER.create_job (
     job_name          => 'cron_pagos_base',
     job_type          => 'STORED_PROCEDURE',
     job_action        => 'prc_pagos_base',
     repeat_interval   => 'FREQ=MONTHLY;',
     enabled           => TRUE,
     comments          => 'Procedimiento almacenado que se ejecuta el primer dia de cada mes ,inserta pagos con valor de 0 para que funcionen las distintas function,para evitar nulos en la manipulacion de datos');
END;
