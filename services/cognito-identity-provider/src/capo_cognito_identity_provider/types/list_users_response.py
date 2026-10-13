"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.search_pagination_token_type
    import capo_cognito_identity_provider.types.users_list_type


class ListUsersResponse(TypedDict, closed=True):
    users: NotRequired[
        "capo_cognito_identity_provider.types.users_list_type.UsersListType"
    ]
    """<p>An array of user pool users who match your query, and their attributes. Between different requests, you might observe variations in the sequence that users in this response object are sorted into. The sort order of users isn't guaranteed to follow a single pattern, but the paginated list from a single chain of requests won't return duplicates.</p>"""
    pagination_token: NotRequired[
        "capo_cognito_identity_provider.types.search_pagination_token_type.SearchPaginationTokenType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_cognito_identity_provider.types.users_list_type

        out["Users"] = (
            capo_cognito_identity_provider.types.users_list_type.serialize_aws_json_1_1(
                value["users"]
            )
        )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_cognito_identity_provider.types.users_list_type

        out["users"] = (
            capo_cognito_identity_provider.types.users_list_type.deserialize_aws_json_1_1(
                data["Users"]
            )
        )
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    return out


def redact_sensitive(value: ListUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_cognito_identity_provider.types.users_list_type

        out["users"] = (
            capo_cognito_identity_provider.types.users_list_type.redact_sensitive(
                value["users"]
            )
        )
    return out
