from celery import Celery

celery_app = Celery('dragons-eggs', broker='pyamqp://guest@localhost//', backend='rpc://', include=['worker.tasks'])

if __name__ == '__main__':
    celery_app.start()