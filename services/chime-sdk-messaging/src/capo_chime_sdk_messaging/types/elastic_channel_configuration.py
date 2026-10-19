"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ElasticChannelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.maximum_sub_channels
    import capo_chime_sdk_messaging.types.minimum_membership_percentage
    import capo_chime_sdk_messaging.types.target_memberships_per_sub_channel


class ElasticChannelConfiguration(TypedDict, closed=True):
    maximum_sub_channels: (
        "capo_chime_sdk_messaging.types.maximum_sub_channels.MaximumSubChannels"
    )
    """<p>The maximum number of SubChannels that you want to allow in the elastic channel.</p>"""
    target_memberships_per_sub_channel: "capo_chime_sdk_messaging.types.target_memberships_per_sub_channel.TargetMembershipsPerSubChannel"
    """<p>The maximum number of members allowed in a SubChannel.</p>"""
    minimum_membership_percentage: "capo_chime_sdk_messaging.types.minimum_membership_percentage.MinimumMembershipPercentage"
    """<p>The minimum allowed percentage of TargetMembershipsPerSubChannel users. Ceil of the calculated value is used in balancing members among SubChannels of the elastic channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticChannelConfiguration) -> dict:
    out: dict = {}
    out["MaximumSubChannels"] = value["maximum_sub_channels"]
    out["TargetMembershipsPerSubChannel"] = value["target_memberships_per_sub_channel"]
    out["MinimumMembershipPercentage"] = value["minimum_membership_percentage"]
    return out


def deserialize_json(data: dict) -> ElasticChannelConfiguration:
    out: ElasticChannelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MaximumSubChannels") is not None:
        out["maximum_sub_channels"] = data["MaximumSubChannels"]
    else:
        out["maximum_sub_channels"] = 0
    if data.get("TargetMembershipsPerSubChannel") is not None:
        out["target_memberships_per_sub_channel"] = data[
            "TargetMembershipsPerSubChannel"
        ]
    else:
        out["target_memberships_per_sub_channel"] = 0
    if data.get("MinimumMembershipPercentage") is not None:
        out["minimum_membership_percentage"] = data["MinimumMembershipPercentage"]
    else:
        out["minimum_membership_percentage"] = 0
    return out
