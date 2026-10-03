"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.query_limit_type
    import capo_cognito_identity_provider.types.search_pagination_token_type
    import capo_cognito_identity_provider.types.searched_attribute_names_list_type
    import capo_cognito_identity_provider.types.user_filter_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class ListUsersRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to display or search for users.</p>"""
    attributes_to_get: NotRequired[
        "capo_cognito_identity_provider.types.searched_attribute_names_list_type.SearchedAttributeNamesListType"
    ]
    """<p>A JSON array of user attribute names, for example <code>given_name</code>, that you want Amazon Cognito to include in the response for each user. When you don't provide an <code>AttributesToGet</code> parameter, Amazon Cognito returns all attributes for each user.</p> <p>Use <code>AttributesToGet</code> with required attributes in your user pool, or in conjunction with <code>Filter</code>. Amazon Cognito returns an error if not all users in the results have set a value for the attribute you request. Attributes that you can't filter on, including custom attributes, must have a value set in every user profile before an <code>AttributesToGet</code> parameter returns results.</p>"""
    limit: NotRequired[
        "capo_cognito_identity_provider.types.query_limit_type.QueryLimitType"
    ]
    """<p>The maximum number of users that you want Amazon Cognito to return in the response. In some SDK contexts, this operation might return fewer items than you specify in the <code>Limit</code> parameter without having reached the end of the full list. If the response contains a <code>PaginationToken</code>, then there are more results.</p>"""
    pagination_token: NotRequired[
        "capo_cognito_identity_provider.types.search_pagination_token_type.SearchPaginationTokenType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""
    filter: NotRequired[
        "capo_cognito_identity_provider.types.user_filter_type.UserFilterType"
    ]
    r"""<p>A filter string of the form <code>"AttributeName Filter-Type "AttributeValue"</code>. Quotation marks within the filter string must be escaped using the backslash (<code>\</code>) character. For example, <code>"family_name = \"Reddy\""</code>.</p> <ul> <li> <p> <i>AttributeName</i>: The name of the attribute to search for. You can only search for one attribute at a time.</p> </li> <li> <p> <i>Filter-Type</i>: For an exact match, use <code>=</code>, for example, "<code>given_name = \"Jon\"</code>". For a prefix ("starts with") match, use <code>^=</code>, for example, "<code>given_name ^= \"Jon\"</code>". </p> </li> <li> <p> <i>AttributeValue</i>: The attribute value that must be matched for each user.</p> </li> </ul> <p>If the filter string is empty, <code>ListUsers</code> returns all users in the user pool.</p> <p>You can only search for the following standard attributes:</p> <ul> <li> <p> <code>username</code> (case-sensitive)</p> </li> <li> <p> <code>email</code> </p> </li> <li> <p> <code>phone_number</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>given_name</code> </p> </li> <li> <p> <code>family_name</code> </p> </li> <li> <p> <code>preferred_username</code> </p> </li> <li> <p> <code>cognito:user_status</code> (called <b>Status</b> in the Console) (case-insensitive)</p> </li> <li> <p> <code>status (called <b>Enabled</b> in the Console) (case-sensitive)</code> </p> </li> <li> <p> <code>sub</code> </p> </li> </ul> <p>Custom attributes aren't searchable.</p> <note> <p>You can also list users with a client-side filter. The server-side filter matches no more than one attribute. For an advanced search, use a client-side filter with the <code>--query</code> parameter of the <code>list-users</code> action in the CLI. When you use a client-side filter, ListUsers returns a paginated list of zero or more users. You can receive multiple pages in a row with zero results. Repeat the query with each pagination token that is returned until you receive a null pagination token value, and then review the combined result. </p> <p>For more information about server-side and client-side filtering, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html">FilteringCLI output</a> in the <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html">Command Line Interface User Guide</a>. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-using-listusers-api">Searching for Users Using the ListUsers API</a> and <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-listusers-api-examples">Examples of Using the ListUsers API</a> in the <i>Amazon Cognito Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "attributes_to_get" in value:
        import capo_cognito_identity_provider.types.searched_attribute_names_list_type

        out["AttributesToGet"] = (
            capo_cognito_identity_provider.types.searched_attribute_names_list_type.serialize_aws_json_1_1(
                value["attributes_to_get"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "filter" in value:
        out["Filter"] = value["filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("ListUsersRequest.user_pool_id required")
    if data.get("AttributesToGet") is not None:
        import capo_cognito_identity_provider.types.searched_attribute_names_list_type

        out["attributes_to_get"] = (
            capo_cognito_identity_provider.types.searched_attribute_names_list_type.deserialize_aws_json_1_1(
                data["AttributesToGet"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("Filter") is not None:
        out["filter"] = data["Filter"]
    return out
