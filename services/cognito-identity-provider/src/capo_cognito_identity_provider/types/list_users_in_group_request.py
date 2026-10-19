"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUsersInGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_name_type
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.query_limit_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class ListUsersInGroupRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to view the membership of the requested group.</p>"""
    group_name: "capo_cognito_identity_provider.types.group_name_type.GroupNameType"
    """<p>The name of the group that you want to query for user membership.</p>"""
    limit: NotRequired[
        "capo_cognito_identity_provider.types.query_limit_type.QueryLimitType"
    ]
    """<p>The maximum number of groups that you want Amazon Cognito to return in the response. In some SDK contexts, this operation might return fewer items than you specify in the <code>Limit</code> parameter without having reached the end of the full list. If the response contains a <code>PaginationToken</code>, then there are more results.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersInGroupRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["GroupName"] = value["group_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersInGroupRequest:
    out: ListUsersInGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
