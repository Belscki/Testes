from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = """<div style='width:100%; height:100vh; display:flex;justify-content:center;align-items:center'>
<<<<<<< HEAD
                    <h1 style='font-size: 4rem; color:green'>BBBBBBBBBBBBBBBBBBBBBBBBBBBB</h1>
=======
                    <h1 style='font-size: 4rem; color:green'>aAAAAAAAAAAAAAAAAAAAAAAA.</h1>
>>>>>>> 5517210d6dc94bf88f124bc98137b67cd4b13f41
                </div>"""
    return HttpResponse(content)
