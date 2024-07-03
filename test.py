# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-s','--square',action='store_true',help="used as an example")
# # parser.add_argument('square',type=int,help="used as an example")

# args = parser.parse_args()

# if args.square:
#     print(2)
# else:
#     print(1)


# from os import listdir

# print(listdir('.'))

# ## Creates empty dictionary named results_dic
# results_dic = dict()

# ## Determines number of items in dictionary
# items_in_dic = len(results_dic)
# print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

# ## Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
# ## a List that contains only one item - the pet image label
# filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
# pet_labels = ["beagle", "boston terrier"]
# for idx in range(0, len(filenames), 1):
#     if filenames[idx] not in results_dic:
#          results_dic[filenames[idx]] = [pet_labels[idx]]
#     else:
#          print("** Warning: Key=", filenames[idx], 
#                "already exists in results_dic with value =", 
#                results_dic[filenames[idx]])

# #Iterating through a dictionary printing all keys & their associated values
# print("\nPrinting all key-value pairs in dictionary results_dic:")
# for key in results_dic:
#     print("Filename=", key, "   Pet Label=", results_dic[key][0])











def isAnagram(s, t):
     if len(s) != len(t):
          return False
    
     s_dic = dict()

     for c in s:
          s_dic[c] = s_dic.get(c, 0) + 1

     t_dic = dict()
     for c in t:    
          t_dic[c] = t_dic.get(c, 0) + 1

     print(t_dic)
     print(s_dic)
     return s_dic == t_dic
        


print(isAnagram('anagram','nagaram'))












