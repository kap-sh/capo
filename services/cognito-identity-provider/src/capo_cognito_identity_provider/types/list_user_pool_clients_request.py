"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolClientsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_type_type
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.query_limit
    import capo_cognito_identity_provider.types.user_pool_id_type


class ListUserPoolClientsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to list user pool clients.</p>"""
    max_results: NotRequired[
        "capo_cognito_identity_provider.types.query_limit.QueryLimit"
    ]
    """<p>The maximum number of app clients that you want Amazon Cognito to return in the response.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""
    client_type: NotRequired[
        "capo_cognito_identity_provider.types.client_type_type.ClientTypeType"
    ]
    """<p>Returns only app clients of this type. For dynamic client registration (<code>DCR</code>) and other app clients, the following values are valid.</p> <dl> <dt>REGULAR</dt> <dd> <p>An app client not created through dynamic client registration.</p> </dd> <dt>DCR</dt> <dd> <p>An app client created through dynamic client registration.</p> </dd> </dl> <p>If you omit <code>ClientType</code>, the response includes app clients of all types. When you set this filter, a page of results can contain fewer app clients than <code>MaxResults</code>, or none, while the response still includes a <code>NextToken</code>. Continue to request pages until the response has no <code>NextToken</code>. The app clients in the response don't include their type. To get the type of an app client, call <code>DescribeUserPoolClient</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolClientsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "client_type" in value:
        import capo_cognito_identity_provider.types.client_type_type

        out["ClientType"] = (
            capo_cognito_identity_provider.types.client_type_type.serialize_aws_json_1_1(
                value["client_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolClientsRequest:
    out: ListUserPoolClientsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ClientType") is not None:
        import capo_cognito_identity_provider.types.client_type_type

        out["client_type"] = (
            capo_cognito_identity_provider.types.client_type_type.deserialize_aws_json_1_1(
                data["ClientType"]
            )
        )
    return out
