from fabric.api import env, run

env.hosts = ['example.com']
env.user = 'deploy'
env.key_filename = '~/.ssh/id_rsa'

def deploy():
    with cd('/var/www/myapp'):
        run('git pull')
        run('pip install -r requirements.txt')
        run('python manage.py migrate')
        run('sudo service apache2 restart')