"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUserStackAssociationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.authentication_type
    import capo_appstream.types.max_results
    import capo_appstream.types.string
    import capo_appstream.types.username


class DescribeUserStackAssociationsRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack that is associated with the user.</p>"""
    user_name: NotRequired["capo_appstream.types.username.Username"]
    """<p>The email address of the user who is associated with the stack.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>"""
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user who is associated with the stack. You must specify USERPOOL.</p>"""
    max_results: NotRequired["capo_appstream.types.max_results.MaxResults"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserStackAssociationsRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserStackAssociationsRequest:
    out: DescribeUserStackAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeUserStackAssociationsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_name" in value:
        out["user_name"] = "*** Sensitive Data Redacted ***"
    return out
