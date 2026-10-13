"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authentication_type
    import capo_datazone.types.basic_authentication_credentials
    import capo_datazone.types.credential_map
    import capo_datazone.types.o_auth2_properties


class AuthenticationConfigurationInput(TypedDict, closed=True):
    authentication_type: NotRequired[
        "capo_datazone.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type of a connection.</p>"""
    o_auth2_properties: NotRequired[
        "capo_datazone.types.o_auth2_properties.OAuth2Properties"
    ]
    """<p>The oAuth2 properties of a connection.</p>"""
    secret_arn: NotRequired["str"]
    """<p>The secret ARN of a connection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The KMS key ARN of a connection.</p>"""
    basic_authentication_credentials: NotRequired[
        "capo_datazone.types.basic_authentication_credentials.BasicAuthenticationCredentials"
    ]
    """<p>The basic authentication credentials of a connection.</p>"""
    custom_authentication_credentials: NotRequired[
        "capo_datazone.types.credential_map.CredentialMap"
    ]
    """<p>The custom authentication credentials of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationConfigurationInput) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import capo_datazone.types.authentication_type

        out["authenticationType"] = (
            capo_datazone.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "o_auth2_properties" in value:
        import capo_datazone.types.o_auth2_properties

        out["oAuth2Properties"] = capo_datazone.types.o_auth2_properties.serialize_json(
            value["o_auth2_properties"]
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "basic_authentication_credentials" in value:
        import capo_datazone.types.basic_authentication_credentials

        out["basicAuthenticationCredentials"] = (
            capo_datazone.types.basic_authentication_credentials.serialize_json(
                value["basic_authentication_credentials"]
            )
        )
    if "custom_authentication_credentials" in value:
        import capo_datazone.types.credential_map

        out["customAuthenticationCredentials"] = (
            capo_datazone.types.credential_map.serialize_json(
                value["custom_authentication_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthenticationConfigurationInput:
    out: AuthenticationConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("authenticationType") is not None:
        import capo_datazone.types.authentication_type

        out["authentication_type"] = (
            capo_datazone.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if data.get("oAuth2Properties") is not None:
        import capo_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            capo_datazone.types.o_auth2_properties.deserialize_json(
                data["oAuth2Properties"]
            )
        )
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("basicAuthenticationCredentials") is not None:
        import capo_datazone.types.basic_authentication_credentials

        out["basic_authentication_credentials"] = (
            capo_datazone.types.basic_authentication_credentials.deserialize_json(
                data["basicAuthenticationCredentials"]
            )
        )
    if data.get("customAuthenticationCredentials") is not None:
        import capo_datazone.types.credential_map

        out["custom_authentication_credentials"] = (
            capo_datazone.types.credential_map.deserialize_json(
                data["customAuthenticationCredentials"]
            )
        )
    return out


def redact_sensitive(value: AuthenticationConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth2_properties" in value:
        import capo_datazone.types.o_auth2_properties

        out["o_auth2_properties"] = (
            capo_datazone.types.o_auth2_properties.redact_sensitive(
                value["o_auth2_properties"]
            )
        )
    if "basic_authentication_credentials" in value:
        out["basic_authentication_credentials"] = "*** Sensitive Data Redacted ***"
    if "custom_authentication_credentials" in value:
        out["custom_authentication_credentials"] = "*** Sensitive Data Redacted ***"
    return out
