"""Generated from Smithy shape ``com.amazonaws.securityagent#ListMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.membership_summary_list
    import capo_securityagent.types.next_token


class ListMembershipsResponse(TypedDict, closed=True):
    membership_summaries: (
        "capo_securityagent.types.membership_summary_list.MembershipSummaryList"
    )
    """<p>The list of membership summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsResponse) -> dict:
    out: dict = {}
    import capo_securityagent.types.membership_summary_list

    out["membershipSummaries"] = (
        capo_securityagent.types.membership_summary_list.serialize_json(
            value["membership_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembershipsResponse:
    out: ListMembershipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("membershipSummaries") is not None:
        import capo_securityagent.types.membership_summary_list

        out["membership_summaries"] = (
            capo_securityagent.types.membership_summary_list.deserialize_json(
                data["membershipSummaries"]
            )
        )
    else:
        out["membership_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
