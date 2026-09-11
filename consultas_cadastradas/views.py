from django import forms
from django.shortcuts import redirect, render

from consultas_cadastradas.models import Consulta, Medico, Paciente

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["nome", "especialidade", "localização", "crm", "genero", "classificacao_pacientes", "preco_consulta", "data_de_nascimento"]
        widgets ={
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "especialidade": forms.TextInput(attrs={"class": "form-control"}),
            "localização": forms.TextInput(attrs={"class": "form-control"}),
            "crm": forms.TextInput(attrs={"class": "form-control"}),
            "genero": forms.Select(attrs={"class": "form-control"}, choices=[("Masculino", "Masculino"), ("Feminino", "Feminino"), ("Outro", "Outro")]),
            "classificacao_pacientes": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "min": "0", "max": "5"}),
            "preco_consulta": forms.NumberInput(attrs={"class": "form-control","step":"0.01","min":"0"}),
            "data_de_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

def register_medico(request):
    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MedicosForm()

    return render(request, "html/cadastro_medico.html", {"form": form})

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nome", "data_de_nascimento", "cpf", "genero", "convenio_medico"]
        widgets ={
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "data_de_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "genero": forms.Select(attrs={"class": "form-control"}, choices=[("Masculino", "Masculino"), ("Feminino", "Feminino"), ("Outro", "Outro")]),
            "convenio_medico": forms.TextInput(attrs={"class": "form-control"}),
        }

def register_paciente(request):
    if request.method == "POST":
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PacientesForm()

    return render(request, "html/cadastro_paciente.html", {"form": form})

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["medico", "paciente", "data_hora", "especialidade"]
        widgets ={
            "medico": forms.Select(attrs={"class": "form-control"}),
            "paciente": forms.Select(attrs={"class": "form-control"}),
            "data_hora": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "especialidade": forms.TextInput(attrs={"class": "form-control"}),
        }


def register_consulta(request):
    if request.method == "POST":
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ConsultasForm()

    return render(request, "html/marcar_consulta.html", {"form": form})
