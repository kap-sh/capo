"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentVersionMetadataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.document_version_metadata

DocumentVersionMetadataList: TypeAlias = list[
    "capo_workdocs.types.document_version_metadata.DocumentVersionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentVersionMetadataList) -> list:
    import capo_workdocs.types.document_version_metadata

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.document_version_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentVersionMetadataList:
    import capo_workdocs.types.document_version_metadata

    out: DocumentVersionMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.document_version_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: DocumentVersionMetadataList) -> list[Any]:
    import capo_workdocs.types.document_version_metadata

    return [
        capo_workdocs.types.document_version_metadata.redact_sensitive(item)
        for item in value
    ]
