p = []

with open('notes.txt', 'r') as f:
    n = f.read()
    l = n.split('\n')
    for i in l:
        p.append(i)
        
test_list = [i for i in p if i] 

def some(my_str):
    d = {}
    for l in my_str:
        row = l.split('\n')
        for el in row:
            world = el.split()
            d[world[0]] = world[1:]
    return d
n = some(test_list)
data = []
news = []
for k ,v in n.items():
    data.append(k)
    news.append(v)