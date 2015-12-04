'''
Day 6 - 编写配置文件

把config_default.py作为开发环境的标准配置，把config_override.py作为生产环境的标准配置，我们就可以既方便地在本地开发，又可以随时把应用部署到服务器上。

应用程序读取配置文件需要优先从config_override.py读取。

为了简化读取配置文件，可以把所有配置读取到统一的config.py中：
'''
import config_default

configs = config_default.configs

try:
    import config_override
except ImportError:
    pass
