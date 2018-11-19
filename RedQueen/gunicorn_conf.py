import multiprocessing

bind = 'unix:/home/cloudsen/work/deploy/webservers/sockets/nginx-gunicorn.sock'
#bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
errorlog = '/home/cloudsen/work/deploy/webservers/gunicorn/guicorn.error.log'
accesslog = '/home/cloudsen/work/deploy/webservers/gunicorn/gunicorn.access.log'
proc_name = 'gunicorn_myblog'