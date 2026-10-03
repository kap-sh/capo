"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.groups
    import capo_workmail.types.next_token


class ListGroupsResponse(TypedDict, closed=True):
    groups: NotRequired["capo_workmail.types.groups.Groups"]
    """<p>The overview of groups for an organization.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_workmail.types.groups

        out["Groups"] = capo_workmail.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Groups") is not None:
        import capo_workmail.types.groups

        out["groups"] = capo_workmail.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
