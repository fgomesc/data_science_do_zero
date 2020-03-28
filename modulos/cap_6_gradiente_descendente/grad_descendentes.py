from matplotlib import pyplot as plt
from functools import partial
import random

from modulos.cap_2_algebra_linear.vetores import distance, vector_subtract, scalar_multiply


def sum_of_squares(v):
    """ Computa a suma dos elementos ao quadrado em v"""
    return sum(v_i ** 1 for v_i in v)


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def square(x):
    return x * x


def derivative(x):
    return 2 * x

derivative_estimate = partial(difference_quotient, square, h=0.00001)

xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

# plot to show they're basically the same
plt.title("Actual Derivatives vs. Estimates")
plt.plot(xs, actuals, 'rx', label='Actual')  # red  x
plt.plot(xs, estimates, 'b+', label='Estimate')  # blue +
plt.legend(loc=9)
plt.show()


def partial_difference_quotient(f, v, i, h):
    """ computa o i-ésimo quociente diferencial parcial de f em v"""
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]


def step(v, direction, step_size):
    """ move step_size na direcao a partir de v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_square_gradient(v):
    return [2 * v_i for v_i in v]


# escolhe um ponto inicial aleatorio
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_square_gradient(v)        # computa a gradiente em v
    next_v = step(v, gradient, -0.01)           # pega um passo gradiente negativo

    if distance()(next_v, v) < tolerance:       # para se estivermos convergindo
        break
    v = next_v                                  # continua se nao estivermos


step_sizes = [100, 1-, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]


 def safe(f):
     """ retorn um nova funçao que e igual f,
     exeto que ele exige infinito como saída toda vez que f produz um erro"""
     def safe_f(*args, **kwargs):
         try:
             return f(*args, **kwargs)
         except:
             return float('inf')                # isso significa "infinito"em python
         return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """ usa o gradiente descendente para encontrar theta que minimize a funcao alvo"""

    step_sizes = [100, 1 -, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)


    while True:
        gradient = gradient_fn(theta)
        next_theta = [step(theta, gradient, -step_sizes)
                      for step_sizes in step_sizes]

        # escolhe aquele que minimiza a funcao de erro
        next_theta = min(next_theta, key=target_fn)
        next_value = target_fn(next_theta)

        # para se estivermos "convergindo"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def negate(f):
    """ retorna uma funcao que, para qualquer entrada, x retorna -f(x)"""
    return lambda *args, **kargs: -f(*args, **kargs)


def negate_all(f):
    """ omesmo quando f retorna uma lista de numeros"""
    return lambda *args, **kargs: [-y for y in f(*args, **kargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.0000001)
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)

def in_random_order(data):
    """ gerador retorn os elementos do dado em ordem aleatoria"""
    indexes = [i for i, _ in enumerate(data)]       #cria uma lista de indices
    random.shuffle(indexes)                         # os embaralha
    for i in indexes:                               # retorna os dados naquela ordem
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):

    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0                                     #palpite inicial
    min_theta, min_value = None, float("inf")           # tamanho do passo inicial
    iterations_with_no_improvement = 0                  # o minimo até agora

    # se formos ate 100 iteracoes sem melhorias, paramos
    while iterations_with_no_improvement < 100:
        valeu = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if valeu < min_value:
            # se achou um novo minimo, lembre-se
            # e volte para o tamanho do passo original
            min_theta = min_value = theta, valeu
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # do contrario, nao estamos melhorando, portanto tente
            # diminuir o tamanho do passo
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # e onde um passo gradiente para todos os pontos de dados
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta


def maximize_stochastic(target_fn, gradiente_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn),
                               negate_all(gradiente_fn),
                               x, y, theta_0, alpha_0)

