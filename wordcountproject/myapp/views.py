from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    full_text = request. GET['totaltext']
    word_num = full_text.split()

    word_dic = {}

    for word in word_num:
        if word in word_dic:
            word_dic[word] +=1
        else:
            word_dic[word]=1    
    
    return render(request, 'result.html', 
    {'total_text': full_text, 'total': len(word_num),"wordcount": word_dic.items()}) 

