"""Generated from Smithy shape ``com.amazonaws.memorydb#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.endpoint
    import capo_memorydb.types.string
    import capo_memorydb.types.t_stamp


class Node(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The node identifier. A node name is a numeric identifier (0001, 0002, etc.). The combination of cluster name, shard name and node name uniquely identifies every node used in a customer's Amazon account.</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the service update on the node</p>"""
    availability_zone: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Availability Zone in which the node resides</p>"""
    create_time: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time when the node was created.</p>"""
    endpoint: NotRequired["capo_memorydb.types.endpoint.Endpoint"]
    """<p>The hostname for connecting to this node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "create_time" in value:
        import capo_memorydb.types.t_stamp

        out["CreateTime"] = capo_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "endpoint" in value:
        import capo_memorydb.types.endpoint

        out["Endpoint"] = capo_memorydb.types.endpoint.serialize_aws_json_1_1(
            value["endpoint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("CreateTime") is not None:
        import capo_memorydb.types.t_stamp

        out["create_time"] = capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("Endpoint") is not None:
        import capo_memorydb.types.endpoint

        out["endpoint"] = capo_memorydb.types.endpoint.deserialize_aws_json_1_1(
            data["Endpoint"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Node) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "create_time" in value:
        import capo_memorydb.types.t_stamp

        out["CreateTime"] = capo_memorydb.types.t_stamp.serialize_cbor(
            value["create_time"]
        )
    if "endpoint" in value:
        import capo_memorydb.types.endpoint

        out["Endpoint"] = capo_memorydb.types.endpoint.serialize_cbor(value["endpoint"])
    return out


def deserialize_cbor(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("CreateTime") is not None:
        import capo_memorydb.types.t_stamp

        out["create_time"] = capo_memorydb.types.t_stamp.deserialize_cbor(
            data["CreateTime"]
        )
    if data.get("Endpoint") is not None:
        import capo_memorydb.types.endpoint

        out["endpoint"] = capo_memorydb.types.endpoint.deserialize_cbor(
            data["Endpoint"]
        )
    return out
