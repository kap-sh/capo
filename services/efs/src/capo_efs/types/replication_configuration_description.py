"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.aws_account_id
    import capo_efs.types.destinations
    import capo_efs.types.file_system_arn
    import capo_efs.types.file_system_id
    import capo_efs.types.region_name
    import capo_efs.types.timestamp


class ReplicationConfigurationDescription(TypedDict, closed=True):
    source_file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the source Amazon EFS file system that is being replicated.</p>"""
    source_file_system_region: "capo_efs.types.region_name.RegionName"
    """<p>The Amazon Web Services Region in which the source EFS file system is located.</p>"""
    source_file_system_arn: "capo_efs.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the current source file system in the replication configuration.</p>"""
    original_source_file_system_arn: "capo_efs.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the original source EFS file system in the replication configuration.</p>"""
    creation_time: "capo_efs.types.timestamp.Timestamp"
    """<p>Describes when the replication configuration was created.</p>"""
    destinations: "capo_efs.types.destinations.Destinations"
    """<p>An array of destination objects. Only one destination object is supported.</p>"""
    source_file_system_owner_id: NotRequired[
        "capo_efs.types.aws_account_id.AwsAccountId"
    ]
    """<p>ID of the Amazon Web Services account in which the source file system resides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationDescription) -> dict:
    out: dict = {}
    out["SourceFileSystemId"] = value["source_file_system_id"]
    out["SourceFileSystemRegion"] = value["source_file_system_region"]
    out["SourceFileSystemArn"] = value["source_file_system_arn"]
    out["OriginalSourceFileSystemArn"] = value["original_source_file_system_arn"]
    import capo_efs.types.timestamp

    out["CreationTime"] = capo_efs.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_efs.types.destinations

    out["Destinations"] = capo_efs.types.destinations.serialize_json(
        value["destinations"]
    )
    if "source_file_system_owner_id" in value:
        out["SourceFileSystemOwnerId"] = value["source_file_system_owner_id"]
    return out


def deserialize_json(data: dict) -> ReplicationConfigurationDescription:
    out: ReplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("SourceFileSystemId") is not None:
        out["source_file_system_id"] = data["SourceFileSystemId"]
    else:
        out["source_file_system_id"] = ""
    if data.get("SourceFileSystemRegion") is not None:
        out["source_file_system_region"] = data["SourceFileSystemRegion"]
    else:
        out["source_file_system_region"] = ""
    if data.get("SourceFileSystemArn") is not None:
        out["source_file_system_arn"] = data["SourceFileSystemArn"]
    else:
        out["source_file_system_arn"] = ""
    if data.get("OriginalSourceFileSystemArn") is not None:
        out["original_source_file_system_arn"] = data["OriginalSourceFileSystemArn"]
    else:
        out["original_source_file_system_arn"] = ""
    if data.get("CreationTime") is not None:
        import capo_efs.types.timestamp

        out["creation_time"] = capo_efs.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Destinations") is not None:
        import capo_efs.types.destinations

        out["destinations"] = capo_efs.types.destinations.deserialize_json(
            data["Destinations"]
        )
    else:
        out["destinations"] = []
    if data.get("SourceFileSystemOwnerId") is not None:
        out["source_file_system_owner_id"] = data["SourceFileSystemOwnerId"]
    return out
