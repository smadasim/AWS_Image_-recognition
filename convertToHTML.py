
def convertToHTML(jokeString):
    file = open('BonBon.html','w')
    file.write('<html> <head> <title>')
    file.write('Bon Bon Cracker...!! </title></head>')
    file.write('<body> <b> A joke of ' + jokeString + ': </b>')
    file.write('<audio controls> <source src =' + '../tmp/speech.mp3' + 'type = ' + '@@@audio/mpeg'
    
