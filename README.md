# Practica 7.04

| Autor                          | Asignatura                     | Curso  |
|--------------------------------|--------------------------------|--------|
| Iván Dimitri Novomiast Dieguez | Sistemas Operativos Monopuesto | 1SMR-B |
<hr>
All Rights Reserved to: ©INovomiast 2023
<br>
<br>

## Bienvenida
Buenos días, tardes, noches, bienvenid@ al repositorio de la tarea 7.04 de el Tema 6 de Sistemas Operativos Monopuesto del Curso 1SMR-B de el Instituto IESFuengirola1.

En este documento, se te guiara en el funcionamiento del Script escrito en python el cual automatiza los comandos:
  * MKDIR
  * TOUCH
  * MV
  * CP

Todo esto para realizar el siguiente diagrama de Directorios y Archivos:

![imagen](https://user-images.githubusercontent.com/116105316/219830252-480c07b2-80fa-4d24-940c-1c7deff004da.png)

Así que sin dar más vueltas comencemos a explicar como es este script!!

## El Script en Accion:

Para poder usarlo deberemos cumplir los siguientes requisitos:
  * Maquina: Windows o Ubuntu (Recomiendo una maquina basada en Linux para el funcionamiento completo).
  * Git: Para clonar el codigo y poder usarlo.

Cumpliendo estas __2__ solicitudes, entendamos como descargarlo y usarlo:

1. Clonar el Repositorio:
Y es que es tan sencillo como tener la herramienta GIT instalada en tu maquina y poner el siguiente comando en tú consola
~~~sh
  git clone https://github.com/INovomiast-IESFuengirola1/Practica7.07.git
~~~

2. Navegar hasta este, donde lo hayas dejado:
Cuando se te clone el REPOSITORIO, el cual lo hará en el mismo directorio en el cual hayas estado a la hora de poner el comando, así que ahora solo
tendremos que navegar hasta el directorio de el REPOSITORIO:

~~~sh
 cd /home/usuario/Escritorio/"Practica 7.07"
~~~

3. Ahora usando el comando posteriormente dicho, solo quedará navegar hasta la carpeta "src" y ejecutar el archivo .py

~~~sh
 cd /home/usuario/Escritorio/"Practica 7.07"/src/
 python3 main.py
~~~

4. Ya estamos en el programa, ahora nos pedira unos datos que necesitará para hacer su magia:
![imagen](https://user-images.githubusercontent.com/116105316/219830795-7f451ca3-9735-4e85-b32f-6602da2c9597.png)

Como primer paso insertaremos el nombre del Directorio Base (En mi caso siendo Practica (Sin acento por el Case Sensitive))

5. Ahora nos pedirá cuantos subdirectorios querremos crear adentro del Directorio Base (En mi caso son 3: Informes, Otros y Proyectos)

![imagen](https://user-images.githubusercontent.com/116105316/219830852-36a03d6e-c940-43f9-a064-625cfdfe0e1e.png)

Aquí solo hay que indicarle un numero entero.

6. Insertar los nombres de los subdirectorios (Irá uno por uno preguntandote como los va a llamar)
![imagen](https://user-images.githubusercontent.com/116105316/219830896-26798be3-485c-4f3a-9691-f62b7d1019a5.png)

Hemos creado los 3 que nos aparecen en el diagrama... El Script los creará automaticamente en la carpeta donde está el proyecto.

7. El proximo paso es crear los subdirectorios en la carpeta Informes, el script ahora te preguntará si quieres crear subdirectorios adentro de las carpetas

![imagen](https://user-images.githubusercontent.com/116105316/219831403-3bbbbf94-8ee6-4a4e-9d66-b859e9dd1105.png)

8. Pasaremos por el mismo proceso que antes donde se nos pedira la cantidad y los nombres de dichas subcarpetas
![imagen](https://user-images.githubusercontent.com/116105316/219832114-acbd6a97-ec68-4176-8628-77f1db3ec8da.png)

9. Casi llegando al final estamos, donde ahora te preguntara donde quieres mover las carpetas creadas, recordemos
que disponemos de 3 directorios creados anteriormente, así que nos dará a elegir entre ellos 3:

![imagen](https://user-images.githubusercontent.com/116105316/219832617-14bdbeda-32ff-4398-bf8f-72cf76275389.png)

Más abajo, donde explico el codigo te aclaro el porque, pero ciñete a los numeros que hay en la izquierda entre unos []
Del 0 al 2 tendras que darle un valor, y automaticamente el script te los moverá al directorio deseado, en este caso siendo
informes que tiene el numero 0.

![imagen](https://user-images.githubusercontent.com/116105316/219833140-4361bb86-d8c5-46b0-9cab-12573412d6db.png)

Como podeis ver, me ha generado los directorios y archivos necesarios, y me los ha colocado donde debia.
Todo esto recordad que os lo explico en el apartado de **Como funciona el Script**.

Una vez finalizado el proceso podreis ver el resultado en la Carpeta src/Practica

<hr>

Con estos sencillos pasos hemos podido completar la tarea sin uso de un comando escrito por nosotros, sino por una atomatización.

## Como funciona el Script

Vamos a dar un paseo juntos por las lineas que conforman a este script!!

Lo primero es entender la estructura de la como inicia este:

~~~python
 #Execute the script if condition is true
 if __name__ == "__main__":
    tool()
"""
 Estas 2 lineas de aquí son las que comienzan cada script de pythhon, son las que condicionan que la herreamienta se pueda ejecutar sin problema
 alguno.
"""
~~~

Como habreis visto, al cumplirse esta condicion invocamos a la función tools(), la cual inicia la Herramienta, basada en CLI.


La función tools() comienza de la siguiente manera:

~~~python
 root_folder_name = input("Insert the *Root* Folder Name: ")
 
 conf.create_starter_config()
 conf.config['DEFAULTS']['root_folder_name'] = root_folder_name
 conf.config[''][''] = platform.system()
 conf.config[''][''] = os.getlogin()
 
 with open('config.ini', 'w') as configfile:
   conf.config.write(configfile)
   configfile.close()
~~~

Está seccion es la de creación de la base, donde nos da un input() y lo guarda en una variable, la cual después sera muy solicitada a lo largo del codigo
así que, forma una buena amistad con ella, para así, no pillarle asco al final.


~~~python
 #Step 2: Take the quantity of child_folders to create:
    child_folder_q = input("Quantity of Child Folders to Create: ")

    #Step 3: For Loop to cycle for creating the folders (Taking the names and appending to list):
    for x in range(int(child_folder_q)):
        inp_fold_name = input("Insert the Child Folder " + str(x) + " Name: ")
        child_folder_names.append(inp_fold_name)

    #print(child_folder_names) //debuggin: Show list to see if appended correctly.

    #Step 4: Array Separation and Folder Creation:
    def create():
        print("Creating Root Dir: <==========> 100%")
        os.mkdir("./" + root_folder_name)
        time.sleep(0.5)
        print('\n')
        print("Creating Subdirs:")
        for x in child_folder_names:
            print(x + '\n') #//Debuggin: Show if values sepparated correcly.
            os.mkdir(os.getcwd() + "/" + root_folder_name + "/" + x)
            
    create()
~~~

Con estas lineas del codigo lo que podemos ver es que usamos un Array con ciertos valores los cuales hemos extraido al preguntar
los nombres de las carpetas que queriamos crear, estas ahora almacenadas en un Array en una variable, pueden ser sometidas a un
bucle for para separarlas de la lista y trabajar individualmente con ellas.

En este caso el valor de x en child_folder_names es el que le dice al modulo ~~~ os.mkdir() ~~~ como llamar a cada directorio.

Otra cosa notable es que nosotros para el mkdir estamos usando una concatenacion la cual es:

1. os.getcwd() // Funcion la cual nos ayuda a conseguir el directorio el cual actualmente se esta usando (Así hay compatibilidad)
2. "/" // Esto es para separar directorios
3. root_folder_name // Esta es la variable que habiamos declarado al principio, ahora consigue los datos de esta.
4. "/" // Esto es para separar directorios
5. x // Variable x del bucle por la lista child_folder_names

El bucle nos separará la lista en strings individuales y la función os.mkdir() nos creará el numero de directorios = n. Valores * lista


Ahora hablemos sobre el tinglado que llevará crear 2 subdirectorios más y que el script localize todo y sepa donde ponerlo:

Actualmente la pieza de codigo es:

~~~python
  #Function to run if opt is y:
    def c_subdir():
        
        #We are going to repeat the process but this time creating the subdirectories:
        sub_folder_q = input("Insert the quantity of SubDirectories to create: ")

        #Loop from Variable Value to determine the Folder Names to be created.
        for y in range(int(sub_folder_q)):
            sub_folder_inp = input("Insert the Subdirectory " + str(y) + " Name: ")
            sub_folder_names.append(sub_folder_inp) #With this we append the Val. of de Var. to the list.

        #Now we take all the folders on the root directory:
        rdir = os.listdir(os.getcwd() + "/" + root_folder_name + "/")
        
        #Step 6: Ask for the Directory Name where we create the subdirectries:
        
        for u in rdir: #We loop thru all the values in rdir (DIRECTORY)
            print("[" + str(rdir.index(u)) + "]" + u) #And we show the Index Number of Val in Array

        sub_dir_name = input("Insert the number of the Directory where you wan't to create this subdirs: ")
        
        #We are trying to use the List index to tell the Script were to create the subdirectory's
        # for o in rdir:
        #     if sub_dir_name == range(int(rdir.index(o))):
        #         print("Directory is avaliable")

        #Step 7: Take the Sub_Dir_Name and create a conditional 
        for o in rdir:

            index_num = rdir.index(o)

            if sub_dir_name in str(index_num):
                for k in sub_folder_names:
                    print('\n')
                    print("Creating Subdirectories: " + k + "...")
                    time.sleep(2)
                    os.mkdir(path=os.getcwd() + "/" + root_folder_name + "/" + rdir[int(sub_dir_name)] + "/marzo")
                    os.mkdir(path=os.getcwd() + "/" + root_folder_name + "/" + rdir[int(sub_dir_name)] + "/abril")
                    if os.path.exists(os.getcwd() + "/" + root_folder_name + "/Informes/" + k):
                        create_files()
                        break
            else:
                print("There was an Error while doing this!!")
                

    #Now we ask if we want to create subdirs
    option_sub = input("You wan't to create Subdirectories? [y/n]: ")

    if option_sub == "y":
        c_subdir()
    elif option_sub == "n":
        exit()

~~~

Misma logica que casi todo el script, pero este lo que más se complica es que a la hora de crearlos, tenemos que seleccionar una carpeta de las 3 ya creadas para que dichas subcarpetas se puedan alojar adentro.

Aquí lo que hacemos es dividir la lista en indices, donde cada valor esta asignado a un numero en la lista, este tenemos que extraerlo para después hacer 2 comprobaciones:
1. Ver que esté en la lista y no sea una opcion inexistente.
2. Alojar los subdirectorios dependiendo de cual sea el indice para asignarlo a un valor y poder usarlo.

En este caso lo que hacemos es hacer un bucle por la lista para que nos arroje todos los valores por STRINGS individuales y después de esta lista pedimos los indices que van asignados a dicho valor.

Para después comprobar que el valor proporcionado por el usuario sea el mismo que el indice del valor de la lista.


Ahora lo que tenemos que hacer es crear las carpetas en el directorio asignado, pero ahora el ordenador lo que tiene son valores de una lista sin mero sentido, pero una vez son reasignadas despues de comprobar, pues permiten a la herramienta decir que valor tiene ese indice y sumarlo al directorio en el cual se crearan las carpetas.

~~~python
  #Function to create the assigned files in the assigned directories. (READ THE DOCS!!)
    def create_files():
        #Files on a JSON type variable
        march = ['marzo.ic', 'marzo.iv']
        april = ['abril.ic', 'abril.iv']
        proyects = ['1.p', '2.p', '3.p', '4.p', '5.p']

        #Marzo:
        for m in march:
            print("Creating files " + m + " in " + os.getcwd() + "/Informes/Marzo")
            if platform.system() == "Windows":
                os.system('type nul > ./' + root_folder_name + "/Informes/Marzo/" + march[0])
                os.system('type nul > ./' + root_folder_name + "/Informes/Marzo/" + march[1])
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Informes/Marzo/" + m)
                time.sleep(3)
                break
            break
        time.sleep(1)
        #Abril
        for a in april:
            print("Creating files " + a + " in " + os.getcwd() + "/Informes/Abril")
            if platform.system() == "Windows":
                os.system('type nul > ' + './' + root_folder_name + "\\Informes\\Abril/" + a)
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Informes/Abril/" + a)
                time.sleep(3)
                break
            break
        time.sleep(1)
        #Proyectos
        for p in proyects:
            print("Creating files " + p + " in " + os.getcwd() + "/Proyectos/")
            if platform.system() == "Windows":
                os.system('type nul > ' + './' + root_folder_name + "\\Proyectos/" + p)
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Proyectos" + p)
                time.sleep(3)
                break
            break
~~~

Bien, una vez tenemos los directorios ya creados ahora toca crear archivos que vayan alojados en esto, para eso usaremos os.system, para ejecutar comandos desde el script, en este caso lo hemos intentado aplicar de forma multiplataforma asi que disponemos:
* Variante Windows: Comando: type nul > nombre_archivo.formato
* Variante Linux: Comando: touch directorio_completo/nombre_archivo.formato
Con esto el script ya sabrá que y donde poner todo.

## LLegamos a un final

Como todo lo bueno, no es infinito, aquí es donde termina esta breve explicación de el script y el codigo..

Soy Iván y me despido hasta una futura practica.

<hr>

<p align="center">
  El script cabe una gran posibilidad de que no rinda al 100% por errores que estoy arreglando!
  
  He usado: 0 comandos, 512 Lineas de Codigo y Texto en total y 5 horas de trabajo han sido requeridas para completar esto!.
</p>

### Propuesta de Corrección de la tarea:
 Entrega de la nota mediante la edición de este archivo: https://github.com/INovomiast-IESFuengirola1/Practica7.07/blob/main/correccion/c.ini
 
 Editar dicho archivo en las lineas con un comentario empezado por #
