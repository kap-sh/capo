"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentTypeListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_type
    import capo_comprehend.types.integer


class DocumentTypeListItem(TypedDict, closed=True):
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number.</p>"""
    type: NotRequired["capo_comprehend.types.document_type.DocumentType"]
    """<p>Document type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentTypeListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "type" in value:
        import capo_comprehend.types.document_type

        out["Type"] = capo_comprehend.types.document_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentTypeListItem:
    out: DocumentTypeListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Type") is not None:
        import capo_comprehend.types.document_type

        out["type"] = capo_comprehend.types.document_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentTypeListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "type" in value:
        import capo_comprehend.types.document_type

        out["Type"] = capo_comprehend.types.document_type.serialize_cbor(value["type"])
    return out


def deserialize_cbor(data: dict) -> DocumentTypeListItem:
    out: DocumentTypeListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Type") is not None:
        import capo_comprehend.types.document_type

        out["type"] = capo_comprehend.types.document_type.deserialize_cbor(data["Type"])
    return out
