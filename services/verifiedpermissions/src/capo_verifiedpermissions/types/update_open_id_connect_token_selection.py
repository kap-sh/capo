"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateOpenIdConnectTokenSelection``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration
    import capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration


class UpdateOpenIdConnectTokenSelectionAccessTokenOnlyMember(TypedDict, closed=True):
    accessTokenOnly: "capo_verifiedpermissions.types.update_open_id_connect_access_token_configuration.UpdateOpenIdConnectAccessTokenConfiguration"


class UpdateOpenIdConnectTokenSelectionIdentityTokenOnlyMember(TypedDict, closed=True):
    identityTokenOnly: "capo_verifiedpermissions.types.update_open_id_connect_identity_token_configuration.UpdateOpenIdConnectIdentityTokenConfiguration"


UpdateOpenIdConnectTokenSelection: TypeAlias = (
    UpdateOpenIdConnectTokenSelectionAccessTokenOnlyMember
    | UpdateOpenIdConnectTokenSelectionIdentityTokenOnlyMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOpenIdConnectTokenSelection) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateOpenIdConnectTokenSelection: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accessTokenOnly" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
