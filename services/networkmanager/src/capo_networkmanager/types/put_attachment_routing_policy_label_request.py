"""Generated from Smithy shape ``com.amazonaws.networkmanager#PutAttachmentRoutingPolicyLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id


class PutAttachmentRoutingPolicyLabelRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network containing the attachment.</p>"""
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment to apply the routing policy label to.</p>"""
    routing_policy_label: (
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    )
    """<p>The routing policy label to apply to the attachment.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAttachmentRoutingPolicyLabelRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["AttachmentId"] = value["attachment_id"]
    out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutAttachmentRoutingPolicyLabelRequest:
    out: PutAttachmentRoutingPolicyLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    else:
        out["attachment_id"] = ""
    if data.get("RoutingPolicyLabel") is not None:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    else:
        out["routing_policy_label"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
