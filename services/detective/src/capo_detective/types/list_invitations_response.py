"""Generated from Smithy shape ``com.amazonaws.detective#ListInvitationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.member_detail_list
    import capo_detective.types.pagination_token


class ListInvitationsResponse(TypedDict, closed=True):
    invitations: NotRequired["capo_detective.types.member_detail_list.MemberDetailList"]
    """<p>The list of behavior graphs for which the member account has open or accepted invitations.</p>"""
    next_token: NotRequired["capo_detective.types.pagination_token.PaginationToken"]
    """<p>If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvitationsResponse) -> dict:
    out: dict = {}
    if "invitations" in value:
        import capo_detective.types.member_detail_list

        out["Invitations"] = capo_detective.types.member_detail_list.serialize_json(
            value["invitations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvitationsResponse:
    out: ListInvitationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Invitations") is not None:
        import capo_detective.types.member_detail_list

        out["invitations"] = capo_detective.types.member_detail_list.deserialize_json(
            data["Invitations"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListInvitationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invitations" in value:
        import capo_detective.types.member_detail_list

        out["invitations"] = capo_detective.types.member_detail_list.redact_sensitive(
            value["invitations"]
        )
    return out
