# guava-mvp

1) Pull Repo

2) pip install -r requirements.txt

3) start app by running python run.py

Add the following to your `~/.gitconfig`:

    [push]
        default = simple
    [pull]
        default = simple
    [alias]
        up = !git pull --rebase=preserve origin \"$(git rev-parse --abbrev-ref HEAD)\"


The alias up is meant to be used when you want to update your local repo with the remote repo. Use it like this: git up

Read up on git rebase 
