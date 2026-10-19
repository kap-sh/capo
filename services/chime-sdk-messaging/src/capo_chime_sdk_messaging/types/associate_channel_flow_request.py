"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#AssociateChannelFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class AssociateChannelFlowRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateChannelFlowRequest) -> dict:
    out: dict = {}
    out["ChannelFlowArn"] = value["channel_flow_arn"]
    return out


def deserialize_json(data: dict) -> AssociateChannelFlowRequest:
    out: AssociateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChannelFlowArn") is not None:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    else:
        out["channel_flow_arn"] = ""
    return out
