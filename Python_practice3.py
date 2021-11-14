#x = 0
#while x <=5:
#    x = x +1
#    print(x)


counties_dict = {"Araphoe": 422829, "Denver": 463353, "Jefferson":432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")



#candidate_votes = int(input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
#    f'you received {candidate_votes:,} votes.' 
#     f' The total number of votes in the election was {total_votes:,}.'
#      f' You received {candidate_votes / total_votes * 100:.2f}% of the total votes.'
#)
#print(message_to_candidate)
 
 