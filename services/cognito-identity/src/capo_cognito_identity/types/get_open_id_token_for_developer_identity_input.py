"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetOpenIdTokenForDeveloperIdentityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.logins_map
    import capo_cognito_identity.types.principal_tags
    import capo_cognito_identity.types.token_duration


class GetOpenIdTokenForDeveloperIdentityInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    logins: "capo_cognito_identity.types.logins_map.LoginsMap"
    """<p>A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax <code>"developer_provider_name": "developer_user_identifier"</code>. The developer provider is the "domain" by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.</p>"""
    principal_tags: NotRequired[
        "capo_cognito_identity.types.principal_tags.PrincipalTags"
    ]
    """<p>Use this operation to configure attribute mappings for custom providers. </p>"""
    token_duration: NotRequired[
        "capo_cognito_identity.types.token_duration.TokenDuration"
    ]
    """<p>The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don't provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary Amazon Web Services credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your Amazon Web Services resources for the token's duration.</p> <note> <p>Please provide for a small grace period, usually no more than 5 minutes, to account for clock skew.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpenIdTokenForDeveloperIdentityInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    import capo_cognito_identity.types.logins_map

    out["Logins"] = capo_cognito_identity.types.logins_map.serialize_aws_json_1_1(
        value["logins"]
    )
    if "principal_tags" in value:
        import capo_cognito_identity.types.principal_tags

        out["PrincipalTags"] = (
            capo_cognito_identity.types.principal_tags.serialize_aws_json_1_1(
                value["principal_tags"]
            )
        )
    if "token_duration" in value:
        out["TokenDuration"] = value["token_duration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpenIdTokenForDeveloperIdentityInput:
    out: GetOpenIdTokenForDeveloperIdentityInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "GetOpenIdTokenForDeveloperIdentityInput.identity_pool_id required"
        )
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    if data.get("Logins") is not None:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.deserialize_aws_json_1_1(
            data["Logins"]
        )
    else:
        raise DeserializationError(
            "GetOpenIdTokenForDeveloperIdentityInput.logins required"
        )
    if data.get("PrincipalTags") is not None:
        import capo_cognito_identity.types.principal_tags

        out["principal_tags"] = (
            capo_cognito_identity.types.principal_tags.deserialize_aws_json_1_1(
                data["PrincipalTags"]
            )
        )
    if data.get("TokenDuration") is not None:
        out["token_duration"] = data["TokenDuration"]
    return out
