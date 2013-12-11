from lettuce import *


with open('bin/github-to-rally') as code_file:
    exec(code_file.read())


@step('I have the user (\w+)')
def have_the_user(step, user):
    world.user = str(user)


@step('I have the repo (.*)')
def have_the_repo(step, repo):
    world.repo = repo


@step('I look up to (\d+) days back')
def look_back(step, days):
    world.days = int(days)


@step('I execute the Github export')
def exeucte_github_export(step):
    world.result = export_from_github(world.user, world.repo, world.days)


@step('I get a list of results')
def check_is_list(step):
    assert type(world.result) == list
