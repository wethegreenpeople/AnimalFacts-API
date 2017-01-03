# AnimalFacts-Api
This is a simple API for serving animal facts. Included is a folder called "Facts" that has a starting point for the animal facts included in the api. These are not all the facts included in the live API, those facts are stored in a database and have been edited/added to.

Inside the /facts/ folder there is a file called 'read.py', its simply a tool for quickly reading all the facts from a .txt file into your database. Make sure to edit it before running. 

The API is live and active at http://uraqt.xyz/api/animalfacts You can sort by /animal/<animal> or /fact/<fact number>. For example: http://uraqt.xyz/api/animalfacts/animal/dog will serve all dog facts, while http://uraqt.xyz/api/animalfacts/fact/69 will only serve fact 69.

If you'd like to see a simple example of the API running you can use http://uraqt.xyz/animalfacts
