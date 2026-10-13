"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentThumbnailUrlMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.document_thumbnail_type
    import capo_workdocs.types.url_type

DocumentThumbnailUrlMap: TypeAlias = dict[
    "capo_workdocs.types.document_thumbnail_type.DocumentThumbnailType",
    "capo_workdocs.types.url_type.UrlType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentThumbnailUrlMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_workdocs.types.document_thumbnail_type

        out[capo_workdocs.types.document_thumbnail_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DocumentThumbnailUrlMap:
    out: DocumentThumbnailUrlMap = {}
    for key, value in data.items():
        import capo_workdocs.types.document_thumbnail_type

        if value is None:
            continue
        out[capo_workdocs.types.document_thumbnail_type.deserialize_json(key)] = value
    return out


def redact_sensitive(value: DocumentThumbnailUrlMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
