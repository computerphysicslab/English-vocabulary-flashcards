import os, json
files = [f for f in os.listdir('pics') if f.lower().endswith(('.jpg','.png','.jpeg','.gif'))]
with open('pics/flashcards.json', 'w') as out:
    json.dump(files, out, indent=2)