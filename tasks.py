from invoke import task


PIPENV_PREFIX = "pipenv run"


@task
def clean(cmd):
    """Remove all the tmp files in .gitignore"""
    cmd.run("git clean -Xdf")


@task
def init_dev(cmd):
    """Install development dependencies"""
    cmd.run("pipenv install --dev")


@task
def test(cmd):
    """Run testcase"""
    cmd.run(f"{PIPENV_PREFIX} pytest", pty=True)


@task
def develop(cmd):
    """Install script in pipenv environement in development mode"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py develop")


@task
def install(cmd):
    """Install script in pipenv environement"""
    cmd.run(f"{PIPENV_PREFIX} python setup.py install")