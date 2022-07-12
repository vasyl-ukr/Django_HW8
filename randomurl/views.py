import random
import string

from django.shortcuts import render


def randomstring(request):

    length = request.GET.get('length', '')
    specials = request.GET.get('specials', '')
    digits = request.GET.get('digits', '')

    check_length = [str(i) for i in range(1, 101)]
    check_bool = ['', '0', '1']

    if not (length in check_length and specials in check_bool and digits in check_bool):
        return render(request, 'randomurl/notvalid.html')
    symbols = string.ascii_letters

    if specials == "1":
        symbols += '!"№;%:?*()_+.'
    if digits == "1":
        symbols += string.digits

    ans_str = ''.join(random.choice(symbols) for i in range(int(length)))

    return render(request, 'randomurl/random.html', {'length': length, 'randomstring': ans_str})

