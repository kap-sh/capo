"""Generated from Smithy shape ``com.amazonaws.qapps#CreatePresignedUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.document_scope
    import capo_qapps.types.filename
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class CreatePresignedUrlInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    card_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the card the file is associated with.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App the file is associated with.</p>"""
    file_contents_sha256: "str"
    """<p>The Base64-encoded SHA-256 digest of the contents of the file to be uploaded.</p>"""
    file_name: "capo_qapps.types.filename.Filename"
    """<p>The name of the file to be uploaded.</p>"""
    scope: "capo_qapps.types.document_scope.DocumentScope"
    """<p>Whether the file is associated with a Q App definition or a specific Q App session.</p>"""
    session_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the Q App session the file is associated with, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresignedUrlInput) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    out["appId"] = value["app_id"]
    out["fileContentsSha256"] = value["file_contents_sha256"]
    out["fileName"] = value["file_name"]
    import capo_qapps.types.document_scope

    out["scope"] = capo_qapps.types.document_scope.serialize_json(value["scope"])
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> CreatePresignedUrlInput:
    out: CreatePresignedUrlInput = {}  # type: ignore[typeddict-item]
    if data.get("cardId") is not None:
        out["card_id"] = data["cardId"]
    else:
        out["card_id"] = ""
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("fileContentsSha256") is not None:
        out["file_contents_sha256"] = data["fileContentsSha256"]
    else:
        out["file_contents_sha256"] = ""
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("scope") is not None:
        import capo_qapps.types.document_scope

        out["scope"] = capo_qapps.types.document_scope.deserialize_json(data["scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_qapps.types.document_scope.DocumentScope", "")
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    return out
