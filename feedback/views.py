from django.shortcuts import render
from feedback.tasks import send_feedback_email_task

def feedback_form_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        if email and message:
            x = send_feedback_email_task.delay(email, message)
            print(f'Task ID: {x.id}')
            return render(request, 'feedback/success.html')
    
    return render(request, 'feedback/feedback.html')

def success_view(request):
    return render(request, 'feedback/success.html')




