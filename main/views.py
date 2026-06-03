from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'main/index.html')

def clients(request):
    return render(request, 'main/clients.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def thanks(request):
    return render(request, 'main/thanks.html')

@csrf_exempt
def send_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company', '')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message', '')
        
        # Отправляем email администратору
        try:
            admin_subject = f'Новая заявка с сайта от {name}'
            admin_message = f'''
            Поступила новая заявка с сайта:
            
            Имя: {name}
            Компания: {company if company else 'Не указана'}
            Телефон: {phone}
            Email: {email}
            Сообщение: {message}
            
            Дата: {__import__('datetime').datetime.now().strftime("%d.%m.%Y %H:%M")}
            '''
            
            send_mail(
    f'Новая заявка от {name}',
    f'Имя: {name}\nТелефон: {phone}\nEmail: {email}\nСообщение: {message}',
    'ehedz@mail.ru',  # Отправитель
    ['ehedz@mail.ru'],  # Получатель (тот же ящик)
    fail_silently=False,
)
            print('Письмо отправлено успешно!')
        except Exception as e:
            print(f'Ошибка отправки: {e}')
        
        return redirect('thanks')
    
    return redirect('index')