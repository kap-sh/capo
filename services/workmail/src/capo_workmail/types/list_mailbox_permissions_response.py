"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailboxPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.next_token
    import capo_workmail.types.permissions


class ListMailboxPermissionsResponse(TypedDict, closed=True):
    permissions: NotRequired["capo_workmail.types.permissions.Permissions"]
    """<p>One page of the user, group, or resource mailbox permissions.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is "null" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailboxPermissionsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import capo_workmail.types.permissions

        out["Permissions"] = capo_workmail.types.permissions.serialize_aws_json_1_1(
            value["permissions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailboxPermissionsResponse:
    out: ListMailboxPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Permissions") is not None:
        import capo_workmail.types.permissions

        out["permissions"] = capo_workmail.types.permissions.deserialize_aws_json_1_1(
            data["Permissions"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
