from scihub import SciHub

sh = SciHub()

# retrieve 5 articles on Google Scholars related to 'bittorrent'
results = sh.search('traffic', 5)

# download the papers; will use sci-hub.io if it must
for paper in results['papers']:
	sh.download(paper['url'])