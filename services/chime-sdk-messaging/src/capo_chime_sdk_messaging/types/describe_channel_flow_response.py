"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelFlowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_flow


class DescribeChannelFlowResponse(TypedDict, closed=True):
    channel_flow: NotRequired["capo_chime_sdk_messaging.types.channel_flow.ChannelFlow"]
    """<p>The channel flow details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelFlowResponse) -> dict:
    out: dict = {}
    if "channel_flow" in value:
        import capo_chime_sdk_messaging.types.channel_flow

        out["ChannelFlow"] = capo_chime_sdk_messaging.types.channel_flow.serialize_json(
            value["channel_flow"]
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelFlowResponse:
    out: DescribeChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelFlow") is not None:
        import capo_chime_sdk_messaging.types.channel_flow

        out["channel_flow"] = (
            capo_chime_sdk_messaging.types.channel_flow.deserialize_json(
                data["ChannelFlow"]
            )
        )
    return out


def redact_sensitive(value: DescribeChannelFlowResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_flow" in value:
        import capo_chime_sdk_messaging.types.channel_flow

        out["channel_flow"] = (
            capo_chime_sdk_messaging.types.channel_flow.redact_sensitive(
                value["channel_flow"]
            )
        )
    return out
