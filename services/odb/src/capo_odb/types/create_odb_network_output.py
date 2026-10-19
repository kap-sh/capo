"""Generated from Smithy shape ``com.amazonaws.odb#CreateOdbNetworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class CreateOdbNetworkOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the ODB network.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the ODB network.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the ODB network.</p>"""
    odb_network_id: "str"
    """<p>The unique identifier of the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOdbNetworkOutput) -> dict:
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
    out["odbNetworkId"] = value["odb_network_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOdbNetworkOutput:
    out: CreateOdbNetworkOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    return out
