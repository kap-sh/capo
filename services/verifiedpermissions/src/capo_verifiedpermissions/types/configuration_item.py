"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ConfigurationItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cognito_user_pool_configuration_item
    import capo_verifiedpermissions.types.open_id_connect_configuration_item


class ConfigurationItemCognitoUserPoolConfigurationMember(TypedDict, closed=True):
    cognitoUserPoolConfiguration: "capo_verifiedpermissions.types.cognito_user_pool_configuration_item.CognitoUserPoolConfigurationItem"


class ConfigurationItemOpenIdConnectConfigurationMember(TypedDict, closed=True):
    openIdConnectConfiguration: "capo_verifiedpermissions.types.open_id_connect_configuration_item.OpenIdConnectConfigurationItem"


ConfigurationItem: TypeAlias = (
    ConfigurationItemCognitoUserPoolConfigurationMember
    | ConfigurationItemOpenIdConnectConfigurationMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigurationItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_item

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration_item.serialize_aws_json_1_0(
                value["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration_item

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration_item.serialize_aws_json_1_0(
                value["openIdConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("ConfigurationItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ConfigurationItem:
    if data.get("cognitoUserPoolConfiguration") is not None:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_item

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration_item.deserialize_aws_json_1_0(
                data["cognitoUserPoolConfiguration"]
            )
        }
    elif data.get("openIdConnectConfiguration") is not None:
        import capo_verifiedpermissions.types.open_id_connect_configuration_item

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration_item.deserialize_aws_json_1_0(
                data["openIdConnectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigurationItem: no recognized variant key")


def redact_sensitive(value: ConfigurationItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_item

        out["cognitoUserPoolConfiguration"] = (
            capo_verifiedpermissions.types.cognito_user_pool_configuration_item.redact_sensitive(
                value["cognitoUserPoolConfiguration"]
            )
        )
    if "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration_item

        out["openIdConnectConfiguration"] = (
            capo_verifiedpermissions.types.open_id_connect_configuration_item.redact_sensitive(
                value["openIdConnectConfiguration"]
            )
        )
    return out
