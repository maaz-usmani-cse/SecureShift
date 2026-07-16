from django.shortcuts import render
from django.contrib import messages

def landing_view(req):
    res = ''
    if req.method == 'POST':
        message = req.POST.get('message', '').strip()
        keys = req.POST.get('keys', '').strip()
        choise = req.POST.get('choise', '').strip()

       
        if not message or not keys or not choise:
            messages.error(req, 'Bhai field empty n rkhe kuch value dey')
            return render(req, 'index.html')
        
        
        if not keys.isdigit():
            messages.error(req, 'keys digit m honi chahiye')
            return render(req, 'index.html')
        
       
        keys = int(keys)
        choise = int(choise)

        if choise == 2:
            keys = -keys

        for i in message:
            if i.isalpha():
                if i.isupper():
                    oldposition = ord(i) - ord('A')
                    newposition = (oldposition + keys) % 26
                    res = res + chr(newposition + ord('A'))
                elif i.islower():
                    oldposition = ord(i) - ord('a')
                    newposition = (oldposition + keys) % 26
                    res = res + chr(newposition + ord('a'))
            else:
                res = res + i

      
        if choise == 2:
            messages.success(req, 'Message successfully unlocked!')
        else:
            messages.success(req, 'Message successfully locked!')

       
        return render(req, 'index.html', {'result': res})
        
    return render(req, 'index.html')