from django.http import HttpResponse
from django.shortcuts import render

def import_tabl(request):
    return render(request, 'import.html',)

def return_tabl(request):
    user_text = request.GET['usertext']
    split_text = user_text.split(' ')
    return render(request, 'return.html',{'split_text_0': split_text[0],
                  'split_text_1': split_text[1],'split_text_2': split_text[2]})













