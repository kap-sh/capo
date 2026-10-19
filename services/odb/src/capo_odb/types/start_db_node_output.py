"""Generated from Smithy shape ``com.amazonaws.odb#StartDbNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_node_resource_status


class StartDbNodeOutput(TypedDict, closed=True):
    db_node_id: "str"
    """<p>The unique identifier of the DB node that was started.</p>"""
    status: NotRequired["capo_odb.types.db_node_resource_status.DbNodeResourceStatus"]
    """<p>The current status of the DB node after the start operation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the DB node after the start operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDbNodeOutput) -> dict:
    out: dict = {}
    out["dbNodeId"] = value["db_node_id"]
    if "status" in value:
        import capo_odb.types.db_node_resource_status

        out["status"] = capo_odb.types.db_node_resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDbNodeOutput:
    out: StartDbNodeOutput = {}  # type: ignore[typeddict-item]
    if data.get("dbNodeId") is not None:
        out["db_node_id"] = data["dbNodeId"]
    else:
        out["db_node_id"] = ""
    if data.get("status") is not None:
        import capo_odb.types.db_node_resource_status

        out["status"] = capo_odb.types.db_node_resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
