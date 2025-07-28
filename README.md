\# Molecule Info Fetcher

This Python script takes the name of a molecule and fetches its SMILES
and IUPAC name using the \`cirpy\` library. It also generates a 2D
molecular structure using RDKit and displays the image.

\## Requirements

\- Python 3.12 - RDKit - cirpy - PIL or any image viewer that works with
\`img.show()\`

This project uses a Conda environment. To set it up:

\`\`\`bash conda create -n molinfo python=3.10 conda activate molinfo
conda install -c rdkit rdkit pip install cirpy

\## Installation

You can install the required libraries using:

\`\`\`bash pip install cirpy \# For RDKit, use conda (recommended):
conda install -c rdkit rdkit

\## Usage

Run the script and follow the prompts:

\`\`\`bash python molecule_info.py
