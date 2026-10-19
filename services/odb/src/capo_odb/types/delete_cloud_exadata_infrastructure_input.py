"""Generated from Smithy shape ``com.amazonaws.odb#DeleteCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class DeleteCloudExadataInfrastructureInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exadata infrastructure to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCloudExadataInfrastructureInput:
    out: DeleteCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        out["cloud_exadata_infrastructure_id"] = ""
    return out
