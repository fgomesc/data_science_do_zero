import math
import random
from modulos.cap_4_probabilidade.distribuicao import inverse_normal_cdf
from modulos.cap_4_probabilidade.plot_2 import normal_cdf


def normal_approximation_to_binomial(n, p):
    """ encontre mi e sigma correspondendo ao Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# o cdf normal é a probabilidade que a variavel esteja abaixo de um limite
normal_probability_below = normal_cdf

# esta acima do limite se nao estiver abaixo
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# esta entre se for menos do que hi, mas nao menor do que lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# esta fora se nao estiver entre
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """ retornar z para que p(z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """ retorna z para que p(z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """ retorna os limites simetricos (sobre a media)
    que contem a probabilidade especifica"""
    tail_probability = (1 - probability) / 2

    #limite superior deveria ter tail_probability acima
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # limite inferior deveria ter tail_probability abaixo
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# 95% dos limites baseados na premissa p é 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# mi e sigma reais baseados em p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# um erro tipo 2 significa que falhamos ao rejeitar a hipotese numa
# que acontecera quando x ainda estiver em nosso intervalo original
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability



hi = normal_upper_bound(0.95, mu_0, sigma_0)
# é 526 (< 531 ja que precisamos de mais probabilidade na aba superior


type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power2 = 1 - type_2_probability



def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # se x for maior do que a media, a coroa sera o que for maior do que x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # se x for menor do que a media, a coroa sera o que for menor do que x
        return 2 * normal_probability_below (x, mu, sigma)



extreme_value_count = 0
for _ in range(1000000):
    num_heads = sum(1  if random.random() < 0.5 else 0          # contagem do # de caras
                    for _ in range(1000))                       # em 1000 lançamentos

    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1



two_sided_p_value(531.5, mu_0, sigma_0)

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

upper_p_value(526.5, mu_0,sigma_0)


p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

normal_two_sided_bounds(0.95, mu, sigma)

def run_experiment():
    """ Lanca uma moeda 1000 vezes, true = cara, false = coroa"""
    return[random.random() < 0.5 for _ in range(1000)]

def reject_fairnesse(experiment):
    """ usando 5% dos niveis de significancia"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiments
                      for experiment in experiments
                      if reject_fairnesse(experiment)])

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 150)

print(two_sided_p_value(z))


def B(alpha, beta):
    """ uma constante normalizada para que a probabilidade total seja 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:      # sem peso fora de [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)

