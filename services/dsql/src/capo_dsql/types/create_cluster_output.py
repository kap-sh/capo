"""Generated from Smithy shape ``com.amazonaws.dsql#CreateClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_arn
    import capo_dsql.types.cluster_creation_time
    import capo_dsql.types.cluster_id
    import capo_dsql.types.cluster_status
    import capo_dsql.types.deletion_protection_enabled
    import capo_dsql.types.encryption_details
    import capo_dsql.types.endpoint
    import capo_dsql.types.multi_region_properties


class CreateClusterOutput(TypedDict, closed=True):
    identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the created cluster.</p>"""
    arn: "capo_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the created cluster.</p>"""
    status: "capo_dsql.types.cluster_status.ClusterStatus"
    """<p>The status of the created cluster.</p>"""
    creation_time: "capo_dsql.types.cluster_creation_time.ClusterCreationTime"
    """<p>The time of when created the cluster.</p>"""
    multi_region_properties: NotRequired[
        "capo_dsql.types.multi_region_properties.MultiRegionProperties"
    ]
    """<p>The multi-Region cluster configuration details that were set during cluster creation</p>"""
    encryption_details: NotRequired[
        "capo_dsql.types.encryption_details.EncryptionDetails"
    ]
    """<p>The encryption configuration for the cluster that was specified during the creation process, including the KMS key identifier and encryption state.</p>"""
    deletion_protection_enabled: (
        "capo_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    )
    """<p>Whether deletion protection is enabled on this cluster.</p>"""
    endpoint: NotRequired["capo_dsql.types.endpoint.Endpoint"]
    """<p>The connection endpoint for the created cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["arn"] = value["arn"]
    import capo_dsql.types.cluster_status

    out["status"] = capo_dsql.types.cluster_status.serialize_json(value["status"])
    import capo_dsql.types.cluster_creation_time

    out["creationTime"] = capo_dsql.types.cluster_creation_time.serialize_json(
        value["creation_time"]
    )
    if "multi_region_properties" in value:
        import capo_dsql.types.multi_region_properties

        out["multiRegionProperties"] = (
            capo_dsql.types.multi_region_properties.serialize_json(
                value["multi_region_properties"]
            )
        )
    if "encryption_details" in value:
        import capo_dsql.types.encryption_details

        out["encryptionDetails"] = capo_dsql.types.encryption_details.serialize_json(
            value["encryption_details"]
        )
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> CreateClusterOutput:
    out: CreateClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_dsql.types.cluster_status

        out["status"] = capo_dsql.types.cluster_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_dsql.types.cluster_status.ClusterStatus", "")
    if data.get("creationTime") is not None:
        import capo_dsql.types.cluster_creation_time

        out["creation_time"] = capo_dsql.types.cluster_creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("multiRegionProperties") is not None:
        import capo_dsql.types.multi_region_properties

        out["multi_region_properties"] = (
            capo_dsql.types.multi_region_properties.deserialize_json(
                data["multiRegionProperties"]
            )
        )
    if data.get("encryptionDetails") is not None:
        import capo_dsql.types.encryption_details

        out["encryption_details"] = capo_dsql.types.encryption_details.deserialize_json(
            data["encryptionDetails"]
        )
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    return out
