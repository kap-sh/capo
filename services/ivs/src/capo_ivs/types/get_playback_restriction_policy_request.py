"""Generated from Smithy shape ``com.amazonaws.ivs#GetPlaybackRestrictionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy_arn


class GetPlaybackRestrictionPolicyRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn"
    """<p>ARN of the playback restriction policy to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackRestrictionPolicyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetPlaybackRestrictionPolicyRequest:
    out: GetPlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
