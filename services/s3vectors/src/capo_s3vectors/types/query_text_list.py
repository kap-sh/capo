"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryTextList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.query_text

QueryTextList: TypeAlias = list["capo_s3vectors.types.query_text.QueryText"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTextList) -> list:
    import capo_s3vectors.types.query_text

    out: list = []
    for item in value:
        out.append(capo_s3vectors.types.query_text.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryTextList:
    import capo_s3vectors.types.query_text

    out: QueryTextList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_s3vectors.types.query_text.deserialize_json(item))
    return out


def redact_sensitive(value: QueryTextList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
