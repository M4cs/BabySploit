def run():
    import subprocess as sub


    p = sub.Popen(('sudo', 'tcpdump', '-l'), stdout=sub.PIPE)
    for row in iter(p.stdout.readline, b''):
        print(row.rstrip())   # process here
