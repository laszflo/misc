# %%
# To compare two sequences
# find the length of the longest subsequence present in both of them

from difflib import SequenceMatcher

seq = SequenceMatcher(None, "ABCDDZDZDZDz", "ABDCZDZDZDZDZ")
print(seq.ratio())  # ratio de ressemblance
print(seq.find_longest_match(0, 8, 0, 8)) # find the longest match






# %% convert to hash -
# https://www.md5hashgenerator.com/


