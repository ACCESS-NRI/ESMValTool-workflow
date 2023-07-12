#!/bin/bash

if [ ! -d "ESMValTool" ]
then
  git clone git@github.com:ESMValGroup/ESMValTool.git
fi
rm ../.github/workflows/recipe*.yml
python generate.py

