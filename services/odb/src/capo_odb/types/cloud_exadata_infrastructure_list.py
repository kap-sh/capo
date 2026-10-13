"""Generated from Smithy shape ``com.amazonaws.odb#CloudExadataInfrastructureList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.cloud_exadata_infrastructure_summary

CloudExadataInfrastructureList: TypeAlias = list[
    "capo_odb.types.cloud_exadata_infrastructure_summary.CloudExadataInfrastructureSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudExadataInfrastructureList) -> list:
    import capo_odb.types.cloud_exadata_infrastructure_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.cloud_exadata_infrastructure_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CloudExadataInfrastructureList:
    import capo_odb.types.cloud_exadata_infrastructure_summary

    out: CloudExadataInfrastructureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.cloud_exadata_infrastructure_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: CloudExadataInfrastructureList) -> list[Any]:
    import capo_odb.types.cloud_exadata_infrastructure_summary

    return [
        capo_odb.types.cloud_exadata_infrastructure_summary.redact_sensitive(item)
        for item in value
    ]
