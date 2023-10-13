#!/bin/sh

#SBATCH -J senpred.sh
#SBATCH -p titanxp
#SBATCH --gres=gpu:2
#SBATCH -o output2.out

srun python3 train.py