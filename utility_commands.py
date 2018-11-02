def create_url(character_id, key_to_choose):
    import time
    import hashlib

    if key_to_choose == '1':
        private_key = "49a10a6af3f500a8a1cf7de742328d24412b62ad"
        public_key = "6308dddf4cd676cd5872a0961e7f1b68"
    if key_to_choose == '2':
        private_key = "6a750b42e5dce2cf04c02e6477e4aa2aa5fa360c"
        public_key = "36bc47996fd4980964a35ebfeec7429e"
    if key_to_choose == '3':
        private_key = "dc0592d0ab83cd4e12db3c9238b8bc71e4ef5125"
        public_key = "46f46f16b9ce8d0d8bc3cb035857ae08"
        # seperate keys due to 3000 calls / day limit.

    url = "http://gateway.marvel.com:80/v1/public/characters"
    timestamp = str(time.time())
    hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
    md5digest = str(hash.hexdigest())
    connection_url = url + "?limit=1&offset=" + str(
        character_id) + "&ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    return connection_url



def filter_description(name, description):
    words_filter = name.replace('.', '').replace('(', '').replace(')', '').replace('/', '')
    words_filter = words_filter.split()
    words_not_to_filter = ['for', 'if', 'of', 'the']
    #strips text and creates a list out of them

    description.replace(name, '***')
    for char in words_filter:
        if char not in words_not_to_filter:
            description = description.replace(char, '***')
            #finds part of the name and removes thos from the description, except
    return description

def format_raw_data(text_to_format, format_style):
    #format style 1 for names and descriptions, style 2 for series/comics
    text_to_format = text_to_format.replace('\n', '')

    if format_style == '2':
        text_to_format = text_to_format.replace('[', '').replace(']', '')
        text_to_format = text_to_format.split(', ')

    return text_to_format
