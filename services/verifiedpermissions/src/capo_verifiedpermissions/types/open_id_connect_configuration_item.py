"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectConfigurationItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_id_prefix
    import capo_verifiedpermissions.types.issuer
    import capo_verifiedpermissions.types.open_id_connect_group_configuration_item
    import capo_verifiedpermissions.types.open_id_connect_token_selection_item


class OpenIdConnectConfigurationItem(TypedDict, closed=True):
    issuer: "capo_verifiedpermissions.types.issuer.Issuer"
    """<p>The issuer URL of an OIDC identity provider. This URL must have an OIDC discovery endpoint at the path <code>.well-known/openid-configuration</code>.</p>"""
    entity_id_prefix: NotRequired[
        "capo_verifiedpermissions.types.entity_id_prefix.EntityIdPrefix"
    ]
    """<p>A descriptive string that you want to prefix to user entities from your OIDC identity provider. For example, if you set an <code>entityIdPrefix</code> of <code>MyOIDCProvider</code>, you can reference principals in your policies in the format <code>MyCorp::User::MyOIDCProvider|Carlos</code>.</p>"""
    group_configuration: NotRequired[
        "capo_verifiedpermissions.types.open_id_connect_group_configuration_item.OpenIdConnectGroupConfigurationItem"
    ]
    """<p>The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a <code>groups</code> claim to <code>MyCorp::UserGroup</code>.</p>"""
    token_selection: "capo_verifiedpermissions.types.open_id_connect_token_selection_item.OpenIdConnectTokenSelectionItem"
    """<p>The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectConfigurationItem) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
    if "entity_id_prefix" in value:
        out["entityIdPrefix"] = value["entity_id_prefix"]
    if "group_configuration" in value:
        import capo_verifiedpermissions.types.open_id_connect_group_configuration_item

        out["groupConfiguration"] = (
            capo_verifiedpermissions.types.open_id_connect_group_configuration_item.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    import capo_verifiedpermissions.types.open_id_connect_token_selection_item

    out["tokenSelection"] = (
        capo_verifiedpermissions.types.open_id_connect_token_selection_item.serialize_aws_json_1_0(
            value["token_selection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectConfigurationItem:
    out: OpenIdConnectConfigurationItem = {}  # type: ignore[typeddict-item]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("OpenIdConnectConfigurationItem.issuer required")
    if data.get("entityIdPrefix") is not None:
        out["entity_id_prefix"] = data["entityIdPrefix"]
    if data.get("groupConfiguration") is not None:
        import capo_verifiedpermissions.types.open_id_connect_group_configuration_item

        out["group_configuration"] = (
            capo_verifiedpermissions.types.open_id_connect_group_configuration_item.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    if data.get("tokenSelection") is not None:
        import capo_verifiedpermissions.types.open_id_connect_token_selection_item

        out["token_selection"] = (
            capo_verifiedpermissions.types.open_id_connect_token_selection_item.deserialize_aws_json_1_0(
                data["tokenSelection"]
            )
        )
    else:
        raise DeserializationError(
            "OpenIdConnectConfigurationItem.token_selection required"
        )
    return out


def redact_sensitive(value: OpenIdConnectConfigurationItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entity_id_prefix" in value:
        out["entity_id_prefix"] = "*** Sensitive Data Redacted ***"
    if "group_configuration" in value:
        import capo_verifiedpermissions.types.open_id_connect_group_configuration_item

        out["group_configuration"] = (
            capo_verifiedpermissions.types.open_id_connect_group_configuration_item.redact_sensitive(
                value["group_configuration"]
            )
        )
    if "token_selection" in value:
        import capo_verifiedpermissions.types.open_id_connect_token_selection_item

        out["token_selection"] = (
            capo_verifiedpermissions.types.open_id_connect_token_selection_item.redact_sensitive(
                value["token_selection"]
            )
        )
    return out
