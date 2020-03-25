# from django.http import HttpResponse
#
# def file(request):
#     with open("textutils/file1.txt", "r") as f:
#         a = f.read()
#     return HttpResponse(a)
#
# def navigation(request):
#     navigate = ''' <ul> <h3> navigation webistes</h3>
#
#     <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"
#     target="blank"> code with harry </a></li>
#     <li><a href="https://mail.google.com/mail/u/0/#inbox" target="blank"> my gmail account </a></li>
#     <li><a href="https://www.w3schools.com/python/python_mongodb_getstarted.asp" target="blank"> learning mongodb </a></li>
#     <li><a href="https://www.facebook.com/ziaurrehmanAZ?ref=bookmarks" target="blank"> my facebook profile </a></li>
#     <ul>
#
#     <h3> <a href="/"> Back to home </a> </h3>
#     '''
#
#
#     return HttpResponse(navigate)