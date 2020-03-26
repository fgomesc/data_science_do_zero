from matplotlib import pyplot as plt


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_saquared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y, in zip(variance, bias_saquared)]
xs = [i for i, _ in enumerate(variance)]

# podemos fazer multiplas chamadas para o plt.plot
# pa mostrar multiplas series no mesmo grafico
plt.plot(xs, variance, 'g-', label='variance') # linha verde solida
plt.plot(xs, bias_saquared, 'r-', label='biasˆ2') # linha com linha de ponto tracejado vermelho
plt.plot(xs, total_error, 'b:', label='total error') # linha com pontilhado azul

# porque atribuimos rotulos para cada serie
#podemos obter uma legenda gratuita
# loc=9 significa "top center"
plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.title("Compromisso entre polarização e variancia")
plt.show()
