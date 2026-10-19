"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.service_network_identifier_without_regex
    import capo_vpc_lattice.types.tag_map


class CreateServiceNetworkResourceAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID of the resource configuration to associate with the service network.</p>"""
    service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex"
    """<p>The ID of the service network to associate with the resource configuration.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the service network resource association. </p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>A key-value pair to associate with a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkResourceAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["resourceConfigurationIdentifier"] = value["resource_configuration_identifier"]
    out["serviceNetworkIdentifier"] = value["service_network_identifier"]
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkResourceAssociationRequest:
    out: CreateServiceNetworkResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resourceConfigurationIdentifier") is not None:
        out["resource_configuration_identifier"] = data[
            "resourceConfigurationIdentifier"
        ]
    else:
        out["resource_configuration_identifier"] = ""
    if data.get("serviceNetworkIdentifier") is not None:
        out["service_network_identifier"] = data["serviceNetworkIdentifier"]
    else:
        out["service_network_identifier"] = ""
    if data.get("privateDnsEnabled") is not None:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
