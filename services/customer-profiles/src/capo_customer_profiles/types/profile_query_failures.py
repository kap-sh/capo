"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileQueryFailures``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.get_segment_membership_message
    import capo_customer_profiles.types.get_segment_membership_status
    import capo_customer_profiles.types.profile_id


class ProfileQueryFailures(TypedDict, closed=True):
    profile_id: "capo_customer_profiles.types.profile_id.ProfileId"
    """<p>The profile id the failure belongs to.</p>"""
    message: "capo_customer_profiles.types.get_segment_membership_message.GetSegmentMembershipMessage"
    """<p>A message describing the failure.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.get_segment_membership_status.GetSegmentMembershipStatus"
    ]
    """<p>The status describing the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQueryFailures) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["Message"] = value["message"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ProfileQueryFailures:
    out: ProfileQueryFailures = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
