import requests, json, random
from secrets import secrets

base_url = "http://capitolwords.org/api/1/phrases.json"
params = {
    'apikey': secrets['sunlight_key'], 
    'entity_type': 'month', 
    'entity_value': '201411'
}
r = requests.get(base_url, params=params)

print r.text

words = json.loads(r.text)
# words = sorted(words, key=lambda k: k['count']) 
print words[0:4]

top_10 = words[0:20]

random_ints = []

shakes_line = 'O %s, %s! wherefore art thou %s?'
shakes_line_2 = "All the world 's a %s, and all the %s and %s merely %s."

words_list = []

def gen_random_keys(num, maximum):
  key_list = []
  for i in range(num):
    rand_int = random.randint(0, maximum)
    while rand_int in key_list:
      rand_int = random.randint(0, maximum)
    key_list.append(rand_int)
  return key_list

key_list = gen_random_keys(4, 19)

for num in key_list:
  words_list.append(top_10[num]['ngram'])

print shakes_line_2 % (words_list[0], words_list[1], words_list[2], words_list[3])
