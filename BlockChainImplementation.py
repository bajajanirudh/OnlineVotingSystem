from threading import Timer

import time
import requests

def count_down_opening_time(opening_time, author, VoterId, CONNECTED_NODE_ADDRESS):
	def close_survey(author,questionid,CONNECTED_NODE_ADDRESS):
	    post_object = {
	        'type' : 'close',
	        'content' : {
	            'VoterId': VoterId,
	            'author': author + ':5000',
	            'timestamp': time.time()
	        }
	    }
	    # Submit a transaction
		# new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

	    # print(new_tx_address)

	    # requests.post(new_tx_address,
	    #               json=post_object,
	    #               headers={'Content-type': 'application/json'})
	# t = Timer(opening_time, close_survey, args=[author,VoterId ,CONNECTED_NODE_ADDRESS])
	# t.start()