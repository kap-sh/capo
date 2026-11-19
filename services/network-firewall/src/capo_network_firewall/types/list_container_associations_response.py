"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListContainerAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_associations
    import capo_network_firewall.types.pagination_token


class ListContainerAssociationsResponse(TypedDict, closed=True):
    container_associations: NotRequired[
        "capo_network_firewall.types.container_associations.ContainerAssociations"
    ]
    """<p>The container association metadata objects for the account and Region.</p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContainerAssociationsResponse) -> dict:
    out: dict = {}
    if "container_associations" in value:
        import capo_network_firewall.types.container_associations

        out["ContainerAssociations"] = (
            capo_network_firewall.types.container_associations.serialize_aws_json_1_0(
                value["container_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContainerAssociationsResponse:
    out: ListContainerAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociations") is not None:
        import capo_network_firewall.types.container_associations

        out["container_associations"] = (
            capo_network_firewall.types.container_associations.deserialize_aws_json_1_0(
                data["ContainerAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListContainerAssociationsResponse) -> dict:
    out: dict = {}
    if "container_associations" in value:
        import capo_network_firewall.types.container_associations

        out["ContainerAssociations"] = (
            capo_network_firewall.types.container_associations.serialize_cbor(
                value["container_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListContainerAssociationsResponse:
    out: ListContainerAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociations") is not None:
        import capo_network_firewall.types.container_associations

        out["container_associations"] = (
            capo_network_firewall.types.container_associations.deserialize_cbor(
                data["ContainerAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
