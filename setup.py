from distutils.core import setup
setup(
    name = "Slowloris",
    py_modules = ["slowloris"],
    entry_points = {"console_scripts": ["slowloris=slowloris:main"]},
    version = "0.1.3",
    description = "Slowloris rewrite in Python. With SOCKS support",
    author = "Gokberk Yaltirakli",
    author_email = "webdosusb@gmail.com",
    url = "https://github.com/wckd/slowloris",
    keywords = ["dos", "http", "slowloris"],
    install_requires=["PySocks"]
)
