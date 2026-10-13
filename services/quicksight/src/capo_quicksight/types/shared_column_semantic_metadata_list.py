"""Generated from Smithy shape ``com.amazonaws.quicksight#SharedColumnSemanticMetadataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.shared_column_semantic_metadata

SharedColumnSemanticMetadataList: TypeAlias = list[
    "capo_quicksight.types.shared_column_semantic_metadata.SharedColumnSemanticMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedColumnSemanticMetadataList) -> list:
    import capo_quicksight.types.shared_column_semantic_metadata

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.shared_column_semantic_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SharedColumnSemanticMetadataList:
    import capo_quicksight.types.shared_column_semantic_metadata

    out: SharedColumnSemanticMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.shared_column_semantic_metadata.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SharedColumnSemanticMetadataList) -> list[Any]:
    import capo_quicksight.types.shared_column_semantic_metadata

    return [
        capo_quicksight.types.shared_column_semantic_metadata.redact_sensitive(item)
        for item in value
    ]
