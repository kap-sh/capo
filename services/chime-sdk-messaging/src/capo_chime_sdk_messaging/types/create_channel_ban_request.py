"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelBanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class CreateChannelBanRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the ban request.</p>"""
    member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the member being banned.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelBanRequest) -> dict:
    out: dict = {}
    out["MemberArn"] = value["member_arn"]
    return out


def deserialize_json(data: dict) -> CreateChannelBanRequest:
    out: CreateChannelBanRequest = {}  # type: ignore[typeddict-item]
    if data.get("MemberArn") is not None:
        out["member_arn"] = data["MemberArn"]
    else:
        out["member_arn"] = ""
    return out
