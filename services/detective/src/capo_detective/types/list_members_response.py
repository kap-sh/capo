"""Generated from Smithy shape ``com.amazonaws.detective#ListMembersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.member_detail_list
    import capo_detective.types.pagination_token


class ListMembersResponse(TypedDict, closed=True):
    member_details: NotRequired[
        "capo_detective.types.member_detail_list.MemberDetailList"
    ]
    """<p>The list of member accounts in the behavior graph.</p> <p>For invited accounts, the results include member accounts that did not pass verification and member accounts that have not yet accepted the invitation to the behavior graph. The results do not include member accounts that were removed from the behavior graph.</p> <p>For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.</p>"""
    next_token: NotRequired["capo_detective.types.pagination_token.PaginationToken"]
    """<p>If there are more member accounts remaining in the results, then use this pagination token to request the next page of member accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "member_details" in value:
        import capo_detective.types.member_detail_list

        out["MemberDetails"] = capo_detective.types.member_detail_list.serialize_json(
            value["member_details"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if data.get("MemberDetails") is not None:
        import capo_detective.types.member_detail_list

        out["member_details"] = (
            capo_detective.types.member_detail_list.deserialize_json(
                data["MemberDetails"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListMembersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member_details" in value:
        import capo_detective.types.member_detail_list

        out["member_details"] = (
            capo_detective.types.member_detail_list.redact_sensitive(
                value["member_details"]
            )
        )
    return out
