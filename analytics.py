import math
from statistics import NormalDist


def option_price(spot, strike, days, volatility, rate, option_type):
    if spot <= 0 or strike <= 0 or days <= 0 or volatility <= 0 or option_type not in ('call', 'put'):
        raise ValueError('价格、剩余天数、波动率必须为正数。')
    t, v, r = days / 365, volatility / 100, rate / 100
    normal = NormalDist()
    d1 = (math.log(spot / strike) + (r + v*v/2)*t) / (v*math.sqrt(t))
    d2 = d1 - v*math.sqrt(t)
    n1, n2 = normal.cdf(d1), normal.cdf(d2)
    density = math.exp(-d1*d1/2) / math.sqrt(2*math.pi)
    discount = math.exp(-r*t)
    gamma = density / (spot*v*math.sqrt(t))
    vega = spot*density*math.sqrt(t) / 100
    common_theta = -spot*density*v/(2*math.sqrt(t))
    if option_type == 'call':
        price = spot*n1 - strike*discount*n2
        delta = n1
        theta = (common_theta - r*strike*discount*n2) / 365
        rho = strike*t*discount*n2 / 100
    else:
        price = strike*discount*normal.cdf(-d2) - spot*normal.cdf(-d1)
        delta = n1 - 1
        theta = (common_theta + r*strike*discount*normal.cdf(-d2)) / 365
        rho = -strike*t*discount*normal.cdf(-d2) / 100
    return {key: round(value, 6) for key, value in {'price': price, 'delta': delta, 'gamma': gamma, 'theta': theta, 'vega': vega, 'rho': rho}.items()}
