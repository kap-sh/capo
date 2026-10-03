"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFabricAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.edition
    import capo_managedblockchain.types.string


class NetworkFabricAttributes(TypedDict, closed=True):
    ordering_service_endpoint: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The endpoint of the ordering service for the network.</p>"""
    edition: NotRequired["capo_managedblockchain.types.edition.Edition"]
    """<p>The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more information, see <a href="http://aws.amazon.com/managed-blockchain/pricing/">Amazon Managed Blockchain Pricing</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFabricAttributes) -> dict:
    out: dict = {}
    if "ordering_service_endpoint" in value:
        out["OrderingServiceEndpoint"] = value["ordering_service_endpoint"]
    if "edition" in value:
        import capo_managedblockchain.types.edition

        out["Edition"] = capo_managedblockchain.types.edition.serialize_json(
            value["edition"]
        )
    return out


def deserialize_json(data: dict) -> NetworkFabricAttributes:
    out: NetworkFabricAttributes = {}  # type: ignore[typeddict-item]
    if data.get("OrderingServiceEndpoint") is not None:
        out["ordering_service_endpoint"] = data["OrderingServiceEndpoint"]
    if data.get("Edition") is not None:
        import capo_managedblockchain.types.edition

        out["edition"] = capo_managedblockchain.types.edition.deserialize_json(
            data["Edition"]
        )
    return out
