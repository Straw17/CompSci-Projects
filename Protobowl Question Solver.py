from googlesearch import search

while True:
    rawtext = input('Input question: ')

    text = rawtext.split(' ')
    query = ''

    for word in range(len(text)):
        try:
            if text[word][0].isupper() or text[word][1].isupper():
                if word != 0:
                    if '.' not in text[word-1]:
                        query += text[word] + ' '
            elif 'this' in text[word-1].lower():
                if text[word] not in query:
                    query = text[word] + ' ' + query
        except IndexError:
            continue

    query = query.replace('“', '')
    query = query.replace('”', '')
    query = query.replace('"', '')
    print(query)
    for url in search(query, tld='com.pk', lang='es', stop=20):
        if 'wikipedia' in url:
            result = url.split('/')
            result = result[len(result)-1]
            result = result.replace('_', ' ')
            if result not in rawtext:
                print('\n' + result + '\n')
            break
