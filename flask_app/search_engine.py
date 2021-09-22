index_system = {}

def add_to_index(address, key_words):
    for word in key_words:
        if word in index_system:
            index_system[word].append(address)
        else:
            index_system[word]=[address]

class Site:
    def __init__(self, address, key_words):
        self.address = address
        self.key_words = key_words

def add_site(address, key_words):
    site = Site(address, key_words)
    #check for 200 response
    #check for basic content
    add_to_index(site.address, site.key_words)

def search(query):
    return index_system[query]

#call functions
add_site(
    'https://theweek.com/politics/1004642/the-ivermectin-saga-exposes-the-dishonesty-of-the-medias-professional-contrarians',
    ['ivermectin', 'Rogan']
)
add_site(
    "https://www.fda.gov/consumers/consumer-updates/why-you-should-not-use-ivermectin-treat-or-prevent-covid-19",
    ['ivermectin']
)

print(len(search('ivermectin')))
print(search('ivermectin'))
