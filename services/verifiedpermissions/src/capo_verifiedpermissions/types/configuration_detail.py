"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ConfigurationDetail``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cognito_user_pool_configuration_detail
    import capo_verifiedpermissions.types.open_id_connect_configuration_detail


class _ConfigurationDetail_cognitoUserPoolConfiguration(TypedDict, closed=True):
    cognitoUserPoolConfiguration: "capo_verifiedpermissions.types.cognito_user_pool_configuration_detail.CognitoUserPoolConfigurationDetail"


class _ConfigurationDetail_openIdConnectConfiguration(TypedDict, closed=True):
    openIdConnectConfiguration: "capo_verifiedpermissions.types.open_id_connect_configuration_detail.OpenIdConnectConfigurationDetail"


ConfigurationDetail: TypeAlias = (
    _ConfigurationDetail_cognitoUserPoolConfiguration
    | _ConfigurationDetail_openIdConnectConfiguration
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigurationDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_detail

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration_detail.serialize_aws_json_1_0(
                value["cognitoUserPoolConfiguration"]
            )
        }
    elif "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration_detail

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration_detail.serialize_aws_json_1_0(
                value["openIdConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("ConfigurationDetail: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ConfigurationDetail:
    if data.get("cognitoUserPoolConfiguration") is not None:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_detail

        return {
            "cognitoUserPoolConfiguration": capo_verifiedpermissions.types.cognito_user_pool_configuration_detail.deserialize_aws_json_1_0(
                data["cognitoUserPoolConfiguration"]
            )
        }
    elif data.get("openIdConnectConfiguration") is not None:
        import capo_verifiedpermissions.types.open_id_connect_configuration_detail

        return {
            "openIdConnectConfiguration": capo_verifiedpermissions.types.open_id_connect_configuration_detail.deserialize_aws_json_1_0(
                data["openIdConnectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigurationDetail: no recognized variant key")


def redact_sensitive(value: ConfigurationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cognitoUserPoolConfiguration" in value:
        import capo_verifiedpermissions.types.cognito_user_pool_configuration_detail

        out["cognitoUserPoolConfiguration"] = (
            capo_verifiedpermissions.types.cognito_user_pool_configuration_detail.redact_sensitive(
                value["cognitoUserPoolConfiguration"]
            )
        )
    if "openIdConnectConfiguration" in value:
        import capo_verifiedpermissions.types.open_id_connect_configuration_detail

        out["openIdConnectConfiguration"] = (
            capo_verifiedpermissions.types.open_id_connect_configuration_detail.redact_sensitive(
                value["openIdConnectConfiguration"]
            )
        )
    return out
