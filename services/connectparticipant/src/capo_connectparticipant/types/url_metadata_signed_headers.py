"""Generated from Smithy shape ``com.amazonaws.connectparticipant#UrlMetadataSignedHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectparticipant.types.url_metadata_signed_headers_key
    import capo_connectparticipant.types.url_metadata_signed_headers_value

UrlMetadataSignedHeaders: TypeAlias = dict[
    "capo_connectparticipant.types.url_metadata_signed_headers_key.UrlMetadataSignedHeadersKey",
    "capo_connectparticipant.types.url_metadata_signed_headers_value.UrlMetadataSignedHeadersValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UrlMetadataSignedHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UrlMetadataSignedHeaders:
    out: UrlMetadataSignedHeaders = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
