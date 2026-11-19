"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociatedGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.gateway_identifier
    import capo_direct_connect.types.gateway_type
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.region


class AssociatedGateway(TypedDict, closed=True):
    id: NotRequired["capo_direct_connect.types.gateway_identifier.GatewayIdentifier"]
    """<p>The ID of the associated gateway.</p>"""
    type: NotRequired["capo_direct_connect.types.gateway_type.GatewayType"]
    """<p>The type of associated gateway.</p>"""
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The ID of the Amazon Web Services account that owns the associated virtual private gateway or transit gateway.</p>"""
    region: NotRequired["capo_direct_connect.types.region.Region"]
    """<p>The Region where the associated gateway is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedGateway) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_direct_connect.types.gateway_type

        out["type"] = capo_direct_connect.types.gateway_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedGateway:
    out: AssociatedGateway = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        import capo_direct_connect.types.gateway_type

        out["type"] = capo_direct_connect.types.gateway_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociatedGateway) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_direct_connect.types.gateway_type

        out["type"] = capo_direct_connect.types.gateway_type.serialize_cbor(
            value["type"]
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_cbor(data: dict) -> AssociatedGateway:
    out: AssociatedGateway = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        import capo_direct_connect.types.gateway_type

        out["type"] = capo_direct_connect.types.gateway_type.deserialize_cbor(
            data["type"]
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out
