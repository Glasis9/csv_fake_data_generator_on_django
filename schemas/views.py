from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from schemas import create_fake_data
from schemas.forms import SchemaForm, RowsForm
from schemas.models import DataSchemas, DataSet


@login_required
def index(request):
    if request.user.is_authenticated:
        data = DataSchemas.objects.all()
        context = {
            "data": data
        }
        return render(request, "schemas/main_page.html", context)
    else:
        return render(request, "registration/login.html")


@login_required
def schema_create(request):
    form = SchemaForm(request.POST or None)
    if form.is_valid():
        dataschema = DataSchemas.objects.create(**form.cleaned_data)

        DataSet.objects.create(dataschema_id=dataschema.id, create_dataschemas=False)

        return HttpResponseRedirect(reverse("schemas"))
    context = {
        "form": form
    }
    return render(request, "schemas/schema_form.html", context)


class SchemaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DataSchemas
    form_class = SchemaForm
    template_name = "schemas/schema_form.html"
    success_url = reverse_lazy("schemas")


@login_required
def schema_detail(request, pk):
    try:
        schema = DataSchemas.objects.get(id=pk)
        data_set = DataSet.objects.filter(dataschema_id=pk)
        form = RowsForm()

    except DataSchemas.DoesNotExist:
        raise Http404("Schema does not exist")

    context = {
        "schema": schema,
        "data_set": data_set,
        "form": form,
    }

    return render(request, "schemas/schema_detail.html", context)


@login_required
def schema_delete(request, pk):
    DataSchemas.objects.get(id=pk).delete()
    return redirect("schemas")


@login_required
def create(request, pk):
    data_set = DataSet.objects.create(create_dataschemas=True, dataschema_id=pk)
    form = RowsForm(request.POST or None)
    if form.is_valid():
        rows = form.cleaned_data.get("rows")
        create_fake_data.create_fake_data(rows, pk, data_set)


@login_required
def dataset_create(request, pk):
    try:
        data_set = DataSet.objects.get(dataschema_id=pk)
        if data_set.create_dataschemas is False:
            form = RowsForm(request.POST or None)
            if form.is_valid():
                rows = form.cleaned_data.get("rows")
                create_fake_data.create_fake_data(rows, pk, data_set)
            return redirect("schema-detail", pk)
        else:
            create(request, pk)
            return redirect("schema-detail", pk)
    except DataSet.MultipleObjectsReturned:
        create(request, pk)
        return redirect("schema-detail", pk)


@login_required
def download_csv(request, pk):
    name = DataSet.objects.get(id=pk).url
    return FileResponse(open(name, "rb"))
