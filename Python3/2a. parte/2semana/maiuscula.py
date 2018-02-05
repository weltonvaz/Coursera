def maiusculas(frase):
    pos = 0
    done = ''
    while pos < len(frase):
        if ord(frase[pos]) >= 65 and ord(frase[pos]) <=90:
            done += frase[pos]
        pos += 1
    return done
