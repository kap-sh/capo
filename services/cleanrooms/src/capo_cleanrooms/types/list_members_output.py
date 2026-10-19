"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListMembersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.member_summary_list
    import capo_cleanrooms.types.pagination_token


class ListMembersOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    member_summaries: "capo_cleanrooms.types.member_summary_list.MemberSummaryList"
    """<p>The list of members returned by the ListMembers operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.member_summary_list

    out["memberSummaries"] = capo_cleanrooms.types.member_summary_list.serialize_json(
        value["member_summaries"]
    )
    return out


def deserialize_json(data: dict) -> ListMembersOutput:
    out: ListMembersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("memberSummaries") is not None:
        import capo_cleanrooms.types.member_summary_list

        out["member_summaries"] = (
            capo_cleanrooms.types.member_summary_list.deserialize_json(
                data["memberSummaries"]
            )
        )
    else:
        out["member_summaries"] = []
    return out
