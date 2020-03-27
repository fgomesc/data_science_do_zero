import math
import random

# distribuição contínuas

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0


# distribuição cumulativa

def uniform_cdf(x):
    """ retorna a probabilidade de uma variavél aleatoria uniforme ser <=x"""
    if x < 0:
        return 0       # a aleatoria uniforme numa é menor do que 0
    elif x < 1:
        return 1     # por exemplo p(x <= 0.4) = 0.4
    else:
        return 1            # a aleatoria uniforme sempre é menor do que 1


# distribuição normal

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """ encontra o inverso mais proximo usando binario"""

    # se nao for, computa o padrao e redimensiona
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0     # normal_cdf(-10) esta (muito perto de) 0
    hi_z, hi_p = 10.0, 1        # normal_cdf(10) esta (muito perto de) 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2      # considera o ponto do meio e o valor da
        mid_p = normal_pdf(mid_z)       # funcao de distribuicao cumulativa la

        if mid_p < p:
            # o ponto do meio ainda esta abaixo, proca acima
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # o ponto do meio ainda esta alto, procura abaixo
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

