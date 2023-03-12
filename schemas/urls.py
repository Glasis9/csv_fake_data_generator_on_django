from django.urls import path
from schemas.views import (
    index,
    schema_delete,
    schema_create,
    SchemaUpdateView,
    schema_detail,
    dataset_create,
    download_csv,
)

urlpatterns = [
    path("", index, name="schemas"),
    path("schema-create/", schema_create, name="schema-create"),
    path("schema-delete/<int:pk>/", schema_delete, name="schema-delete"),
    path("schema-detail/<int:pk>/", schema_detail, name="schema-detail"),
    path("schema-update/<int:pk>/", SchemaUpdateView.as_view(), name="schema-update"),
    path("dataset-create/<int:pk>/", dataset_create, name="dataset-create"),
    path("download/<int:pk>/", download_csv, name="download-csv")
]
