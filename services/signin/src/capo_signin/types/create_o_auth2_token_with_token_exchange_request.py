"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithTokenExchangeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.resource
    import capo_signin.types.scope
    import capo_signin.types.subject_token
    import capo_signin.types.subject_token_type
    import capo_signin.types.token_exchange_grant_type


class CreateOAuth2TokenWithTokenExchangeRequest(TypedDict, closed=True):
    grant_type: "capo_signin.types.token_exchange_grant_type.TokenExchangeGrantType"
    """The OAuth 2.0 grant type. Currently only supports "urn:ietf:params:oauth:grant-type:token-exchange"."""
    subject_token: NotRequired["capo_signin.types.subject_token.SubjectToken"]
    """The subject token that represents the identity of the party on whose behalf the request is made. Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange"."""
    subject_token_type: NotRequired[
        "capo_signin.types.subject_token_type.SubjectTokenType"
    ]
    """The token type of the subject token. Currently only supports "urn:ietf:params:oauth:token-type:jwt". Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange"."""
    resource: NotRequired["capo_signin.types.resource.Resource"]
    """The OAuth resource for which the access token is requested. Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange". Example: "glue.amazonaws.com"."""
    scope: NotRequired["capo_signin.types.scope.Scope"]
    """IAM managed policy Amazon Resource Names (ARNs) to apply as session policies that further scope down the permissions of the issued access token, provided as a space-delimited list. Example: "arn:aws:iam::444455556666:policy/MyPolicy"."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenWithTokenExchangeRequest) -> dict:
    out: dict = {}
    out["grant_type"] = value["grant_type"]
    if "subject_token" in value:
        out["subject_token"] = value["subject_token"]
    if "subject_token_type" in value:
        out["subject_token_type"] = value["subject_token_type"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "scope" in value:
        out["scope"] = value["scope"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenWithTokenExchangeRequest:
    out: CreateOAuth2TokenWithTokenExchangeRequest = {}  # type: ignore[typeddict-item]
    if data.get("grant_type") is not None:
        out["grant_type"] = data["grant_type"]
    else:
        out["grant_type"] = ""
    if data.get("subject_token") is not None:
        out["subject_token"] = data["subject_token"]
    if data.get("subject_token_type") is not None:
        out["subject_token_type"] = data["subject_token_type"]
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    if data.get("scope") is not None:
        out["scope"] = data["scope"]
    return out


def redact_sensitive(
    value: CreateOAuth2TokenWithTokenExchangeRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subject_token" in value:
        out["subject_token"] = "*** Sensitive Data Redacted ***"
    return out
