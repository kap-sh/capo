"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateCoreNetworkPrefixListAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.prefix_list_arn


class CreateCoreNetworkPrefixListAssociationRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to associate with the prefix list.</p>"""
    prefix_list_arn: "capo_networkmanager.types.prefix_list_arn.PrefixListArn"
    """<p>The ARN of the prefix list to associate with the core network.</p>"""
    prefix_list_alias: "capo_networkmanager.types.constrained_string.ConstrainedString"
    """<p>An optional alias for the prefix list association.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkPrefixListAssociationRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["PrefixListArn"] = value["prefix_list_arn"]
    out["PrefixListAlias"] = value["prefix_list_alias"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkPrefixListAssociationRequest:
    out: CreateCoreNetworkPrefixListAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("PrefixListArn") is not None:
        out["prefix_list_arn"] = data["PrefixListArn"]
    else:
        out["prefix_list_arn"] = ""
    if data.get("PrefixListAlias") is not None:
        out["prefix_list_alias"] = data["PrefixListAlias"]
    else:
        out["prefix_list_alias"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
