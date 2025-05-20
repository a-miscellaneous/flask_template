import multiprocessing

worker_class = "gthread"
# worker_class = "sync"
threads = 1
workers = 1
bind = "0.0.0.0:80"
timeout = 90
keepalive = 3600
preload_app = True
