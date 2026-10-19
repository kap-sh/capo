"""Generated from Smithy shape ``com.amazonaws.qapps#FileUploadCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.card_type
    import capo_qapps.types.dependency_list
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class FileUploadCard(TypedDict, closed=True):
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the file upload card.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The title of the file upload card.</p>"""
    dependencies: "capo_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the file upload card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    filename: NotRequired["str"]
    """<p>The name of the file being uploaded.</p>"""
    file_id: NotRequired["str"]
    """<p>The unique identifier of the file associated with the card.</p>"""
    allow_override: NotRequired["bool"]
    """<p>A flag indicating if the user can override the default file for the upload card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileUploadCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import capo_qapps.types.dependency_list

    out["dependencies"] = capo_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(value["type"])
    if "filename" in value:
        out["filename"] = value["filename"]
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    if "allow_override" in value:
        out["allowOverride"] = value["allow_override"]
    return out


def deserialize_json(data: dict) -> FileUploadCard:
    out: FileUploadCard = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("dependencies") is not None:
        import capo_qapps.types.dependency_list

        out["dependencies"] = capo_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        out["dependencies"] = []
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_qapps.types.card_type.CardType", "")
    if data.get("filename") is not None:
        out["filename"] = data["filename"]
    if data.get("fileId") is not None:
        out["file_id"] = data["fileId"]
    if data.get("allowOverride") is not None:
        out["allow_override"] = data["allowOverride"]
    return out
