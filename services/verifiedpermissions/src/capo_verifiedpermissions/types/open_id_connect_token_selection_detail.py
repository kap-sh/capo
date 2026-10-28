"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectTokenSelectionDetail``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail
    import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail


class OpenIdConnectTokenSelectionDetailAccessTokenOnlyMember(TypedDict, closed=True):
    accessTokenOnly: "capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.OpenIdConnectAccessTokenConfigurationDetail"


class OpenIdConnectTokenSelectionDetailIdentityTokenOnlyMember(TypedDict, closed=True):
    identityTokenOnly: "capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.OpenIdConnectIdentityTokenConfigurationDetail"


OpenIdConnectTokenSelectionDetail: TypeAlias = (
    OpenIdConnectTokenSelectionDetailAccessTokenOnlyMember
    | OpenIdConnectTokenSelectionDetailIdentityTokenOnlyMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectTokenSelectionDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OpenIdConnectTokenSelectionDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.serialize_aws_json_1_0(
                value["accessTokenOnly"]
            )
        }
    elif "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.serialize_aws_json_1_0(
                value["identityTokenOnly"]
            )
        }
    else:
        raise SerializationError(
            "OpenIdConnectTokenSelectionDetail: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectTokenSelectionDetail:
    if data.get("accessTokenOnly") is not None:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail

        return {
            "accessTokenOnly": capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.deserialize_aws_json_1_0(
                data["accessTokenOnly"]
            )
        }
    elif data.get("identityTokenOnly") is not None:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail

        return {
            "identityTokenOnly": capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.deserialize_aws_json_1_0(
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
            "OpenIdConnectTokenSelectionDetail: no recognized variant key"
        )


def redact_sensitive(value: OpenIdConnectTokenSelectionDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accessTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail

        out["accessTokenOnly"] = (
            capo_verifiedpermissions.types.open_id_connect_access_token_configuration_detail.redact_sensitive(
                value["accessTokenOnly"]
            )
        )
    if "identityTokenOnly" in value:
        import capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail

        out["identityTokenOnly"] = (
            capo_verifiedpermissions.types.open_id_connect_identity_token_configuration_detail.redact_sensitive(
                value["identityTokenOnly"]
            )
        )
    return out
