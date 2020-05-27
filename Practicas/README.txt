Hola buenas,

soy David Fontela moñino y aquí explico brevemente como he implementado mi práctica 2.

NOTA: La semilla de LCM la he dejado fija porque me gustó el mapa que salió, aún así he dejado una línea comentada dentro de LCM que genera una semilla
a partir de la fecha y hora actuales, este método lo use para comprobar que funcionaba el algoritmo.

1º Mediante unas parámetros al principio del script, genero un array bidimensional que representará al mapa de mi juego
	- 0 donde haya una pared.
	- 1 donde haya un suelo.
   Se inicializa a todo suelo.

2º Llamamos a randomWalk(), donde necesita el ancho y alto de la pantalla, el número de túneles y su tamaño máximo y el mapa en sí.
	- Elige aleatoriamente donde comenzar, la que será la posición de nuestro personaje y la almacena y comienza el algoritmo.

	- Ahora para cada túnel, elegirá una dirección aleatoria y un tamaño aleatorio pero tendremos en cuenta la última elegida para no volver hacia detrás.
	  También se tiene en cuenta si anteriormente ha chocado contra una pared para no elegir la dirección que le sacaría del mapa.

	- Cuando elige esta dirección, sabiendo ya el tamaño, comprueba si se saldría del mapa al pintarlo, si es así pinta el túnel hasta el límite del mapa
	  y pasa a generar el túnel siguiente con las condiciones ya dichas.

3º Cuando terminamos de generar el mapa, falta pintarlo y generar el juego, esto lo hace la función printMap()
	- Crea la ventana del juego y carga los diferentes assets.

	- Recorremos el mapa completo:
		- Si hay que pintar un suelo, elige aleatoriamente si es un enemigo, una recompensa o que tipo de suelo, teniendo en cuenta las densidades
		  de los parámetros iniciales.
		- Si hay que pintar una pared, elige aleatoriamente que tipo de pared, teniendo en cuenta las densidades de los parámetros iniciales.
	
	- Finalmente pinta al personaje en la posición guardada anteriormente.

Los sprites se han conseguido de la siguiente página web (ya que mis dotes artísticas no son muy elevadas): https://www.spriters-resource.com/game_boy_gbc/pokemoncrystal/
