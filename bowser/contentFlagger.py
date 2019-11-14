import re
from typing import List


class ContentFlagger:
	"""A class that can flag content as containing specific words or phrases."""

	def __init__(self, keywords: List[str], regex_matches: List[str]):
		self.match_words = keywords
		self.regex_matches = regex_matches

	def flag_content(self, content: str):

		if content is None:  # thanks for the null values json <3 i feel like i'm in Java all over again
			return False

		# Fix any issues dealing with capitalization
		content = content.lower()

		# check all our keywords
		for word in self.match_words:
			if word in content.split(" "):
				return True

		# check all our regex
		for rexp in self.regex_matches:
			if re.compile(rexp).match(content):
				return True

		return False

 
ContentFlaggerRacism = ContentFlagger(
	keywords=[
		'nigger', 'negro', 'niglet', 'shitskin', 'cuck',
		'scum', 'degenerate', 'crusade',
		'kike', 'jew', 'shekel', 'chink', 'slanty eye',
		'gas', 'genocide', 'final solution', 'uss liberty',
		'goyper' 
	],

	regex_matches=[
		r'anti[.|]white'
		r'deep[.|]state'
		r'nationalis[tm]'
		r'birth[.|]rate',
		r'wipe. out',
		r'\({2,}[\w ]+\){2,}', #((echoes))
	],
)

ContentFlaggerBadWords = ContentFlagger(
	keywords=[
		'soyboy',  # TODO: Reclassify? IDK.
		'tranny', 'homo', 'queer', 'attack helicopter',
		'pepe', 'groyper',
		'maga', 'magapede',  # TODO: Politics flagger c
	],

	regex_matches=[
		r'she{1,}i{1,}t',
		r'fag(|got)',
		r'f[.|]ck',
		r'.*gate'
	],
)

ContentFlaggerTerrorist = ContentFlagger(
	keywords=[
		'bomb', 'assault', 'nuke', 'nuclear', 'gun',
		'kill', 'chemical', 'poison', 'virus',
		'merc', 'suicide', 'IED', 'weapon', 'terror', 'cartel',
		'breach', 'NSA', 'radio', 'isis', ],

	regex_matches=[
		r'(love if|someone (should|will|)) \w{1,10} (sho{1,2}t|bomb)',
		r'assassin(|ate(|d))'
	],
)

ContentFlaggerConspiracyTheories = ContentFlagger(
	keywords=[ 'Illuminati', 'Lizard',
		
	],

	regex_matches=[
		
		r'.*gate'
	]
)