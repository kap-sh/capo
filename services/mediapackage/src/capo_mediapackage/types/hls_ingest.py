"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsIngest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__list_of_ingest_endpoint


class HlsIngest(TypedDict, closed=True):
    ingest_endpoints: NotRequired[
        "capo_mediapackage.types.__list_of_ingest_endpoint.__listOfIngestEndpoint"
    ]
    """A list of endpoints to which the source stream should be sent."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsIngest) -> dict:
    out: dict = {}
    if "ingest_endpoints" in value:
        import capo_mediapackage.types.__list_of_ingest_endpoint

        out["ingestEndpoints"] = (
            capo_mediapackage.types.__list_of_ingest_endpoint.serialize_json(
                value["ingest_endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsIngest:
    out: HlsIngest = {}  # type: ignore[typeddict-item]
    if data.get("ingestEndpoints") is not None:
        import capo_mediapackage.types.__list_of_ingest_endpoint

        out["ingest_endpoints"] = (
            capo_mediapackage.types.__list_of_ingest_endpoint.deserialize_json(
                data["ingestEndpoints"]
            )
        )
    return out


def redact_sensitive(value: HlsIngest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ingest_endpoints" in value:
        import capo_mediapackage.types.__list_of_ingest_endpoint

        out["ingest_endpoints"] = (
            capo_mediapackage.types.__list_of_ingest_endpoint.redact_sensitive(
                value["ingest_endpoints"]
            )
        )
    return out
