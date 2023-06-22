from django.shortcuts import render, redirect
#Estamos importando la "Form" de default de Django para crear usuarios
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, PasswordForm, ResetearPasswordForm #LRJ
from django.contrib.auth import login, logout, authenticate, get_user_model #LRJ
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import user_passes_test # to enable only superuser


# Create your views here.
#LRJk
@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profilePk(request, pk):
    # user=get_user_model
    # profile_pk = 
    return render(request, 'user/profile.html')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Gracias por confirmar su correo electrónico. Ya puede acceder con su e-mai y contraseña.")
        return redirect('user-login')
    else:
        messages.error(request, "El enlace de activación no es válido!")

    return redirect('user-login')

def activateEmail(request, user, to_email):
    mail_subject = "Por favor active su cuenta para ingresar a SAVIA v2.0."
    message = render_to_string("user/activarCuenta.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Estimado <b>{user.username}</b>, Favor de revisar la bandeja de entrada de su correo electrónico: <b>{to_email}</b> \
                Se ha enviado un enlace de activación para confirmar y completar su registro. <b>Nota:</b> En caso de no encontrarlo en su bandeja de entrada, Revise en Spam.')
    else:
        messages.error(request, f'Hubo un problema al enviar el enlace a {to_email}, Favor de verificar que este escrito correctamente.')
        
        
# @login_required
@user_passes_test(lambda u: u.is_superuser)
def register(request):
    User = get_user_model()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #LRJ
            username = form.cleaned_data.get('email')
            try:
                user = User.objects.get(username=username)  # Check if the user already exists
                messages.error(request, f"{username} is already registered.")
            except User.DoesNotExist:
                user = form.save(commit=False)
                user.is_active=False
                user.save()
                activateEmail(request, user, form.cleaned_data.get('email'))
                # LRJ
                # form.save()
                messages.success(request, "Usuario ha sido creado exitosamente")
                return redirect('user-register')
            except Exception as err:
                print(f'Error inesperado{err=}, {type(err)}')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                
    else:
        form = UserForm()
    ctx = {
        'form':form,
        }
    
    return render(request, 'user/register.html',ctx)


@login_required
def cambiar_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El password ha sido cambiado exitosamente")
            return redirect('user-login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = PasswordForm(user)
    return render(request, 'user/password_reset_confirm.html', {'form': form})


@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = ResetearPasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Solicitud de cambio de Password"
                message = render_to_string("user/tokenPassword.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h5>Se ha enviado un enlace de cambio de password a su e-mail</h5>
                        <p>
                            Se le ha enviado instrucciones para la configuracion de su password via correo electrónico.
                            Si el e-mail ha sido registrado, favor de revisar su bandeja de entrada.<br> En caso de no recibirlo, asegurese 
                            que lo ha escrito correctamente. Tambien revise en SPAM.
                        </p>
                        """
                    )
                else:
                    messages.error(request, ", <b>Hubo un problema en el SERVER al enviar enlace para cambiar su password</b>")

            return redirect('user-login')

        # for key, error in list(form.errors.items()):
        for error in list(form.errors.items()):
            if error[0] == 'Este campo es requirido.':
            # if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "Introduzca un password valido")
                continue

    form = ResetearPasswordForm()
    return render(
        request=request, 
        template_name="user/reset_password.html", 
        context={"form": form}
        )


def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = PasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Su password ha sido cambiado. Ya puede iniciar Sesion a partir de ahora.")
                return redirect('user-login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = PasswordForm(user)
        return render(request, 'user/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "El enlace ha expirado!")

    messages.error(request, 'Ocurrio un error inesperado, redireccionando a Inicio de Sesion')
    return redirect("user-login")