"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudExadataInfrastructureStorageCapacityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class UpdateCloudExadataInfrastructureStorageCapacityInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier or Amazon Resource Name (ARN) of the Exadata infrastructure to update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateCloudExadataInfrastructureStorageCapacityInput,
) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateCloudExadataInfrastructureStorageCapacityInput:
    out: UpdateCloudExadataInfrastructureStorageCapacityInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        out["cloud_exadata_infrastructure_id"] = ""
    return out
