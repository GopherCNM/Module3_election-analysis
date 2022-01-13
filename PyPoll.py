# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path (indirect path to the file using os.path.join)
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file (below is indirect)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a new list to store cadidate options
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Declare variables for winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the elction results and read the file ("with" command opens & closes the file, and replaces the open/close commands)
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # this is the same thing as writing total_votes = total_votes + 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate he percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate's name, vote count, and percentage of votes
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)


# Print the total votes
#code removed: print(total_votes)

# Print the candidate list
#code removed: print(candidate_options)

# Print the candidate vote dictionary
#code removed: print(candidate_votes)

# Use the open statement to open the file as a text file
    # outfile = open(file_to_save, "w")
# Close the file
    # outfile.close()

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
