"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetDerivedTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.issued_token_type_identifier_type
    import capo_cognito_identity_provider.types.o_auth_token_type_type
    import capo_cognito_identity_provider.types.scope_list_type
    import capo_cognito_identity_provider.types.token_model_type


class GetDerivedTokenResponse(TypedDict, closed=True):
    issued_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>The token that Amazon Cognito issued in response to the token exchange request.</p>"""
    issued_token_type: "capo_cognito_identity_provider.types.issued_token_type_identifier_type.IssuedTokenTypeIdentifierType"
    """<p>The type of the token in the <code>IssuedToken</code> parameter. Valid values:</p> <ul> <li> <p> <code>ACCESS_TOKEN</code> – The issued token is an access token.</p> </li> <li> <p> <code>ID_TOKEN</code> – The issued token is an ID token.</p> </li> </ul>"""
    token_type: (
        "capo_cognito_identity_provider.types.o_auth_token_type_type.OAuthTokenTypeType"
    )
    """<p>The type of the issued token. For example, <code>Bearer</code>.</p>"""
    expires_in: "capo_cognito_identity_provider.types.integer_type.IntegerType"
    """<p>The number of seconds until the issued token expires.</p>"""
    scopes: NotRequired[
        "capo_cognito_identity_provider.types.scope_list_type.ScopeListType"
    ]
    """<p>The scopes that Amazon Cognito granted in the issued token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDerivedTokenResponse) -> dict:
    out: dict = {}
    out["IssuedToken"] = value["issued_token"]
    import capo_cognito_identity_provider.types.issued_token_type_identifier_type

    out["IssuedTokenType"] = (
        capo_cognito_identity_provider.types.issued_token_type_identifier_type.serialize_aws_json_1_1(
            value["issued_token_type"]
        )
    )
    import capo_cognito_identity_provider.types.o_auth_token_type_type

    out["TokenType"] = (
        capo_cognito_identity_provider.types.o_auth_token_type_type.serialize_aws_json_1_1(
            value["token_type"]
        )
    )
    out["ExpiresIn"] = value.get("expires_in", 0)
    if "scopes" in value:
        import capo_cognito_identity_provider.types.scope_list_type

        out["Scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDerivedTokenResponse:
    out: GetDerivedTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("IssuedToken") is not None:
        out["issued_token"] = data["IssuedToken"]
    else:
        out["issued_token"] = ""
    if data.get("IssuedTokenType") is not None:
        import capo_cognito_identity_provider.types.issued_token_type_identifier_type

        out["issued_token_type"] = (
            capo_cognito_identity_provider.types.issued_token_type_identifier_type.deserialize_aws_json_1_1(
                data["IssuedTokenType"]
            )
        )
    else:
        import typing

        out["issued_token_type"] = typing.cast(
            "capo_cognito_identity_provider.types.issued_token_type_identifier_type.IssuedTokenTypeIdentifierType",
            "",
        )
    if data.get("TokenType") is not None:
        import capo_cognito_identity_provider.types.o_auth_token_type_type

        out["token_type"] = (
            capo_cognito_identity_provider.types.o_auth_token_type_type.deserialize_aws_json_1_1(
                data["TokenType"]
            )
        )
    else:
        import typing

        out["token_type"] = typing.cast(
            "capo_cognito_identity_provider.types.o_auth_token_type_type.OAuthTokenTypeType",
            "",
        )
    if data.get("ExpiresIn") is not None:
        out["expires_in"] = data["ExpiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("Scopes") is not None:
        import capo_cognito_identity_provider.types.scope_list_type

        out["scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out


def redact_sensitive(value: GetDerivedTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "issued_token" in value:
        out["issued_token"] = "*** Sensitive Data Redacted ***"
    return out
