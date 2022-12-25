a = input().split()
c = []
k = []
f = False
for i in range (len(a)):
    if a[i] == '(':
        c.append(a[i])
        k.append(i)
    if a[i] == ')':
        if len(c) == 0:
            print('Ну не повезло, лишняя закрывающая скобка на', i+1,'позиции')
            f = True
            break
        if len(c) > 0:
            if c[-1] == '(':
                c.pop()
                k.pop()

if len(c) == 0 and f == False:
    print('Ура!!! Последовательность корректная')
if len(c)>0 and f == False:
    print('Эх, не повезло, скобочка открылась, однако не закрылась на позиции', k[-1]+1)