"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_id


class DeleteDocument(TypedDict, closed=True):
    document_id: "capo_qbusiness.types.document_id.DocumentId"
    """<p>The identifier of the deleted document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDocument) -> dict:
    out: dict = {}
    out["documentId"] = value["document_id"]
    return out


def deserialize_json(data: dict) -> DeleteDocument:
    out: DeleteDocument = {}  # type: ignore[typeddict-item]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    else:
        out["document_id"] = ""
    return out
