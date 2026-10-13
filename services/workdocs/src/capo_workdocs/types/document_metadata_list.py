"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentMetadataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.document_metadata

DocumentMetadataList: TypeAlias = list[
    "capo_workdocs.types.document_metadata.DocumentMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentMetadataList) -> list:
    import capo_workdocs.types.document_metadata

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.document_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentMetadataList:
    import capo_workdocs.types.document_metadata

    out: DocumentMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.document_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: DocumentMetadataList) -> list[Any]:
    import capo_workdocs.types.document_metadata

    return [
        capo_workdocs.types.document_metadata.redact_sensitive(item) for item in value
    ]
