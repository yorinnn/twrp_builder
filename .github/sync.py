#!python3
import os

def repo_cmd_builder(repo):
    return ["repo", "sync", repo[0], "&&", "rm", "-rf", f".repo/{repo[1]}"]