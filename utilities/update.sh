#!/bin/bash

if [ ! -d "ESMValTool" ]
then
  git clone git@github.com:ESMValGroup/ESMValTool.git --branch v2.8.0
fi
rm ../.github/workflows/recipe*.yml
python generate.py

