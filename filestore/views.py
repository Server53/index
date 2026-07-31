import tempfile

from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .file_stores import file_store
from .forms import AddServerForm


@require_POST
@login_required
def upload_file(request: HttpRequest) -> HttpResponse:
    form = AddServerForm(request.POST, request.FILES)
    if form.is_valid():
        file_id = _upload_to_file_store(request.FILES["client_json_file"])  # type: ignore
        return JsonResponse({"status": "success", "file_id": file_id})
    return HttpResponseBadRequest()


def _upload_to_file_store(f: UploadedFile) -> str:
    with tempfile.TemporaryFile("wb+") as temp_file:
        for chunk in f.chunks():
            temp_file.write(chunk)
        file_id = file_store.upload(temp_file)
    return file_id


@require_GET
@login_required
def get_admin_panel(request: HttpRequest) -> HttpResponse:
    return render(request, "files_panel.html")


@require_GET
def get_file(request: HttpRequest, file_id: str) -> StreamingHttpResponse:
    file_io = file_store.download(file_id)
    return FileResponse(file_io, filename=file_id)
