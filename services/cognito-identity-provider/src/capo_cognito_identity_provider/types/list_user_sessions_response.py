"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserSessionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.sessions_list_type


class ListUserSessionsResponse(TypedDict, closed=True):
    sessions: NotRequired[
        "capo_cognito_identity_provider.types.sessions_list_type.SessionsListType"
    ]
    """<p>A list of the user's active sessions. Each element describes one token session or SSO session.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserSessionsResponse) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_cognito_identity_provider.types.sessions_list_type

        out["Sessions"] = (
            capo_cognito_identity_provider.types.sessions_list_type.serialize_aws_json_1_1(
                value["sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserSessionsResponse:
    out: ListUserSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_cognito_identity_provider.types.sessions_list_type

        out["sessions"] = (
            capo_cognito_identity_provider.types.sessions_list_type.deserialize_aws_json_1_1(
                data["Sessions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListUserSessionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessions" in value:
        import capo_cognito_identity_provider.types.sessions_list_type

        out["sessions"] = (
            capo_cognito_identity_provider.types.sessions_list_type.redact_sensitive(
                value["sessions"]
            )
        )
    return out
