# Import Statements..
import parsl
from parsl import python_app
from parsl.monitoring import MonitoringHub
from parsl.executors.funcX import FuncXExec

import multiprocessing
import os

from parsl.providers import LocalProvider
from parsl.channels import LocalChannel
from parsl.launchers import SingleNodeLauncher

from parsl.config import Config
from parsl.executors import HighThroughputExecutor


from parsl.data_provider.http import HTTPInTaskStaging
from parsl.data_provider.ftp import FTPInTaskStaging
from parsl.data_provider.file_noop import NoOpFileStaging

import time

def fresh_config():
    return Config(
        executors=[FuncXExec(endpoint_id = 'fa11b360-9f04-4df8-903e-81fc706fd21c', max_threads = 1)],
        internal_tasks_max_threads = 1
    )

@python_app
def app_A():
    import time
    time.sleep(10)
    a = 2 * 3 + 1
    return a

@python_app
def app_B(x):
    import time
    time.sleep(10)
    b = x + 2 / 2
    return b

@python_app
def app_C(x, y):
    import time
    time.sleep(10)
    return x + y

@python_app
def app_D(a,b,c):
    import time
    time.sleep(1)
    d = a + b - c
    a = d + b
    return (a / d) + 2

@python_app
def app_E(a,b,c,d):
    import time
    time.sleep(7)
    e = a + b - c / d
    a = e * d + b
    return (a / e) + 2

@python_app
def app_F(a,b,c,d,e):
    import time
    time.sleep(3)
    return (c - b) + e * (d / a)

@python_app
def app_G():
    import time
    time.sleep(9)
    return 9 * 2

@python_app
def app_H(x):
    import time
    time.sleep(3)
    return x / 2

@python_app
def app_I(x,y):
    import time
    time.sleep(1)
    z = x * x - (3 - 4 * y)
    return (0 - z) + 2

@python_app
def app_J(x,y,z):
    import time
    time.sleep(2)
    return (x + y) * z / 2

@python_app
def app_K(a,b,c,d):
    import time
    time.sleep(3)
    e = a + b - c / d
    a = e * d + b
    return (a / e) + 2

@python_app
def app_L(a,b,c,d,e):
    import time
    time.sleep(1)
    return (c - b) + e * (d / a)

@python_app
def app_M():
    import time
    time.sleep(4)
    return 10 * 3 / 5

@python_app
def app_N(x):
    import time
    time.sleep(3)
    return x / 2

@python_app
def app_O(x,y):
    import time
    time.sleep(6)
    return x / 2 + y

@python_app
def app_P(x,y,z):
    import time
    time.sleep(2)
    return y - x + z * y / x

@python_app
def app_Q(a,b,c,d):
    import time
    time.sleep(8)
    p = a * a + b / (c - d)
    return p * p / p + p

@python_app
def app_R(a,b,c,d,e):
    import time
    time.sleep(2)
    a = a + 9
    b = a + b
    c = b + c
    d = c + d
    e = d + e
    r = e * a
    return r

@python_app
def app_S(a,b,c,d,e,f):
    import time
    time.sleep(4)
    return a - f + b * c / d + e

@python_app
def app_T(a,b,c,d,e,f,g):
    import time
    time.sleep(3)
    return a + b + c + d + e + f + g

@python_app
def app_U(a,b,c,d,e,f,g,h):
    import time
    time.sleep(6)
    return a + b - c * d / e + f - g * h

@python_app
def app_V(a,b,c,d,e,f,g,h,i):
    import time
    time.sleep(8)
    a = a * b + 1
    b = b * c + a
    c = c * d + b
    d = d * e + c
    e = e * f + d
    f = f / g + e
    g = g / h + f
    v = g + (h/f)
    return v * 8 - i

@python_app
def app_W(a,b,c,d,e,f,g,h,i,j):
    import time
    time.sleep(2)
    w = j - a + e / (c * h)
    return w / 3 + b * d - 2 + f / g * i

@python_app
def app_X(a,b,c,d,e,f,g,h,i,j,k):
    import time
    time.sleep(3)
    x = 6 * f - h / g + f
    return x * 3 + (i * j - 4 * k / (a - b + c * d / e))

@python_app
def app_Y(a,b,c,d,e,f,g,h,i,j,k,l):
    import time
    time.sleep(1)
    a = a * (c + 8 / d * l)
    b = e - a + 5 * k * (g - 7 + i * b + j / h)
    y = b * 9 / f + 1
    return 18 * y / 2

@python_app
def app_Z(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
    import time
    time.sleep(6)
    z = (a + b) - c * d + e - f + (g - h) + i / j - (k + l)
    return z * (n + r) / m + o + p - (q * t / s)

parsl.load(fresh_config())
# print(3)
# print(app_A())
# print(app_B(2).result())
x = time.time()
# print(app_C(app_A(), app_B(2)).result())
total = app_Z(app_D(app_A(),app_G(),app_M()),
                      app_E(5,10,15,20),
                      app_F(9,app_M(),app_E(19, app_N(6),24,34),45,app_B(8)),
                      app_J(app_H(app_G()),app_D(5,2,9),5),
                      app_K(52,app_A(),13,54),
                      app_L(app_N(13),22,app_H(11),27,18),
                      app_P(50,16,app_M()),
                      app_Q(14,23,20,45),
                      app_R(48,20,30,app_O(21,38),23),
                      app_S(app_I(47,7),29,48,3,5,24),
                      app_T(4,11,46,36,48,38,6),
                      app_U(25,29,36,12,7,14,10,50),
                      app_V(44,30,35,10,app_Q(34,8,12,49),7,15,21,47),
                      app_W(49,31,app_I(9,7),20,32,29,23,15,27,1),
                      app_X(41,20,app_B(44),21,48,45,41,20,app_C(24,33),7,36),
                      app_Y(0,31,5,app_N(40),46,40,22,1,16,32,12,42),
                      app_A(),
                      app_B(28),
                      app_C(45, app_B(app_P(42,37,app_M()))),
                      app_M()).result()
print(total)
print(time.time() - x)