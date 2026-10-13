"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUsersInGroupResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.users_list_type


class ListUsersInGroupResponse(TypedDict, closed=True):
    users: NotRequired[
        "capo_cognito_identity_provider.types.users_list_type.UsersListType"
    ]
    """<p>An array of users who are members in the group, and their attributes.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersInGroupResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_cognito_identity_provider.types.users_list_type

        out["Users"] = (
            capo_cognito_identity_provider.types.users_list_type.serialize_aws_json_1_1(
                value["users"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersInGroupResponse:
    out: ListUsersInGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_cognito_identity_provider.types.users_list_type

        out["users"] = (
            capo_cognito_identity_provider.types.users_list_type.deserialize_aws_json_1_1(
                data["Users"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListUsersInGroupResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_cognito_identity_provider.types.users_list_type

        out["users"] = (
            capo_cognito_identity_provider.types.users_list_type.redact_sensitive(
                value["users"]
            )
        )
    return out
