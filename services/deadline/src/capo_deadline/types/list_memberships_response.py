"""Generated from Smithy shape ``com.amazonaws.deadline#ListMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.membership_summaries
    import capo_deadline.types.next_token


class ListMembershipsResponse(TypedDict, closed=True):
    memberships: "capo_deadline.types.membership_summaries.MembershipSummaries"
    """<p>The memberships associated with the specified principal.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.membership_summaries

    out["memberships"] = capo_deadline.types.membership_summaries.serialize_json(
        value["memberships"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembershipsResponse:
    out: ListMembershipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("memberships") is not None:
        import capo_deadline.types.membership_summaries

        out["memberships"] = capo_deadline.types.membership_summaries.deserialize_json(
            data["memberships"]
        )
    else:
        raise DeserializationError("ListMembershipsResponse.memberships required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
