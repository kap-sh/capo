"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthenticationResultType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.new_device_metadata_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.token_model_type


class AuthenticationResultType(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's access token.</p>"""
    expires_in: "capo_cognito_identity_provider.types.integer_type.IntegerType"
    """<p>The expiration period of the authentication result in seconds.</p>"""
    token_type: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The intended use of the token, for example <code>Bearer</code>.</p>"""
    refresh_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's refresh token.</p>"""
    id_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>Your user's ID token.</p>"""
    new_device_metadata: NotRequired[
        "capo_cognito_identity_provider.types.new_device_metadata_type.NewDeviceMetadataType"
    ]
    """<p>The new device metadata from an authentication result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationResultType) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    out["ExpiresIn"] = value.get("expires_in", 0)
    if "token_type" in value:
        out["TokenType"] = value["token_type"]
    if "refresh_token" in value:
        out["RefreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["IdToken"] = value["id_token"]
    if "new_device_metadata" in value:
        import capo_cognito_identity_provider.types.new_device_metadata_type

        out["NewDeviceMetadata"] = (
            capo_cognito_identity_provider.types.new_device_metadata_type.serialize_aws_json_1_1(
                value["new_device_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationResultType:
    out: AuthenticationResultType = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    if data.get("ExpiresIn") is not None:
        out["expires_in"] = data["ExpiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("TokenType") is not None:
        out["token_type"] = data["TokenType"]
    if data.get("RefreshToken") is not None:
        out["refresh_token"] = data["RefreshToken"]
    if data.get("IdToken") is not None:
        out["id_token"] = data["IdToken"]
    if data.get("NewDeviceMetadata") is not None:
        import capo_cognito_identity_provider.types.new_device_metadata_type

        out["new_device_metadata"] = (
            capo_cognito_identity_provider.types.new_device_metadata_type.deserialize_aws_json_1_1(
                data["NewDeviceMetadata"]
            )
        )
    return out


def redact_sensitive(value: AuthenticationResultType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    if "refresh_token" in value:
        out["refresh_token"] = "*** Sensitive Data Redacted ***"
    if "id_token" in value:
        out["id_token"] = "*** Sensitive Data Redacted ***"
    return out
