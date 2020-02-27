#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:14:06 2020

@author: nitish.singidi
"""

from pydriller import RepositoryMining,GitRepository

git = GitRepository("pythontestsamples")

for commit in RepositoryMining("/Users/nitish.singidi/Desktop/gitcheck").traverse_commits():
    for files in commit.modifications:
        dataset = files.
        print(dataset)
        
        
        