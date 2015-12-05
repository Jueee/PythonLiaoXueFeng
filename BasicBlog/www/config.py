'''
Day 6 - 编写配置文件

把config_default.py作为开发环境的标准配置，把config_override.py作为生产环境的标准配置，我们就可以既方便地在本地开发，又可以随时把应用部署到服务器上。

应用程序读取配置文件需要优先从config_override.py读取。

为了简化读取配置文件，可以把所有配置读取到统一的config.py中：
'''
import config_default

class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k,v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attributr '%s'" % key)
        
    def __setattr__(self, key ,value):
        self[key] = value
        

def merge(defaults, override):
    r = {}
    for k,v in defaults.items():
        if k in override:
            if isinstance(v,dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)

