"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutMessagingStreamingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.streaming_configuration_list


class PutMessagingStreamingConfigurationsRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the streaming configuration.</p>"""
    streaming_configurations: "capo_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList"
    """<p>The streaming configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMessagingStreamingConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.streaming_configuration_list

    out["StreamingConfigurations"] = (
        capo_chime_sdk_messaging.types.streaming_configuration_list.serialize_json(
            value["streaming_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutMessagingStreamingConfigurationsRequest:
    out: PutMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StreamingConfigurations") is not None:
        import capo_chime_sdk_messaging.types.streaming_configuration_list

        out["streaming_configurations"] = (
            capo_chime_sdk_messaging.types.streaming_configuration_list.deserialize_json(
                data["StreamingConfigurations"]
            )
        )
    else:
        out["streaming_configurations"] = []
    return out
