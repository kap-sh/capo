"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkServiceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.service_network_identifier
    import capo_vpc_lattice.types.tag_map


class CreateServiceNetworkServiceAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    service_network_identifier: (
        "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkServiceAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["serviceIdentifier"] = value["service_identifier"]
    out["serviceNetworkIdentifier"] = value["service_network_identifier"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkServiceAssociationRequest:
    out: CreateServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("serviceIdentifier") is not None:
        out["service_identifier"] = data["serviceIdentifier"]
    else:
        out["service_identifier"] = ""
    if data.get("serviceNetworkIdentifier") is not None:
        out["service_network_identifier"] = data["serviceNetworkIdentifier"]
    else:
        out["service_network_identifier"] = ""
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
