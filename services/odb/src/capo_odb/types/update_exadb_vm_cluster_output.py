"""Generated from Smithy shape ``com.amazonaws.odb#UpdateExadbVmClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class UpdateExadbVmClusterOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the Exascale VM cluster.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exascale VM cluster.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exascale VM cluster.</p>"""
    exadb_vm_cluster_id: "str"
    """<p>The unique identifier of the Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateExadbVmClusterOutput) -> dict:
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
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateExadbVmClusterOutput:
    out: UpdateExadbVmClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    return out
