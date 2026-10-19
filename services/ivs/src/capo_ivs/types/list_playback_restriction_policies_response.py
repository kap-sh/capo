"""Generated from Smithy shape ``com.amazonaws.ivs#ListPlaybackRestrictionPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.pagination_token
    import capo_ivs.types.playback_restriction_policy_list


class ListPlaybackRestrictionPoliciesResponse(TypedDict, closed=True):
    playback_restriction_policies: (
        "capo_ivs.types.playback_restriction_policy_list.PlaybackRestrictionPolicyList"
    )
    """<p>List of the matching policies.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more channels than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackRestrictionPoliciesResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.playback_restriction_policy_list

    out["playbackRestrictionPolicies"] = (
        capo_ivs.types.playback_restriction_policy_list.serialize_json(
            value["playback_restriction_policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaybackRestrictionPoliciesResponse:
    out: ListPlaybackRestrictionPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("playbackRestrictionPolicies") is not None:
        import capo_ivs.types.playback_restriction_policy_list

        out["playback_restriction_policies"] = (
            capo_ivs.types.playback_restriction_policy_list.deserialize_json(
                data["playbackRestrictionPolicies"]
            )
        )
    else:
        out["playback_restriction_policies"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
