"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudExadataInfrastructuresOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.cloud_exadata_infrastructure_list


class ListCloudExadataInfrastructuresOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    cloud_exadata_infrastructures: "capo_odb.types.cloud_exadata_infrastructure_list.CloudExadataInfrastructureList"
    """<p>The list of Exadata infrastructures along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudExadataInfrastructuresOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.cloud_exadata_infrastructure_list

    out["cloudExadataInfrastructures"] = (
        capo_odb.types.cloud_exadata_infrastructure_list.serialize_aws_json_1_0(
            value["cloud_exadata_infrastructures"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudExadataInfrastructuresOutput:
    out: ListCloudExadataInfrastructuresOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudExadataInfrastructures") is not None:
        import capo_odb.types.cloud_exadata_infrastructure_list

        out["cloud_exadata_infrastructures"] = (
            capo_odb.types.cloud_exadata_infrastructure_list.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructures"]
            )
        )
    else:
        raise DeserializationError(
            "ListCloudExadataInfrastructuresOutput.cloud_exadata_infrastructures required"
        )
    return out


def redact_sensitive(value: ListCloudExadataInfrastructuresOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cloud_exadata_infrastructures" in value:
        import capo_odb.types.cloud_exadata_infrastructure_list

        out["cloud_exadata_infrastructures"] = (
            capo_odb.types.cloud_exadata_infrastructure_list.redact_sensitive(
                value["cloud_exadata_infrastructures"]
            )
        )
    return out
