# 2021 Philippine Vaccine Brand Discourse on Twitter
This repository contains the files that were used in the ongoing undergraduate research of Martha Ysaac entitled, "A Corpus-Assisted Critical Discourse Analysis of Tweets on the COVID-19 Vaccine Brand Discourse in the Philippines". Visuals of the data that were presented in the research can be found [here](https://public.tableau.com/app/profile/martha.ysaac). 

## Information about the Data
- Academic access was required to extract Tweets from the year 2021. Details on this can be read [here](https://developer.twitter.com/en/products/twitter-api/academic-research/product-details).
- The Tweets that were collected were from March 1, 2021 up until December 31, 2021.
- Five vaccine brands were chosen as the keywords for extracting Tweets related to the PH COVID-19 vaccine brand Twitter discourse: Sinovac, Pfizer, Moderna, Astrazeneca, and Sputnik.
- Tagalog was the chosen language for the language parameter in the query. 
- Details on building a query can be found [here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).

## Python Files
1. vacbrand_twitter - Program for scraping Tweets using tweepy and the Twitter API
2. vacbrand_find_string - Program for finding a specific substring from the text

## Text Files
1. alltweets_sorted - Tweets from all vaccine brands sorted alphabetically
2. alltweets_sorted_filtered - Tweets from alltweets_sorted with punctuations removed and all letters in smallcaps
3. smallcaps_sinovac - Tweets containing "sinovac" with punctuations removed and all letters in smallcaps
4. smallcaps_pfizer - Tweets containing "pfizer" with punctuations removed and all letters in smallcaps
5. smallcaps_moderna - Tweets containing "moderna" with punctuations removed and all letters in smallcaps
6. smallcaps_astrazeneca - Tweets containing "astrazeneca" with punctuations removed and all letters in smallcaps
7. smallcaps_sputnik - Tweets containing "sputnik" with punctuations removed and all letters in smallcaps

## CSV Files
1. vacbrand_tweetnumber - Table containing the number of Tweets collected per vaccine brand and month
2. alltweets_mostusedwords - Table containing the top 25 most frequently used words in alltweets_sorted.txt
3. pronoun_frequency - Table containing frequency of all pronouns
4. ko_collocations - Table containing the top 10 collocations of the singular Tagalog pronoun "ko" ("me" or "my" in English) and their frequencies
5. officialmentions_frequency - Table containing the Twitter user accounts relevant to the Philippine COVID-19 vaccine brand discourse on Twitter and their frequencies
