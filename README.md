# PyPoll with Python

## Overview of Project

The purpose of this analysis is to help two Colorado Board of Elections employees, Tom and Seth, to validate the election results for a US Congressional Precinct. We were tasked with writing a Python script to read a CSV file containing the election results, and to deliver a report to certify the election. The report will state the number of votes cast in the election, votes and percentages by candidate, votes and percentages by county, the winning candidate, and the county with the most votes cast. Ideally, this script will be written in a way that can be repurposed and used for other future elections.

## Election-Audit Results

The following is a summary of the election results, and the supporting Python code.

- How many votes were cast in this congressional election?
369,711 votes were cast in this election.
```
total_votes = total_votes + 1
```
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson had 10.5% of the votes (38,855)
  - Denver had 82.8% of the votes (306,055)
  - Arapahoe had 6.7% of the votes (24,801)
```
for county_name in county_votes:
	votes_by_county = county_votes.get(county_name)
	county_vote_percentage = float(votes_by_county) / float(total_votes) * 100
```
- Which county had the largest number of votes?
Denver had the largest number of votes, with 306,055 of 369,711 (82.8%).
```
if (votes_by_county > largest_turnout):
	largest_turnout = votes_by_county
	largest_county = county_name
```
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham had 23.0% of the votes (85,213)
  - Diana DeGette had 73.8% of the votes (272,892)
  - Raymon Anthony Doane had 3.1% of the votes (11,606)
```
for candidate_name in candidate_votes:
	votes = candidate_votes.get(candidate_name)
	vote_percentage = float(votes) / float(total_votes) * 100
```
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Diana DeGette won the election, with 272,892 of 369,711 (73.8%)
```
if (votes > winning_count) and (vote_percentage > winning_percentage):
	winning_count = votes
	winning_candidate = candidate_name
	winning_percentage = vote_percentage
```
**Final election results report**

![Election Report](/Resources/Election_Results_Report.PNG)

## Election-Audit Summary

We wrote this Python script in such a way that it can be leveraged for other future elections. This helps to automate this important task, and to add credibility and certainty to the process. Provided election results in a CSV file, this script can be tweaked slightly to read and report results with a few minor code modifications.
- Update the election results source file name and file path as needed.
![File Name & Path](/Resources/FilePath_FileName.PNG)
- Confirm that source CSV files have header rows. If not, remove this code.
![Header Row](/Resources/Read_Header_Row.PNG)
- Confirm that columns in source CSV file are in the arranged in the same order. If not, this indexing will need to be adjusted to point to the correct columns.
![Indexes](/Resources/Candidate_County_Indexes.PNG)
