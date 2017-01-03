from flask import Flask
import codecs
from animalfacts import db, Facts

with open('mantis-shrimp.txt') as f:
	fullFile = f.readlines()
	i = 0
	for item in fullFile:
		doot = fullFile[i].strip()
		print doot
		fact = Facts('mantis-shrimp', doot.decode('utf-8'))
		db.session.add(fact)
		i += 1

	db.session.commit()
	print ("Success")
