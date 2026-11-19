"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociatedCoreNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.core_network_attachment_id
    import capo_direct_connect.types.core_network_identifier
    import capo_direct_connect.types.owner_account


class AssociatedCoreNetwork(TypedDict, closed=True):
    id: NotRequired[
        "capo_direct_connect.types.core_network_identifier.CoreNetworkIdentifier"
    ]
    """<p>The ID of the Cloud WAN core network that the Direct Connect gateway is associated to.</p>"""
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The account owner of the Cloud WAN core network.</p>"""
    attachment_id: NotRequired[
        "capo_direct_connect.types.core_network_attachment_id.CoreNetworkAttachmentId"
    ]
    """<p>the ID of the Direct Connect gateway attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedCoreNetwork) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedCoreNetwork:
    out: AssociatedCoreNetwork = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociatedCoreNetwork) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_cbor(data: dict) -> AssociatedCoreNetwork:
    out: AssociatedCoreNetwork = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    return out
