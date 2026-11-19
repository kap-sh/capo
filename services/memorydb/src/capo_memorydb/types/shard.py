"""Generated from Smithy shape ``com.amazonaws.memorydb#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.node_list
    import capo_memorydb.types.string


class Shard(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the shard</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The current state of this replication group - creating, available, modifying, deleting.</p>"""
    slots: NotRequired["capo_memorydb.types.string.String"]
    """<p>The keyspace for this shard.</p>"""
    nodes: NotRequired["capo_memorydb.types.node_list.NodeList"]
    """<p>A list containing information about individual nodes within the shard</p>"""
    number_of_nodes: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of nodes in the shard</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Shard) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "slots" in value:
        out["Slots"] = value["slots"]
    if "nodes" in value:
        import capo_memorydb.types.node_list

        out["Nodes"] = capo_memorydb.types.node_list.serialize_aws_json_1_1(
            value["nodes"]
        )
    if "number_of_nodes" in value:
        out["NumberOfNodes"] = value["number_of_nodes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Slots") is not None:
        out["slots"] = data["Slots"]
    if data.get("Nodes") is not None:
        import capo_memorydb.types.node_list

        out["nodes"] = capo_memorydb.types.node_list.deserialize_aws_json_1_1(
            data["Nodes"]
        )
    if data.get("NumberOfNodes") is not None:
        out["number_of_nodes"] = data["NumberOfNodes"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Shard) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "slots" in value:
        out["Slots"] = value["slots"]
    if "nodes" in value:
        import capo_memorydb.types.node_list

        out["Nodes"] = capo_memorydb.types.node_list.serialize_cbor(value["nodes"])
    if "number_of_nodes" in value:
        out["NumberOfNodes"] = value["number_of_nodes"]
    return out


def deserialize_cbor(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Slots") is not None:
        out["slots"] = data["Slots"]
    if data.get("Nodes") is not None:
        import capo_memorydb.types.node_list

        out["nodes"] = capo_memorydb.types.node_list.deserialize_cbor(data["Nodes"])
    if data.get("NumberOfNodes") is not None:
        out["number_of_nodes"] = data["NumberOfNodes"]
    return out
