# 𝓟𝓵𝓾𝓿𝓲ó𝓶𝓮𝓽𝓻𝓸 𝓐𝓻𝓭𝓾𝓲𝓷𝓸 𝓐𝓾𝓽𝓸𝓶𝓪𝓽𝓲𝔃𝓪𝓭𝓸 𝓬𝓸𝓷 𝓟𝔂𝓽𝓱𝓸𝓷

> Es un proyecto de un pluviómetro a base una una placa Arduino unida a dos sensores (humedad y temperatura, y precipitación pluvial), los cuales registran datos que son guardados y graficados automáticamente en el ordenador por medio de Python y luego son enviados a este repositorio.

## 𝓓𝓮𝓼𝓬𝓻𝓲𝓹𝓬𝓲ó𝓷

- El pluviómetro es una herramienta fundamental en la agricultura y la meteorología, ya que mide la precipitación pluvial. A través del pluviómetro o el pluviógrafo se obtiene información sobre las características espaciales de la lluvia, su frecuencia y la cantidad precipitada en un lugar específico. Cualquier extremo en la cantidad de lluvia resulta preocupante: si llueve mucho durante un periodo prolongado, pueden ocurrir inundaciones, deslizamientos o desbordamientos de ríos; si llueve muy poco, existe el riesgo de una disminución alarmante del caudal.
Es por esto que se decidió diseñar y construir un pluviómetro automatizado mediante tecnología Arduino, con el propósito de mejorar las prácticas de riego a través de la reducción del consumo de agua y el fortalecimiento del monitoreo ambiental para una gestión sostenible del recurso hídrico.
- ¿Cómo utilizarlo?
1. Conectar el pluviómetro, mediante un cable USB tipo A a tipo B a la computadora.
2. Abrir el script registrar_pluviometro.py desde el equipo.
3. Abrir el script generar_graficas.py desde el equipo.
4. Monitorear el repositorio.
- Desde cuándo está recolectando datos
Este es un proyecto que se a trabajado en conjunto desde 2024, se han podido recopilar datos del 10-21 de sep, 2024; 22-27 de ago, 2025 y 8-13 de sep, 2026. se piensa seguir utilizando esta herramienta para recopilar datos climáticos y así crear un  banco de datos. Útil para el publico en general.

## 𝓗𝓪𝓻𝓭𝔀𝓪𝓻𝓮 𝓾𝓽𝓲𝓵𝓲𝔃𝓪𝓭𝓸

- Sensor: DHT11, Módulo sensor de nivel de agua / lluvia
- Microcontrolador:Arduino
- Otros componentes:
  Caja protectora
  cables Dupont (jumper wires) MACHO-HEMBRA
  cable USB tipo A a USB tipo B
  Computadora        

## 𝓒ó𝓶𝓸 𝓯𝓾𝓷𝓬𝓲𝓸𝓷𝓪 𝓮𝓵 𝓼𝓸𝓯𝓽𝔀𝓪𝓻𝓮

1. 𝙀𝙡 𝙨𝙚𝙣𝙨𝙤𝙧 𝙙𝙚 𝙡𝙡𝙪𝙫𝙞𝙖 𝙙𝙚𝙩𝙚𝙘𝙩𝙖 𝙘𝙖𝙙𝙖 𝙫𝙚𝙯 𝙦𝙪𝙚 𝙡𝙡𝙪𝙚𝙫𝙚.
  El sensor de agua funciona bajo el principio de conductividad eléctrica del agua. Está compuesto por una serie de pistas de cobre paralelas y expuestas sobre la placa, las cuales permanecen eléctricamente aisladas entre sí mientras se encuentran secas.
Cuando el agua entra en contacto con estas pistas, actúa como conductor y las une parcialmente, generando una resistencia eléctrica variable entre ellas: mientras mayor sea la cantidad de pistas cubiertas por el agua, menor será la resistencia resultante.
Esta variación de resistencia es procesada por un circuito integrado en la propia placa del sensor, el cual arma un divisor de voltaje y convierte dicho cambio en una señal analógica de voltaje proporcional al nivel de agua detectado. Esta señal se entrega a través del pin S (señal), mientras que los pines + y - corresponden a la alimentación (VCC y GND) necesaria para el funcionamiento del circuito.
2. 𝙀𝙡 𝙨𝙚𝙣𝙨𝙤𝙧 𝘿𝙃𝙏11 𝙙𝙚𝙩𝙚𝙘𝙩𝙖 𝙡𝙖 𝙝𝙪𝙢𝙚𝙙𝙖𝙙 𝙮 𝙩𝙚𝙢𝙥𝙚𝙧𝙖𝙩𝙪𝙧𝙖.
   El sensor DHT11 combina dos elementos sensores distintos dentro de una misma carcasa: un sensor de humedad de tipo capacitivo y un termistor para la medición de temperatura.
El sensor de humedad está compuesto por una lámina higroscópica ubicada entre dos placas, formando un pequeño capacitor. Cuando la humedad relativa del aire aumenta, dicha lámina absorbe mayor cantidad de vapor de agua, lo que provoca un cambio en su capacitancia. Este cambio es medido internamente y traducido a un valor de humedad relativa.
El termistor, por su parte, es un componente cuya resistencia eléctrica varía de forma predecible según la temperatura ambiente. Esta variación es igualmente medida y convertida a un valor de temperatura en grados Celsius.
Ambas lecturas son procesadas por un chip integrado dentro del propio sensor, el cual las digitaliza y las transmite a través de un único pin de datos, mediante un protocolo de comunicación propio de una sola línea.
3. 𝙀𝙨𝙩𝙤𝙨 𝙙𝙖𝙩𝙤𝙨 𝙨𝙤𝙣 𝙩𝙧𝙖𝙣𝙨𝙢𝙞𝙩𝙞𝙙𝙤𝙨 𝙢𝙚𝙙𝙞𝙖𝙣𝙩𝙚 𝙘𝙖𝙗𝙡𝙚𝙨 𝙙𝙪𝙥𝙤𝙣𝙩 𝙃𝙀𝙈𝘽𝙍𝘼-𝙈𝘼𝘾𝙃𝙊 𝙖 𝙡𝙖 𝙥𝙡𝙖𝙘𝙖 𝘼𝙧𝙙𝙪𝙞𝙣𝙤 𝙐𝙣𝙤.
   La placa Arduino UNO actúa como el microcontrolador central encargado de leer, procesar y transmitir los datos provenientes de los sensores conectados a ella.
Para el sensor de agua, que entrega una señal analógica de voltaje, la placa utiliza su conversor analógico-digital (ADC) integrado, el cual toma esa señal continua y la traduce a un valor numérico que el programa puede interpretar.
Para el sensor DHT11, que se comunica mediante un protocolo digital propio de una sola línea, la placa mide los tiempos exactos de los pulsos eléctricos enviados por el sensor, decodificándolos —generalmente con ayuda de una librería específica para obtener los valores de temperatura y humedad.
4. 𝙇𝙤𝙨 𝙙𝙖𝙩𝙤𝙨 𝙨𝙤𝙣 𝙚𝙣𝙫𝙞𝙖𝙙𝙤𝙨 𝙖 𝙩𝙧𝙖𝙫é𝙨 𝙙𝙚𝙡 𝙥𝙪𝙚𝙧𝙩𝙤 𝙨𝙚𝙧𝙞𝙖𝙡 𝙢𝙚𝙙𝙞𝙖𝙣𝙩𝙚 𝙘𝙤𝙣𝙚𝙭𝙞ó𝙣 𝙐𝙎𝘽 𝙖 𝙡𝙖 𝙘𝙤𝙢𝙥𝙪𝙩𝙖𝙙𝙤𝙧𝙖.
   Una vez obtenidas ambas lecturas, el programa cargado en la placa (ejecutado de forma continua dentro de su ciclo principal) las combina y las envía a través del puerto serial mediante conexión USB, en forma de texto plano, listas para ser recibidas y almacenadas por la computadora conectada.
5. 𝙀𝙡 𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙖 𝘼𝙧𝙙𝙪𝙞𝙣𝙤 𝙄𝘿𝙀 𝙞𝙣𝙨𝙩𝙖𝙡𝙖𝙙𝙤 𝙚𝙣 𝙚𝙡 𝙤𝙧𝙙𝙚𝙣𝙖𝙙𝙤𝙧 𝙨𝙚 𝙚𝙣𝙘𝙖𝙧𝙜𝙖 𝙙𝙚 𝙥𝙧𝙤𝙘𝙚𝙨𝙖𝙧 𝙡𝙤𝙨 𝙙𝙖𝙩𝙤𝙨 .
El Arduino IDE es el programa utilizado desde la computadora para escribir, verificar y transferir el código hacia la placa Arduino. De redacta el código, denominado sketch, dentro del editor de texto del programa. Todo sketch debe contener al menos dos funciones: `setup()`, que se ejecuta una única vez al iniciar la placa, y `loop()`, que se repite de manera continua mientras la placa permanezca encendida.
Mediante la opción "Verificar", el IDE compila el código escrito, es decir, lo traduce a un archivo binario comprensible para el microcontrolador, y adicionalmente revisa la existencia de errores de sintaxis antes de continuar con el proceso.
Se selecciona la opción "Cargar" (o "Subir"), dicho archivo binario es enviado a la placa a través del cable USB, siempre que se encuentren correctamente seleccionados el modelo de placa y el puerto de conexión correspondientes.
Al recibir el programa, la placa lo almacena en su memoria interna y comienza a ejecutar la función `loop()` de forma indefinida, realizando así las lecturas de los sensores y el envío de los datos según lo programado.
IDE cuenta con una herramienta llamada Monitor Serial, la cual permite visualizar en tiempo real la información que la placa envía a través del puerto USB.
6. 𝙎𝙚 𝙖𝙡𝙢𝙖𝙘𝙚𝙣𝙖 𝙡𝙤𝙨 𝙙𝙖𝙩𝙤𝙨 𝙢𝙚𝙙𝙞𝙖𝙣𝙩𝙚 𝙪𝙣 𝙘𝙤𝙙𝙞𝙜𝙤 𝙙𝙚 𝙋𝙮𝙩𝙝𝙤𝙣.
   El script de Python utiliza una librería de comunicación serial (como pyserial) para establecer conexión con el puerto al que está conectado el Arduino, especificando la misma velocidad de transmisión (baudrate) configurada en el código de la placa.
Una vez establecida la conexión, el programa entra en un ciclo continuo en el que permanece a la espera de que el Arduino envíe una nueva línea de datos a través del puerto serial. Cada línea recibida llega como texto plano, con los valores separados por comas (por ejemplo: temperatura, humedad y lluvia), los cuales el script separa y convierte a valores numéricos.
El programa obtiene la fecha y hora actual del sistema y la agrega junto con los valores leídos del sensor. Con esta información completa, se escribe una nueva fila al final del archivo CSV correspondiente, quedando así registrada la lectura junto con su marca de tiempo.
Este proceso se repite de manera constante mientras el Arduino continúe enviando datos, lo que permite que el archivo CSV se vaya actualizando de forma progresiva con cada nueva lectura de los sensores.
7. 𝙎𝙚 𝙘𝙧𝙚𝙖𝙣 𝙡𝙖𝙨 𝙜𝙧𝙖𝙛𝙞𝙘𝙖𝙨 𝙢𝙚𝙙𝙞𝙖𝙣𝙩𝙚 𝙪𝙣 𝙘𝙤𝙙𝙞𝙜𝙤 𝙙𝙚 𝙋𝙮𝙩𝙝𝙤𝙣.
   El script encargado de generar las gráficas lee el archivo datos_pluviometro.csv mediante la librería pandas, cargando todas las filas correspondientes (fecha y hora, temperatura, humedad y lluvia) en una tabla de datos.
Convierte la columna de fecha y hora a un formato real de fecha, contemplando los distintos formatos que pueden presentarse dentro del archivo, y ordena todas las filas de manera cronológica, con el fin de evitar inconsistencias visuales al momento de graficar.
Una vez ordenados los datos, mediante la librería Plotly se agrupan por día y por mes, generando gráficos interactivos que muestran las líneas de temperatura, humedad y lluvia, así como los promedios y valores máximos correspondientes en el caso de las gráficas mensuales.
Cada gráfica generada se guarda como un archivo HTML independiente dentro de las carpetas graficas/diario y graficas/mensual, identificado con la fecha correspondiente.
8. 𝙇𝙤𝙨 𝙙𝙖𝙩𝙤𝙨 𝙮 𝙡𝙖𝙨 𝙜𝙧𝙖𝙛𝙞𝙘𝙖𝙨 𝙨𝙤𝙣 𝙚𝙣𝙫𝙞𝙖𝙙𝙖𝙨 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙖𝙢𝙚𝙣𝙩𝙚 𝙖 𝙜𝙞𝙩𝙝𝙪𝙗.
   El proyecto se encuentra vinculado a un repositorio remoto en GitHub mediante Git, un sistema de control de versiones encargado de dar seguimiento a los cambios realizados en los archivos del proyecto.
   Mediante el Administrador de tareas de windows, se configuró un desencadenador de tipo repetitivo, establecido para ejecutarse cada treinta minutos, indicándole al sistema que realice cierta acción de manera periódica e indefinida. Dicha tarea se encuentra vinculada al programa PowerShell, al cual se le indica como argumento la ruta del script correspondiente, de forma similar a como se ejecutaba previamente de manera manual desde la terminal.
   De esta forma, cada treinta minutos el sistema operativo ejecuta dicho script en segundo plano, el cual regenera las gráficas correspondientes y realiza los comandos git add, git commit y git push, replicando el mismo proceso que se llevaría a cabo manualmente.
Como resultado, el repositorio en GitHub se mantiene actualizado de forma automática cada media hora con los datos y gráficas más recientes, sin requerir intervención manual por parte del usuario.





  
