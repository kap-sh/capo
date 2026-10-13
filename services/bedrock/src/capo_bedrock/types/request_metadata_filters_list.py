"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataFiltersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.request_metadata_base_filters

RequestMetadataFiltersList: TypeAlias = list[
    "capo_bedrock.types.request_metadata_base_filters.RequestMetadataBaseFilters"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataFiltersList) -> list:
    import capo_bedrock.types.request_metadata_base_filters

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.request_metadata_base_filters.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RequestMetadataFiltersList:
    import capo_bedrock.types.request_metadata_base_filters

    out: RequestMetadataFiltersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.request_metadata_base_filters.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RequestMetadataFiltersList) -> list[Any]:
    import capo_bedrock.types.request_metadata_base_filters

    return [
        capo_bedrock.types.request_metadata_base_filters.redact_sensitive(item)
        for item in value
    ]
