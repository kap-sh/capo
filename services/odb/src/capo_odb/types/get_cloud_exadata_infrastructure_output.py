"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_exadata_infrastructure


class GetCloudExadataInfrastructureOutput(TypedDict, closed=True):
    cloud_exadata_infrastructure: NotRequired[
        "capo_odb.types.cloud_exadata_infrastructure.CloudExadataInfrastructure"
    ]
    """<p>The Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudExadataInfrastructureOutput) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure" in value:
        import capo_odb.types.cloud_exadata_infrastructure

        out["cloudExadataInfrastructure"] = (
            capo_odb.types.cloud_exadata_infrastructure.serialize_aws_json_1_0(
                value["cloud_exadata_infrastructure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudExadataInfrastructureOutput:
    out: GetCloudExadataInfrastructureOutput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructure") is not None:
        import capo_odb.types.cloud_exadata_infrastructure

        out["cloud_exadata_infrastructure"] = (
            capo_odb.types.cloud_exadata_infrastructure.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructure"]
            )
        )
    return out


def redact_sensitive(value: GetCloudExadataInfrastructureOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cloud_exadata_infrastructure" in value:
        import capo_odb.types.cloud_exadata_infrastructure

        out["cloud_exadata_infrastructure"] = (
            capo_odb.types.cloud_exadata_infrastructure.redact_sensitive(
                value["cloud_exadata_infrastructure"]
            )
        )
    return out
