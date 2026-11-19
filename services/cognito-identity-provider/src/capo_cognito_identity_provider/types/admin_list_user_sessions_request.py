"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminListUserSessionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminListUserSessionsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the user.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The username of the user whose sessions you want to list.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token that Amazon Cognito returned in a previous response. Use this value to retrieve the next page of results if a <code>NextToken</code> was included in a prior response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminListUserSessionsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminListUserSessionsRequest:
    out: AdminListUserSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: AdminListUserSessionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
