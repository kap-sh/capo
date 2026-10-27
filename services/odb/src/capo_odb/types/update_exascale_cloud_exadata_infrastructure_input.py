"""Generated from Smithy shape ``com.amazonaws.odb#UpdateExascaleCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class UpdateExascaleCloudExadataInfrastructureInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier or Amazon Resource Name (ARN) of the Exadata infrastructure to update.</p>"""
    total_storage_size_in_g_bs: "int"
    """<p>The total amount of Exascale storage, in gigabytes (GB), to configure on the Exadata infrastructure.</p>"""
    total_vm_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of Exascale storage, in gigabytes (GB), to allocate for VM storage on the Exadata infrastructure. VM clusters that store their VM file systems or VM backups in Exascale storage use this capacity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateExascaleCloudExadataInfrastructureInput,
) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    out["totalStorageSizeInGBs"] = value["total_storage_size_in_g_bs"]
    if "total_vm_storage_size_in_g_bs" in value:
        out["totalVmStorageSizeInGBs"] = value["total_vm_storage_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateExascaleCloudExadataInfrastructureInput:
    out: UpdateExascaleCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        out["cloud_exadata_infrastructure_id"] = ""
    if data.get("totalStorageSizeInGBs") is not None:
        out["total_storage_size_in_g_bs"] = data["totalStorageSizeInGBs"]
    else:
        out["total_storage_size_in_g_bs"] = 0
    if data.get("totalVmStorageSizeInGBs") is not None:
        out["total_vm_storage_size_in_g_bs"] = data["totalVmStorageSizeInGBs"]
    return out
