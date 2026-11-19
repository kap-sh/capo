"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListResourcesInContextStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.resource_contexts


class ListResourcesInContextStoreResponse(TypedDict, closed=True):
    resource_contexts: "capo_network_firewall.types.resource_contexts.ResourceContexts"
    """<p>The resources that the context store records and that match your filters.</p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourcesInContextStoreResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.resource_contexts

    out["ResourceContexts"] = (
        capo_network_firewall.types.resource_contexts.serialize_aws_json_1_0(
            value["resource_contexts"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourcesInContextStoreResponse:
    out: ListResourcesInContextStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceContexts") is not None:
        import capo_network_firewall.types.resource_contexts

        out["resource_contexts"] = (
            capo_network_firewall.types.resource_contexts.deserialize_aws_json_1_0(
                data["ResourceContexts"]
            )
        )
    else:
        out["resource_contexts"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListResourcesInContextStoreResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.resource_contexts

    out["ResourceContexts"] = (
        capo_network_firewall.types.resource_contexts.serialize_cbor(
            value["resource_contexts"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListResourcesInContextStoreResponse:
    out: ListResourcesInContextStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceContexts") is not None:
        import capo_network_firewall.types.resource_contexts

        out["resource_contexts"] = (
            capo_network_firewall.types.resource_contexts.deserialize_cbor(
                data["ResourceContexts"]
            )
        )
    else:
        out["resource_contexts"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
