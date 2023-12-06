from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = ['.', './atom_files']

a = AutoModel(env, alnfile='alig.fa',
              knowns=('3J4Q', '6F14', '1CTP'), sequence='seq')
a.starting_model = 1
a.ending_model = 2

a.make()
a.write("model.pdb")

