"""Generated from Smithy shape ``com.amazonaws.iot#ListSecurityProfilesForTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.recursive
    import capo_iot.types.security_profile_target_arn


class ListSecurityProfilesForTargetRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    recursive: NotRequired["capo_iot.types.recursive.Recursive"]
    """<p>If true, return child groups too.</p>"""
    security_profile_target_arn: (
        "capo_iot.types.security_profile_target_arn.SecurityProfileTargetArn"
    )
    """<p>The ARN of the target (thing group) whose attached security profiles you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesForTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesForTargetRequest:
    out: ListSecurityProfilesForTargetRequest = {}  # type: ignore[typeddict-item]
    return out
