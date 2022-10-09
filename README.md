# filthy_words
A list of nsfw words, terms, phrases, scraped from internet sources and processed. 

I went looking around the net for this dataset but couldn't find it anywhere. What I was really looking for was a list of words, terms, phrases that would be associated with all sex acts and their potential permutations. If I'm being honest, I'm not certain I've captured that even now but I'm a lot closer than anyone else appears to be from my searches. Here are the steps I took to build this dataset. 

Step 1) Find collections of dirty words that are cleanly formatted:
  You would not believe how difficult this was. 
  In fact, it was so difficult, I didn't really succeed whatsoever. 

Step 2) Find collections of dirrty words that are formatted all wrong:
  Jackpot!
  Found an nsfw filter that included a lot of sex acts and references to bodyparts, but also sex-related historical events (2 girls 1 cup, as an example) at 
  https://github.com/uvasoftware/yara-language-nsfw/blob/main/src/en-language-nsfw.yara
  Found a 'dictionary' of dirty sex words here https://www.cltampa.com/news/dirty-sex-dictionary-12310282 and manually scraped

Step 3) clean data
  For the program, this was absurdly easy. Used regular expressions to remove all quoted things from each line. Throwaway code for that was this:

def extract_quotes(text):
	import re
	pattern = r'"(.+?)"'
	m = re.findall(pattern, text)
	return(m)

For the dictionary, it was a bit more complex, and I've uploaded the dirty_words.py file to capture what I did. 

step 4) Finally I extended that list using some more throwaway code to cover permutations:

suffixes=['d',"ed",'s','er','r','ing','ings','ier','ish','y']
def find_relatives(word):
	return([word+i for i in suffixes])
def strip_end(word):
	return([word[:-(len(x))] for x in suffixes if word.endswith(x)])
def extend_relatives(data):
	data=set(data)
	[data.add(x) for x in data if strip_end(x)]
	for i in range(1):
		datalist=[find_relatives(word) for word in data]
		for item in datalist:
			[data.add(i) for i in item]
	return(list(data))
  
  The resulting list of words includes words/phrases and pseudowords/phrases involving pseudowords that may nevertheless appear in conversations, such as "casting couchish" or "blumpkinery" or "cleveland steamerers". However, there is a ton of nonsense garbage, such as "sasquatchdd" and "fugleyedd". 
  
  Nevertheless, I think this is a great starting point for anyone looking to use this data to help in efforts such as nsfw model training. 
