#Las horas TTLM es un indicador KPI que utiliza la división de envíos postales de la SUNAT para medir las horas promedio
#de atencion de un envío desde su fecha de llegada al Depósito Temporal de Serpost hasta la fecha de levante.

#Lo que se quiere es gestionar la reducción de las horas promedio TTLM reduciendo las horas promedio TTLM de las mercancías
#a las que se les da un levante parcial.

#H0: Los envíos que tienen un levante parcial afectan significativamente al TTLM total
#H1: Los envíos que tienen un levante parcial no afectan significativamente al TTLM total.

import pandas as pd
import matplotlib.pyplot as plt
import sklearn as skl
import numpy as np
import seaborn as sns

df=pd.read_excel("C:/Users/asus/Desktop/TTLM.xlsx")
print(df)

#######################################################################################################################
############################################## EXAMINANDO LOS DATOS ###################################################
#######################################################################################################################

#Grafico 1: Evolución diaría de ambos TTLM'S
plt.subplot(2,1,1)
plt.plot(df["DIA"], df["TTLM_TOTAL"], label="TTLM_TOTAL")
plt.plot(df["DIA"], df["TTLM_PARCIAL"], label="TTLM_PARCIAL")
plt.xlabel("DIA")
plt.ylabel("TTLMS")
plt.title("Gráfico de evolución")

#Grafico 2: Grafico de dispersión
plt.subplot(2,1,2)
y=np.array(df["TTLM_TOTAL"])
x=np.array(df["TTLM_PARCIAL"])

m, b = np.polyfit(x, y, 1)

plt.scatter(x, y)
plt.plot(x, m*x + b, color='red')
plt.xlabel("TTLM PARCIAL")
plt.ylabel("TTLM TOTAL")
plt.title("Gráfico de dispersión")

# Muestra el gráfico
plt.tight_layout()
plt.show()


########################################################################################################################
################################################ Regresión Lineal ######################################################
########################################################################################################################

#USANDO SKLEARN
from sklearn.linear_model import LinearRegression

Modelo=LinearRegression()
Modelo.fit(df["TTLM_PARCIAL"].values.reshape(-1,1), df["TTLM_TOTAL"])
print('Coeficiente:', Modelo.coef_)
print('Intercepto:', Modelo.intercept_)

#R cuadrado
r2 = Modelo.score(df["TTLM_PARCIAL"].values.reshape(-1,1), df["TTLM_TOTAL"])
print('R cuadrado:', r2)
#Hemos obtenido un R cuadrado de 2.3% lo que indica una correlación muy debil.


#Error caudratico medio
from sklearn.metrics import mean_squared_error
y_pred = Modelo.predict(df["TTLM_PARCIAL"].values.reshape(-1,1))
mse = mean_squared_error(df["TTLM_TOTAL"], y_pred)
rmse = mse ** 0.5
print('Raíz de errores cuadráticos medios:', rmse)

#USANDO STATSMODELS
import statsmodels.api as sm

# Ajustar modelo de regresión lineal usando statsmodels
X = df[['TTLM_PARCIAL']]
y = df['TTLM_TOTAL']
X = sm.add_constant(X)
modelo = sm.OLS(y, X).fit()

# Imprimir resumen de la regresión
print(modelo.summary())

########################################################################################################################
###################################################### Conclusión ######################################################
########################################################################################################################

print("En conclusión tenemos que los envíos con levante parcial tienen poca significancia en el TTLM total, y puede",
      "deberse a su baja cantidad, por lo que la reducción del indicador TTLM total debe gestionarse por otro tipo de variables.")





