from django.shortcuts import render

# Create your views here.


# This method request --> call render() 
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    