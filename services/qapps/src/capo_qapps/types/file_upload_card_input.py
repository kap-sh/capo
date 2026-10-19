"""Generated from Smithy shape ``com.amazonaws.qapps#FileUploadCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.card_type
    import capo_qapps.types.filename
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class FileUploadCardInput(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the file upload card.</p>"""
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the file upload card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    filename: NotRequired["capo_qapps.types.filename.Filename"]
    """<p>The default filename to use for the file upload card.</p>"""
    file_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The identifier of a pre-uploaded file associated with the card.</p>"""
    allow_override: NotRequired["bool"]
    """<p>A flag indicating if the user can override the default file for the upload card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileUploadCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(
        value.get("type", "file-upload")
    )
    if "filename" in value:
        out["filename"] = value["filename"]
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    if "allow_override" in value:
        out["allowOverride"] = value["allow_override"]
    return out


def deserialize_json(data: dict) -> FileUploadCardInput:
    out: FileUploadCardInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "file-upload"
    if data.get("filename") is not None:
        out["filename"] = data["filename"]
    if data.get("fileId") is not None:
        out["file_id"] = data["fileId"]
    if data.get("allowOverride") is not None:
        out["allow_override"] = data["allowOverride"]
    return out
