"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.maintenance_window
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn


class UpdateCloudExadataInfrastructureInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exadata infrastructure to update.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new user-friendly name for the Exadata infrastructure.</p>"""
    compute_count: NotRequired["int"]
    """<p>The number of database servers for the Exadata infrastructure.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The maintenance window configuration for the Exadata Cloud infrastructure.</p> <p>This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.</p>"""
    storage_count: NotRequired["int"]
    """<p>The number of storage servers to activate for the Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "compute_count" in value:
        out["computeCount"] = value["compute_count"]
    if "maintenance_window" in value:
        import capo_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            capo_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    if "storage_count" in value:
        out["storageCount"] = value["storage_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCloudExadataInfrastructureInput:
    out: UpdateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        out["cloud_exadata_infrastructure_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("computeCount") is not None:
        out["compute_count"] = data["computeCount"]
    if data.get("maintenanceWindow") is not None:
        import capo_odb.types.maintenance_window

        out["maintenance_window"] = (
            capo_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if data.get("storageCount") is not None:
        out["storage_count"] = data["storageCount"]
    return out
