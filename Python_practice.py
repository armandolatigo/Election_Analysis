#counties = ["Araphoe", "Denver", "Jefferson"]

#if "Araphoe" in counties and "El Paso" not in counties:
#        print("Only Araphoe is in the list of counties.")
#else:
#       print("Araphoe is in the list but El Paso is not in the list of counties.")




#counties_dict = {"Araphoe": 422829, "Denver":463353, "Jefferson":432438}
#for county, voters in counties_dict.items():
#               print(county, 'county has', voters, 'registered voters')




voting_data = [{"county": "Araphoe", "registered_voters":422829},
                {"county": "Denver", "registered_voters":463353},
                {"county": "Jefferson", "registered_voters":432438}]
for county_dict in voting_data:
       print(county_dict["county"])

#my_votes = int(input("How many votes did you get in the election?")) 
#total_votes = int(input("What is the total votes in the election?")) 
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes) + "% of the total votes") 
#print(f"I received {my_votes / total_votes  * 100:.2f}% of the total votes.")