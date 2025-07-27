from rdkit import Chem
from rdkit.Chem import Draw
import cirpy
for i in range(3):
    mol = input("Please input name of molecule: ")
    info = cirpy.resolve(mol, 'smiles')
    IUPAC =cirpy.resolve(mol,'iupac_name')
    if info is not None:
        print("smiles notation: "+str(info))
    else:
        print("Sorry no Smiles")
    if IUPAC is not None:
        print("iupac notaion: "+str(IUPAC))
    else:
        print("Sorry No IUPAC found :(")
    smiles= info
    if smiles is not None:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            img=Draw.MolToImage(mol)
            img.show()
    else:
        print("could not parse the compound")
