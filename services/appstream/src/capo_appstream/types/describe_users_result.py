"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUsersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.user_list


class DescribeUsersResult(TypedDict, closed=True):
    users: NotRequired["capo_appstream.types.user_list.UserList"]
    """<p>Information about users in the user pool.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersResult) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_appstream.types.user_list

        out["Users"] = capo_appstream.types.user_list.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersResult:
    out: DescribeUsersResult = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_appstream.types.user_list

        out["users"] = capo_appstream.types.user_list.deserialize_aws_json_1_1(
            data["Users"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeUsersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_appstream.types.user_list

        out["users"] = capo_appstream.types.user_list.redact_sensitive(value["users"])
    return out
