# TPCFast-Log-Reader
This python script gets the TPCFast logs and then reads the .csv file to count how quick each user's replies were, and also the sums of each user's times. Note that this does not count the 001 count, since the 000 count is not in the .csv file that is originally provided.

Examples:
Username|Speed|Counts
---|---|---
AutomatedCountingBot | 0s | 1
AutomatedCountingBot | 1s | 220
AutomatedCountingBot | 2s | 192
AutomatedCountingBot | 3s | 45
AutomatedCountingBot | 4s | 10
AutomatedCountingBot | 5s | 14
AutomatedCountingBot | 6s | 2
AutomatedCountingBot | 7s | 6
AutomatedCountingBot | 9s | 3
AutomatedCountingBot | 12s | 2
AutomatedCountingBot | 13s | 1
AutomatedCountingBot | 16s | 1
AutomatedCountingBot | 17s | 1
AutomatedCountingBot | 23s | 1
notbasskro | 0s | 45
notbasskro | 1s | 333
notbasskro | 2s | 93
notbasskro | 3s | 17
notbasskro | 4s | 4
notbasskro | 9s | 1
notbasskro | 13s | 1
notbasskro | 15s | 1
notbasskro | 17s | 1
notbasskro | 31s | 1
notbasskro | 35s | 1
Countletics | 12s | 1
Antichess | 12s | 1

Username|Reply time sum
---|---
AutomatedCountingBot | 17m 3s 
notbasskro | 11m 46s 
Countletics | 12s 
Antichess | 12s 
