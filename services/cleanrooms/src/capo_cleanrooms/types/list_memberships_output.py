"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListMembershipsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_summary_list
    import capo_cleanrooms.types.pagination_token


class ListMembershipsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    membership_summaries: (
        "capo_cleanrooms.types.membership_summary_list.MembershipSummaryList"
    )
    """<p>The list of memberships returned from the ListMemberships operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.membership_summary_list

    out["membershipSummaries"] = (
        capo_cleanrooms.types.membership_summary_list.serialize_json(
            value["membership_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMembershipsOutput:
    out: ListMembershipsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("membershipSummaries") is not None:
        import capo_cleanrooms.types.membership_summary_list

        out["membership_summaries"] = (
            capo_cleanrooms.types.membership_summary_list.deserialize_json(
                data["membershipSummaries"]
            )
        )
    else:
        out["membership_summaries"] = []
    return out
