"""Generated from Smithy shape ``com.amazonaws.dsql#GetClusterOutput``."""

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
    import capo_dsql.types.tag_map


class GetClusterOutput(TypedDict, closed=True):
    identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the retrieved cluster.</p>"""
    arn: "capo_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the retrieved cluster.</p>"""
    status: "capo_dsql.types.cluster_status.ClusterStatus"
    """<p>The status of the retrieved cluster.</p>"""
    creation_time: "capo_dsql.types.cluster_creation_time.ClusterCreationTime"
    """<p>The time of when the cluster was created.</p>"""
    deletion_protection_enabled: (
        "capo_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    )
    """<p>Whether deletion protection is enabled in this cluster.</p>"""
    multi_region_properties: NotRequired[
        "capo_dsql.types.multi_region_properties.MultiRegionProperties"
    ]
    """<p>Returns the current multi-Region cluster configuration, including witness region and linked cluster information.</p>"""
    tags: NotRequired["capo_dsql.types.tag_map.TagMap"]
    encryption_details: NotRequired[
        "capo_dsql.types.encryption_details.EncryptionDetails"
    ]
    """<p>The current encryption configuration details for the cluster.</p>"""
    endpoint: NotRequired["capo_dsql.types.endpoint.Endpoint"]
    """<p>The connection endpoint for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["arn"] = value["arn"]
    import capo_dsql.types.cluster_status

    out["status"] = capo_dsql.types.cluster_status.serialize_json(value["status"])
    import capo_dsql.types.cluster_creation_time

    out["creationTime"] = capo_dsql.types.cluster_creation_time.serialize_json(
        value["creation_time"]
    )
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "multi_region_properties" in value:
        import capo_dsql.types.multi_region_properties

        out["multiRegionProperties"] = (
            capo_dsql.types.multi_region_properties.serialize_json(
                value["multi_region_properties"]
            )
        )
    if "tags" in value:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.serialize_json(value["tags"])
    if "encryption_details" in value:
        import capo_dsql.types.encryption_details

        out["encryptionDetails"] = capo_dsql.types.encryption_details.serialize_json(
            value["encryption_details"]
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> GetClusterOutput:
    out: GetClusterOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("multiRegionProperties") is not None:
        import capo_dsql.types.multi_region_properties

        out["multi_region_properties"] = (
            capo_dsql.types.multi_region_properties.deserialize_json(
                data["multiRegionProperties"]
            )
        )
    if data.get("tags") is not None:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.deserialize_json(data["tags"])
    if data.get("encryptionDetails") is not None:
        import capo_dsql.types.encryption_details

        out["encryption_details"] = capo_dsql.types.encryption_details.deserialize_json(
            data["encryptionDetails"]
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    return out
