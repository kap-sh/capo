"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListPointInTimeRecoveriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.pool_query_limit_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class ListPointInTimeRecoveriesRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to list point-in-time recoveries.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""
    max_results: NotRequired[
        "capo_cognito_identity_provider.types.pool_query_limit_type.PoolQueryLimitType"
    ]
    """<p>The maximum number of recoveries that you want Amazon Cognito to return in the response. Valid values are 1 through 60. The default value is 60.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPointInTimeRecoveriesRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPointInTimeRecoveriesRequest:
    out: ListPointInTimeRecoveriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
