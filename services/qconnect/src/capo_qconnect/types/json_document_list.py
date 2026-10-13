"""Generated from Smithy shape ``com.amazonaws.qconnect#JSONDocumentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.json_document

JSONDocumentList: TypeAlias = list["capo_qconnect.types.json_document.JSONDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: JSONDocumentList) -> list:
    return list(value)


def deserialize_json(data: list) -> JSONDocumentList:
    return [item for item in data if item is not None]


def redact_sensitive(value: JSONDocumentList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
