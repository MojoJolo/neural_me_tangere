# -*- coding: utf-8 -*-
from unidecode import unidecode
import re

with open("el_filibusterismo.txt") as text_file:
    rizal = text_file.read()

rizal = rizal.decode('utf-8')

rizal = unidecode(rizal)

rizal = rizal.replace('~', '')
rizal = rizal.replace('c', 'k')
rizal = rizal.replace('C', 'K')
rizal = re.sub(r'\[[^)]*\)', '', rizal)
rizal = rizal.replace('--!', ' ')
rizal = rizal.replace('--?', ' ')
rizal = rizal.replace('--', ' ')
rizal = rizal.replace('\n', ' ')
rizal = ' '.join(rizal.split())

print rizal