from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email_subject = 'You have a new message from portfolio' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + ' .Message: ' + message

        sendmail(
                email_subject,
                message_body,
                'devs5sunuwar@gmail.com',
                [admin_email],
                fail_silently = False,

        )
    return render(request, 'pages/home.html')
