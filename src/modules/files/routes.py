import tempfile

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse

from . import config
from .file_stores import file_store

router = APIRouter()


@router.post("/upload")
def upload_file(file: UploadFile):
    with tempfile.TemporaryFile("wb+") as tmp_file:
        while chunk := file.file.read(config.CHUNK_SIZE_BYTES):
            tmp_file.write(chunk)
        file_id = file_store.upload(tmp_file)
        info = file_store.info(file_id)
        return JSONResponse({"file_id": file_id, "size": info.size})


@router.delete("/{file_id}")
def delete_file(file_id: str):
    deleted = file_store.delete(file_id)
    if not deleted:
        raise HTTPException(404, detail="File not found")
    return JSONResponse({"deleted": deleted}, status_code=204)


@router.get("/{file_id}")
def download_file(file_id: str):
    try:
        info = file_store.info(file_id)
        def file_generator():
            file = file_store.download(file_id)
            try:
                while chunk := file.read(config.CHUNK_SIZE_BYTES):
                    yield chunk
            finally:
                file.close()
        return StreamingResponse(
            content=file_generator(),
            headers={
                'Content-Disposition': f'attachment; filename="{file_id}"',
                'Content-Length': str(info.size),
            },
            media_type='application/octet-stream',
        )
    except FileNotFoundError:
        return HTTPException(404, detail="File not found")
