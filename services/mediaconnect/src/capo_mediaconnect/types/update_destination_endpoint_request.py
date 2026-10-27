"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateDestinationEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn
    import capo_mediaconnect.types.destination_endpoint_configuration


class UpdateDestinationEndpointRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the destination endpoint to update.</p>"""
    description: NotRequired["str"]
    """<p>A description to help you identify the destination endpoint.</p>"""
    configuration: NotRequired[
        "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration"
    ]
    """<p>The updated configuration settings for the destination endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDestinationEndpointRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "configuration" in value:
        import capo_mediaconnect.types.destination_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.destination_endpoint_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDestinationEndpointRequest:
    out: UpdateDestinationEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.destination_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.destination_endpoint_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
