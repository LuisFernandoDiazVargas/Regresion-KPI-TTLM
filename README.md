Regresión KPI TTLM

En el presente trabajo se busca encontrar el impacto que tienen las horas de atención promedio (TTLM) de envíos con levante parcial en las horas TTLM promedio del total de envíos que pasan por canal rojo y tienen levante.
La finalidad es establecer una serie de medidas para reducir el indicador KPI TTLM de la división de Envíos Postales. Se tiene como hipótesis que los envíos con levante parcial al ser tramitados obligatoriamente por el consginatario a través Mesa de Partes virtual dilatan el TTLM total.
En el presente trabajo se busca medir ese impacto a través de un modelo de regresión simple debido a la naturaleza de la obtencion del TTLM total (Los envíos con levante parcial son parte del calculo del promedio de TTLM total, sin embargo se desconoce la cantidad total de envíos). Para ello se hace uso de librerías como scikit-learn y statsmodels
