#test_dogma.py by Sophia Chen

import dogma

print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
print(dogma.translate('ATGCCGGAATAA'))

s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
