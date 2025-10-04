from celery import shared_task

@shared_task
def my_blog_task():
    print("This is a task from the blog app.")