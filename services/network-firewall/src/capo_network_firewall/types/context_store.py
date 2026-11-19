"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextStore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.aws_account_id
    import capo_network_firewall.types.context_store_id


class ContextStore(TypedDict, closed=True):
    context_store_id: "capo_network_firewall.types.context_store_id.ContextStoreId"
    """<p>The unique identifier of the context store. Use this value in <code>ListResourcesInContextStore</code> to list the resources that the context store records.</p>"""
    context_store_owner_account_id: (
        "capo_network_firewall.types.aws_account_id.AWSAccountId"
    )
    """<p>The ID of the Amazon Web Services account that owns the context store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextStore) -> dict:
    out: dict = {}
    out["ContextStoreId"] = value["context_store_id"]
    out["ContextStoreOwnerAccountId"] = value["context_store_owner_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextStore:
    out: ContextStore = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreId") is not None:
        out["context_store_id"] = data["ContextStoreId"]
    else:
        out["context_store_id"] = ""
    if data.get("ContextStoreOwnerAccountId") is not None:
        out["context_store_owner_account_id"] = data["ContextStoreOwnerAccountId"]
    else:
        out["context_store_owner_account_id"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContextStore) -> dict:
    out: dict = {}
    out["ContextStoreId"] = value["context_store_id"]
    out["ContextStoreOwnerAccountId"] = value["context_store_owner_account_id"]
    return out


def deserialize_cbor(data: dict) -> ContextStore:
    out: ContextStore = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreId") is not None:
        out["context_store_id"] = data["ContextStoreId"]
    else:
        out["context_store_id"] = ""
    if data.get("ContextStoreOwnerAccountId") is not None:
        out["context_store_owner_account_id"] = data["ContextStoreOwnerAccountId"]
    else:
        out["context_store_owner_account_id"] = ""
    return out
