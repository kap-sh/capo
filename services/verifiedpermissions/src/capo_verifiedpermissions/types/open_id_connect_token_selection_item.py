"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectTokenSelectionItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item
    import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item


class OpenIdConnectTokenSelectionItemAccessTokenOnlyMember(TypedDict, closed=True):
    accessTokenOnly: "capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item.OpenIdConnectAccessTokenConfigurationItem"


class OpenIdConnectTokenSelectionItemIdentityTokenOnlyMember(TypedDict, closed=True):
    identityTokenOnly: "capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.OpenIdConnectIdentityTokenConfigurationItem"


OpenIdConnectTokenSelectionItem: TypeAlias = (
    OpenIdConnectTokenSelectionItemAccessTokenOnlyMember
    | OpenIdConnectTokenSelectionItemIdentityTokenOnlyMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectTokenSelectionItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OpenIdConnectTokenSelectionItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError("OpenIdConnectTokenSelectionItem: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectTokenSelectionItem:
    if data.get("accessTokenOnly") is not None:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif data.get("identityTokenOnly") is not None:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.deserialize_aws_json_1_0(
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
            "OpenIdConnectTokenSelectionItem: no recognized variant key"
        )


def redact_sensitive(value: OpenIdConnectTokenSelectionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item

        out["accessTokenOnly"] = (
            capo_verifiedpermissions.types.open_id_connect_access_token_configuration_item.redact_sensitive(
                value["accessTokenOnly"]
            )
        )
    if "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item

        out["identityTokenOnly"] = (
            capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_item.redact_sensitive(
                value["identityTokenOnly"]
            )
        )
    return out
