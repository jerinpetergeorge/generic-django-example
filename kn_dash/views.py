# # from django.shortcuts import render
# #
# # # Create your views here.
# from redash_toolbelt import Redash as _Redash
# from pprint import pprint
# import json
#
# class Redash(_Redash):
#     def get_cached_result(self, query_id):
#         return self._get(f"api/queries/{query_id}/results").json()
#
# host = "http://134.209.146.38"
# api_key = "sOdmEx87QNybxVRryhQPdFzFYdng0FOkdPnkTe4o"
#
# client = Redash(host, api_key)
# query = client.get_cached_result(1)
# print(json.dumps(query, indent=4))
#
# from datetime import timedelta

# from django.core.management import call_command
#
# call_command("search_index", "--populate", "--parallel")
# print("Here =123")
