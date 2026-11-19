"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListContextStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.context_stores
    import capo_network_firewall.types.pagination_token


class ListContextStoresResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    context_stores: "capo_network_firewall.types.context_stores.ContextStores"
    """<p>The context stores that are associated with your firewalls.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContextStoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_network_firewall.types.context_stores

    out["ContextStores"] = (
        capo_network_firewall.types.context_stores.serialize_aws_json_1_0(
            value["context_stores"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContextStoresResponse:
    out: ListContextStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ContextStores") is not None:
        import capo_network_firewall.types.context_stores

        out["context_stores"] = (
            capo_network_firewall.types.context_stores.deserialize_aws_json_1_0(
                data["ContextStores"]
            )
        )
    else:
        out["context_stores"] = []
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListContextStoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_network_firewall.types.context_stores

    out["ContextStores"] = capo_network_firewall.types.context_stores.serialize_cbor(
        value["context_stores"]
    )
    return out


def deserialize_cbor(data: dict) -> ListContextStoresResponse:
    out: ListContextStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ContextStores") is not None:
        import capo_network_firewall.types.context_stores

        out["context_stores"] = (
            capo_network_firewall.types.context_stores.deserialize_cbor(
                data["ContextStores"]
            )
        )
    else:
        out["context_stores"] = []
    return out
