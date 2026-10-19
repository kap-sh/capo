"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputSourceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_source_metadata_details


class GetRouterInputSourceMetadataResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    name: "str"
    """<p>The name of the router input.</p>"""
    source_metadata_details: "capo_mediaconnect.types.router_input_source_metadata_details.RouterInputSourceMetadataDetails"
    """<p>Detailed metadata information about the router input source, including connection state, timestamps, and stream configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputSourceMetadataResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_input_source_metadata_details

    out["sourceMetadataDetails"] = (
        capo_mediaconnect.types.router_input_source_metadata_details.serialize_json(
            value["source_metadata_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputSourceMetadataResponse:
    out: GetRouterInputSourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sourceMetadataDetails") is not None:
        import capo_mediaconnect.types.router_input_source_metadata_details

        out["source_metadata_details"] = (
            capo_mediaconnect.types.router_input_source_metadata_details.deserialize_json(
                data["sourceMetadataDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetRouterInputSourceMetadataResponse.source_metadata_details required"
        )
    return out
