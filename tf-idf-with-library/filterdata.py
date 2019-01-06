import sqlite3, json, sys

connect = sqlite3.connect('yourdatabase.sqlite3')

databatik = json.loads(open('filename.json').read())

passing_data = []
count = 0
for text in databatik:
	if len(text['images']) != 0:
		if len(text['images']) == 1:
			passing_data.append([text['id'],text['text'],text['images'][0]])
		else:
			for img_url in text['images']:
				passing_data.append([text['id'], text['text'], img_url])

for counter, tweet in enumerate(passing_data):
	connect.execute("INSERT INTO tablename(coloumnname, coloumnname, coloumnname) VALUES (?, ?, ?, ?)", 
		(tweet[0], tweet[1], tweet[2], str(counter)+'_'+tweet[0]+tweet[2][-4:]))

connect.commit()
connect.close()