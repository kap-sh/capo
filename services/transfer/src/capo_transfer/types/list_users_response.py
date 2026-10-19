"""Generated from Smithy shape ``com.amazonaws.transfer#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_users
    import capo_transfer.types.next_token
    import capo_transfer.types.server_id


class ListUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListUsers</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional users.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that the users are assigned to.</p>"""
    users: "capo_transfer.types.listed_users.ListedUsers"
    """<p>Returns the Transfer Family users and their properties for the <code>ServerId</code> value that you specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    import capo_transfer.types.listed_users

    out["Users"] = capo_transfer.types.listed_users.serialize_aws_json_1_1(
        value["users"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("Users") is not None:
        import capo_transfer.types.listed_users

        out["users"] = capo_transfer.types.listed_users.deserialize_aws_json_1_1(
            data["Users"]
        )
    else:
        out["users"] = []
    return out
