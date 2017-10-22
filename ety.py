import bs4
import urllib.request as url


def find_ety(word):
    if ' ' in word:
        word = word.replace(' ', '+')

    link = 'http://www.etymonline.com/index.php?term={}&allowed_in_frame=0'.format(word)

    source = url.urlopen(link).read()
    soup = bs4.BeautifulSoup(source, 'lxml')

    dtlist = []
    for dt in soup.find_all('dt'):
        dtlist.append(dt.text)

    ddlist = []
    for dd in soup.find_all('dd'):
        ddlist.append(dd.text)

    textbody = {}
    textbody = dict(zip(dtlist, ddlist))

    par = []
    no_matches = None
    for p in soup.find_all('p'):
        par.append(p.text)
        if 'No matching terms found.' in par:
            no_matches = True

    msg = []
    for key, value in textbody.items():
        for_msg = key + '\n' + value + '\n'
        msg.append(for_msg)
    else:
        if 'No matching terms found.' not in par:
            source = 'Sourced from www.etymonline.com.' + '\n'
        msg.append(source)
        try:
            msg = '\n'.join(msg)
        except TypeError:
            if no_matches is True:
                msg = 'No matching terms found.'
            pass
    #print(msg)
    return msg


if __name__ == '__main__':
    ety = input('What word would like to find the etymology of? ')
    print(find_ety(ety))
