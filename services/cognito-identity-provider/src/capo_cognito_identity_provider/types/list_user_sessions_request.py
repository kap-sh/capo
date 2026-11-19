"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserSessionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.token_model_type


class ListUserSessionsRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the user whose sessions you want to list. Amazon Cognito derives the user pool and username from this token.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>A pagination token that Amazon Cognito returned in a previous response. Use this value to retrieve the next page of results if a <code>NextToken</code> was included in a prior response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserSessionsRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserSessionsRequest:
    out: ListUserSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        out["access_token"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListUserSessionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
