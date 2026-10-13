"""Generated from Smithy shape ``com.amazonaws.ssm#Node``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.node_capture_time
    import capo_ssm.types.node_id
    import capo_ssm.types.node_owner_info
    import capo_ssm.types.node_region
    import capo_ssm.types.node_type


class Node(TypedDict, closed=True):
    capture_time: NotRequired["capo_ssm.types.node_capture_time.NodeCaptureTime"]
    """<p>The UTC timestamp for when the managed node data was last captured.</p>"""
    id: NotRequired["capo_ssm.types.node_id.NodeId"]
    """<p>The ID of the managed node.</p>"""
    owner: NotRequired["capo_ssm.types.node_owner_info.NodeOwnerInfo"]
    """<p>Information about the ownership of the managed node.</p>"""
    region: NotRequired["capo_ssm.types.node_region.NodeRegion"]
    """<p>The Amazon Web Services Region that a managed node was created in or assigned to.</p>"""
    node_type: NotRequired["capo_ssm.types.node_type.NodeType"]
    """<p>Information about the type of node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "capture_time" in value:
        import capo_ssm.types.node_capture_time

        out["CaptureTime"] = capo_ssm.types.node_capture_time.serialize_aws_json_1_1(
            value["capture_time"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "owner" in value:
        import capo_ssm.types.node_owner_info

        out["Owner"] = capo_ssm.types.node_owner_info.serialize_aws_json_1_1(
            value["owner"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "node_type" in value:
        import capo_ssm.types.node_type

        out["NodeType"] = capo_ssm.types.node_type.serialize_aws_json_1_1(
            value["node_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("CaptureTime") is not None:
        import capo_ssm.types.node_capture_time

        out["capture_time"] = capo_ssm.types.node_capture_time.deserialize_aws_json_1_1(
            data["CaptureTime"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Owner") is not None:
        import capo_ssm.types.node_owner_info

        out["owner"] = capo_ssm.types.node_owner_info.deserialize_aws_json_1_1(
            data["Owner"]
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("NodeType") is not None:
        import capo_ssm.types.node_type

        out["node_type"] = capo_ssm.types.node_type.deserialize_aws_json_1_1(
            data["NodeType"]
        )
    return out


def redact_sensitive(value: Node) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "node_type" in value:
        import capo_ssm.types.node_type

        out["node_type"] = capo_ssm.types.node_type.redact_sensitive(value["node_type"])
    return out
