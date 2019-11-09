#!/usr/bin/env python3
from pprint import pprint
from typing import List

import requests

from cache import install_4plebs_cache

install_4plebs_cache()

TOTALLY_LEGIT_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
	              'Chrome/50.0.2661.102 Safari/537.36 '
}


def should_flag_content(content: str) -> bool:
	"""Should this content be flagged?"""
	# TODO This is naive
	return 'fuck' in content


def gen_index_api_url(board: str, page: int) -> str:
	"""Given a board and page number, return a URL for the web API that will retrieve that index page's posts."""
	return "http://archive.4plebs.org/_/api/chan/index/?board={board}&page={page}".format(
		board=board,
		page=page,
	)


def gen_post_api_url(board: str, postid: int) -> str:
	"""Given a board and post number, return a URL for the web API that will retrieve that post's info."""
	return "http://archive.4plebs.org/_/api/chan/post/?board={board}&num={postid}".format(
		board=board,
		postid=postid,
	)


def gen_thread_api_url(board: str, threadid: int) -> str:
	"""Given a board and thread number, return a URL for the web API that will retrieve that thread's info."""
	return "http://archive.4plebs.org/_/api/chan/thread/?board={board}&num={threadid}".format(
		board=board,
		threadid=threadid
	)


class FourPlebsAPI_Post:
	"""
	Constructor to access properties of 4plebs API response objects.

	Not necessary per se but makes interacting with 4plebs API response objects easier.
	"""

	def __init__(self, id: int, json: dict):
		"""
		:rtype: FourPlebsAPI_Post
		"""
		self._json = json
		self.id = id

	@property
	def board_code(self):
		return self._json['op']['board']['shortname']

	def gen_post_api_url(self):
		return gen_post_api_url(self.board_code, self.id)

	def __str__(self):
		return ''' >> {klassname} << 
	Post ID {postid}
	'''.format(
			klassname=self.__class__.__name__,
			postid=self.id
		)


def extract_threadids_from_index_json(index_json: dict) -> List[int]:
	"""Given a JSON object from an index, return a list of thread IDs inside that index JSON object."""
	postids = index_json.keys()

	threadids = []

	# See if we can extract threads posts
	# Go through each post,
	for postid in postids:
		json_obj = index_json[postid]
		threadids.append(int(json_obj['op']['thread_num']))

	return threadids


def httpGET_json(url: str) -> dict:
	"""Given a URL, request content via HTTP GET and return the JSON object the request provides."""
	response = requests.get(url, headers=TOTALLY_LEGIT_HEADERS)

	if not response.status_code == 200:
		raise Exception("Response from {} gave {} != 200!".format(url, response.status_code))

	data = (response.json())

	return data


if __name__ == '__main__':

	BOARD = 'pol'
	BOARD = 'x'

	result = httpGET_json(gen_index_api_url(BOARD, 1))

	postids = result.keys()

	pprint(result)
	pprint(postids)

	print("All thread API URLs from the first page of /{}/:".format(BOARD))
	for threadid in extract_threadids_from_index_json(result):
		print(gen_thread_api_url(board=BOARD, threadid=threadid))

	for id, jsonObject in result.items():
		post = FourPlebsAPI_Post(id, jsonObject)
		print(post)
