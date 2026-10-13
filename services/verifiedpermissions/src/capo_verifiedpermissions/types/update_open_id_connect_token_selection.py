"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateOpenIdConnectTokenSelection``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration
    import capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration


class _UpdateOpenIdConnectTokenSelection_accessTokenOnly(TypedDict, closed=True):
    accessTokenOnly: "capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration.UpdateOpenIdConnectAccessTokenConfiguration"


class _UpdateOpenIdConnectTokenSelection_identityTokenOnly(TypedDict, closed=True):
    identityTokenOnly: "capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.UpdateOpenIdConnectIdentityTokenConfiguration"


UpdateOpenIdConnectTokenSelection: TypeAlias = (
    _UpdateOpenIdConnectTokenSelection_accessTokenOnly
    | _UpdateOpenIdConnectTokenSelection_identityTokenOnly
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOpenIdConnectTokenSelection) -> dict:
    if "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError(
            "UpdateOpenIdConnectTokenSelection: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> UpdateOpenIdConnectTokenSelection:
    if data.get("accessTokenOnly") is not None:
        import capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif data.get("identityTokenOnly") is not None:
        import capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.deserialize_aws_json_1_0(
                data["identityTokenOnly"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateOpenIdConnectTokenSelection: no recognized variant key"
        )


def redact_sensitive(value: UpdateOpenIdConnectTokenSelection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration

        out["accessTokenOnly"] = (
            capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration.redact_sensitive(
                value["accessTokenOnly"]
            )
        )
    if "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration

        out["identityTokenOnly"] = (
            capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.redact_sensitive(
                value["identityTokenOnly"]
            )
        )
    return out
