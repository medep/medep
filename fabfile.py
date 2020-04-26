from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.utils import puts

base_path = os.path.abspath(os.path.dirname(__file__))

env.forward_agent = True
env.user = 'ubuntu'
env.key_filename = os.path.join(base_path, 'keys/medep_rsa')
env.host_string = 'medep.org:22'

@task
def deploy():
    with cd('/home/ubuntu/mpg/'):
        puts(magenta("[Pulling master]"))
        run('git pull origin master')

        puts(magenta("[Updating containers]"))
        run('docker-compose -f docker-compose.production.yml up -d --build')
        run('yes | docker system prune -a')



