"""Generated from Smithy shape ``com.amazonaws.odb#CreateOdbPeeringConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class CreateOdbPeeringConnectionOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The display name of the ODB peering connection.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The status of the ODB peering connection.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the ODB peering connection.</p>"""
    odb_peering_connection_id: "str"
    """<p>The unique identifier of the ODB peering connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOdbPeeringConnectionOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["odbPeeringConnectionId"] = value["odb_peering_connection_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOdbPeeringConnectionOutput:
    out: CreateOdbPeeringConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("odbPeeringConnectionId") is not None:
        out["odb_peering_connection_id"] = data["odbPeeringConnectionId"]
    else:
        out["odb_peering_connection_id"] = ""
    return out
