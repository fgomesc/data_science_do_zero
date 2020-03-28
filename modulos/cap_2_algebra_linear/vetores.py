from functools import reduce
import math




height_weight_age = [70,   #polegadas,
                     170,  #quilos,
                     40]   #anos


grades = [95, # teste 1
          80, # teste 2
          75, # teste 3
          62] # teste 4

def vector_add(v, w):
    """ Soma elementos correspondentes"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """ Subtrai elementos correspondentes """
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

"""
def vector_sum(vectors):
    # Soma toda os elemntos correspondentes 
    result = vectors[0]                         # começa com o primeiro vetor
    for vector in vectors[1:]:                  # depois passa por todos os outros
        result = vector_add(result, vector)     # e os adiciona ao resultado
    return result

"""
# forma reduzida da função acima

def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """ C é um número, v é um vetor """
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """ Computar o vetor cujo i-ésimo elemnto seja a media dos
    i-ésimos elementos dos vetores inclusos"""
    n = len(vectors)
    return scalar_miltiply(1/n, vector_sum(vectors))

def dot(v, w):
    """ v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))


def sum_of_quares(v):
    """ v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_quares(v))  # math.sqrt é a função da raiz quadrada


def squared_distance(v, w):
    """ v_1 - w_1 ** 2 + ... (n_n - w_n) ** 2 """
    return sum_of_quares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(squared_distance(v, w))

