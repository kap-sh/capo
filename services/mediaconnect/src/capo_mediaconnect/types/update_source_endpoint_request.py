"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateSourceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn
    import capo_mediaconnect.types.source_endpoint_configuration


class UpdateSourceEndpointRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint to update.</p>"""
    description: NotRequired["str"]
    """<p>A description to help you identify the source endpoint.</p>"""
    configuration: NotRequired[
        "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration"
    ]
    """<p>The updated configuration settings for the source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceEndpointRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "configuration" in value:
        import capo_mediaconnect.types.source_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.source_endpoint_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSourceEndpointRequest:
    out: UpdateSourceEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.source_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.source_endpoint_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
