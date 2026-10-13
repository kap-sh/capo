"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectGroupConfigurationDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.claim
    import capo_verifiedpermissions.types.group_entity_type


class OpenIdConnectGroupConfigurationDetail(TypedDict, closed=True):
    group_claim: "capo_verifiedpermissions.types.claim.Claim"
    """<p>The token claim that you want Verified Permissions to interpret as group membership. For example, <code>groups</code>.</p>"""
    group_entity_type: (
        "capo_verifiedpermissions.types.group_entity_type.GroupEntityType"
    )
    """<p>The policy store entity type that you want to map your users' group claim to. For example, <code>MyCorp::UserGroup</code>. A group entity type is an entity that can have a user entity type as a member.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectGroupConfigurationDetail) -> dict:
    out: dict = {}
    out["groupClaim"] = value["group_claim"]
    out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectGroupConfigurationDetail:
    out: OpenIdConnectGroupConfigurationDetail = {}  # type: ignore[typeddict-item]
    if data.get("groupClaim") is not None:
        out["group_claim"] = data["groupClaim"]
    else:
        raise DeserializationError(
            "OpenIdConnectGroupConfigurationDetail.group_claim required"
        )
    if data.get("groupEntityType") is not None:
        out["group_entity_type"] = data["groupEntityType"]
    else:
        raise DeserializationError(
            "OpenIdConnectGroupConfigurationDetail.group_entity_type required"
        )
    return out


def redact_sensitive(value: OpenIdConnectGroupConfigurationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_claim" in value:
        out["group_claim"] = "*** Sensitive Data Redacted ***"
    if "group_entity_type" in value:
        out["group_entity_type"] = "*** Sensitive Data Redacted ***"
    return out
