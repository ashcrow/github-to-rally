import unittest


with open('bin/github-to-rally') as code_file:
    exec(code_file.read())


class TestCase(unittest.TestCase):
    pass
