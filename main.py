__author__ = 'johnfulgoni'

import facebook
import httplib

#https://developers.facebook.com/tools/access_token/

#permanent
app_token = "599501133559658|B-oew8OsyP3AOZwOQSewKZCQSvk"

#below has an expiration of ~1 hour
user_token = "EAAIhPjwbt2oBABEZB6aUDu5PPlEayO8bNvhxGcoAVANmyf4BedJLLLssFTEtZBW3WNvHP5H8x8ZBXzlffWu8iNPZBr0zYiJ3pmyqVMFug5nXRU7OLRiJOFCOyGYvRpiYrOkpRHdiHsx0Y6reBY2ROjKlmYSj7v5zZC8ZBNjItU1AZDZD"

graph = facebook.GraphAPI(user_token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list #not working!