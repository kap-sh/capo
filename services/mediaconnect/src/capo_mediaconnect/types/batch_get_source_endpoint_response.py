"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetSourceEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_source_endpoint_error_list
    import capo_mediaconnect.types.source_endpoint_list


class BatchGetSourceEndpointResponse(TypedDict, closed=True):
    source_endpoints: "capo_mediaconnect.types.source_endpoint_list.SourceEndpointList"
    """<p>The source endpoints that MediaConnect successfully retrieved.</p>"""
    errors: "capo_mediaconnect.types.batch_get_source_endpoint_error_list.BatchGetSourceEndpointErrorList"
    """<p>The errors for any source endpoints that MediaConnect couldn't retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSourceEndpointResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.source_endpoint_list

    out["sourceEndpoints"] = (
        capo_mediaconnect.types.source_endpoint_list.serialize_json(
            value["source_endpoints"]
        )
    )
    import capo_mediaconnect.types.batch_get_source_endpoint_error_list

    out["errors"] = (
        capo_mediaconnect.types.batch_get_source_endpoint_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSourceEndpointResponse:
    out: BatchGetSourceEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceEndpoints") is not None:
        import capo_mediaconnect.types.source_endpoint_list

        out["source_endpoints"] = (
            capo_mediaconnect.types.source_endpoint_list.deserialize_json(
                data["sourceEndpoints"]
            )
        )
    else:
        out["source_endpoints"] = []
    if data.get("errors") is not None:
        import capo_mediaconnect.types.batch_get_source_endpoint_error_list

        out["errors"] = (
            capo_mediaconnect.types.batch_get_source_endpoint_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
