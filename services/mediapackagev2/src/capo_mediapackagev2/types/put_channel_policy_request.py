"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#PutChannelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.policy_text
    import capo_mediapackagev2.types.resource_name


class PutChannelPolicyRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    policy: "capo_mediapackagev2.types.policy_text.PolicyText"
    """<p>The policy to attach to the specified channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutChannelPolicyRequest:
    out: PutChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
