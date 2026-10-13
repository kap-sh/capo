"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfIngestEndpoint``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage.types.ingest_endpoint

__listOfIngestEndpoint: TypeAlias = list[
    "capo_mediapackage.types.ingest_endpoint.IngestEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIngestEndpoint) -> list:
    import capo_mediapackage.types.ingest_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediapackage.types.ingest_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIngestEndpoint:
    import capo_mediapackage.types.ingest_endpoint

    out: __listOfIngestEndpoint = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediapackage.types.ingest_endpoint.deserialize_json(item))
    return out


def redact_sensitive(value: __listOfIngestEndpoint) -> list[Any]:
    import capo_mediapackage.types.ingest_endpoint

    return [
        capo_mediapackage.types.ingest_endpoint.redact_sensitive(item) for item in value
    ]
