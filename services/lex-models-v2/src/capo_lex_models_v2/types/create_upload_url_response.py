"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateUploadUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.presigned_s3_url


class CreateUploadUrlResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>An identifier for a unique import job. Use it when you call the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html">StartImport</a> operation.</p>"""
    upload_url: NotRequired["capo_lex_models_v2.types.presigned_s3_url.PresignedS3Url"]
    """<p>A pre-signed S3 write URL. Upload the zip archive file that contains the definition of your bot or bot locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadUrlResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "upload_url" in value:
        out["uploadUrl"] = value["upload_url"]
    return out


def deserialize_json(data: dict) -> CreateUploadUrlResponse:
    out: CreateUploadUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    if data.get("uploadUrl") is not None:
        out["upload_url"] = data["uploadUrl"]
    return out
