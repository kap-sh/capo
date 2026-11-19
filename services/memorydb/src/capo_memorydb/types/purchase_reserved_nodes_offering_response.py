"""Generated from Smithy shape ``com.amazonaws.memorydb#PurchaseReservedNodesOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.reserved_node


class PurchaseReservedNodesOfferingResponse(TypedDict, closed=True):
    reserved_node: NotRequired["capo_memorydb.types.reserved_node.ReservedNode"]
    """<p>Represents the output of a <code>PurchaseReservedNodesOffering</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseReservedNodesOfferingResponse) -> dict:
    out: dict = {}
    if "reserved_node" in value:
        import capo_memorydb.types.reserved_node

        out["ReservedNode"] = capo_memorydb.types.reserved_node.serialize_aws_json_1_1(
            value["reserved_node"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseReservedNodesOfferingResponse:
    out: PurchaseReservedNodesOfferingResponse = {}  # type: ignore[typeddict-item]
    if data.get("ReservedNode") is not None:
        import capo_memorydb.types.reserved_node

        out["reserved_node"] = (
            capo_memorydb.types.reserved_node.deserialize_aws_json_1_1(
                data["ReservedNode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PurchaseReservedNodesOfferingResponse) -> dict:
    out: dict = {}
    if "reserved_node" in value:
        import capo_memorydb.types.reserved_node

        out["ReservedNode"] = capo_memorydb.types.reserved_node.serialize_cbor(
            value["reserved_node"]
        )
    return out


def deserialize_cbor(data: dict) -> PurchaseReservedNodesOfferingResponse:
    out: PurchaseReservedNodesOfferingResponse = {}  # type: ignore[typeddict-item]
    if data.get("ReservedNode") is not None:
        import capo_memorydb.types.reserved_node

        out["reserved_node"] = capo_memorydb.types.reserved_node.deserialize_cbor(
            data["ReservedNode"]
        )
    return out
