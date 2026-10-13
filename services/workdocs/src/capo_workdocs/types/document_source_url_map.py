"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentSourceUrlMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.document_source_type
    import capo_workdocs.types.url_type

DocumentSourceUrlMap: TypeAlias = dict[
    "capo_workdocs.types.document_source_type.DocumentSourceType",
    "capo_workdocs.types.url_type.UrlType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentSourceUrlMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_workdocs.types.document_source_type

        out[capo_workdocs.types.document_source_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DocumentSourceUrlMap:
    out: DocumentSourceUrlMap = {}
    for key, value in data.items():
        import capo_workdocs.types.document_source_type

        if value is None:
            continue
        out[capo_workdocs.types.document_source_type.deserialize_json(key)] = value
    return out


def redact_sensitive(value: DocumentSourceUrlMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
