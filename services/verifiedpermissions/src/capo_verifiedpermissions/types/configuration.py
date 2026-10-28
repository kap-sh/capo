"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#Configuration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cognito_user_pool_configuration
    import capo_verifiedpermissions.types.open_id_connect_configuration


class ConfigurationCognitoUserPoolConfigurationMember(TypedDict, closed=True):
    cognitoUserPoolConfiguration: "capo_verifiedpermissions.types.cognito_user_pool_configuration.CognitoUserPoolConfiguration"


class ConfigurationOpenIdConnectConfigurationMember(TypedDict, closed=True):
    openIdConnectConfiguration: "capo_verifiedpermissions.types.open_id_connect_configuration.OpenIdConnectConfiguration"


Configuration: TypeAlias = (
    ConfigurationCognitoUserPoolConfigurationMember
    | ConfigurationOpenIdConnectConfigurationMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Configuration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Configuration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration.serialize_aws_json_1_0(
                value["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration.serialize_aws_json_1_0(
                value["openIdConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Configuration:
    if data.get("cognitoUserPoolConfiguration") is not None:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration.deserialize_aws_json_1_0(
                data["cognitoUserPoolConfiguration"]
            )
        }
    elif data.get("openIdConnectConfiguration") is not None:
        import capo_verifiedpermissions.types.open_id_connect_configuration

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration.deserialize_aws_json_1_0(
                data["openIdConnectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Configuration: no recognized variant key")


def redact_sensitive(value: Configuration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration

        out["cognitoUserPoolConfiguration"] = (
            capo_verifiedpermissions.types.cognito_user_pool_configuration.redact_sensitive(
                value["cognitoUserPoolConfiguration"]
            )
        )
    if "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration

        out["openIdConnectConfiguration"] = (
            capo_verifiedpermissions.types.open_id_connect_configuration.redact_sensitive(
                value["openIdConnectConfiguration"]
            )
        )
    return out
