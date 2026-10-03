"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.access_point_metadata_map
    import capo_backup.types.access_point_name
    import capo_backup.types.access_point_policy
    import capo_backup.types.recovery_point_arn
    import capo_backup.types.tag_map


class CreateBackupAccessPointRequest(TypedDict, closed=True):
    access_point_metadata: NotRequired[
        "capo_backup.types.access_point_metadata_map.AccessPointMetadataMap"
    ]
    """<p>Metadata for the backup access point. For continuous (point-in-time) recovery points, you must include an <code>AccessPointInTime</code> timestamp (in format <code>2021-11-27T03:30:27Z</code>). The access point provides access to the content present in the backup at that specific time. You can specify any time within the continuous backup's retention period, up to the latest restorable time. For snapshot recovery points, do not include <code>AccessPointInTime</code>.</p>"""
    access_point_policy: NotRequired[
        "capo_backup.types.access_point_policy.AccessPointPolicy"
    ]
    """<p>An optional resource-based policy, in JSON format, to apply to the underlying Amazon S3 access point. The policy controls how backup data can be accessed through the access point. If you do not specify a policy, access is governed by the caller's IAM permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html">Configuring IAM policies for using access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    name: "capo_backup.types.access_point_name.AccessPointName"
    """<p>The name of the backup access point. This name is shared with the Amazon S3 access point namespace. It must be unique within your account and Region and cannot conflict with an existing Amazon S3 access point. For more information about access point naming, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.html">Access points naming rules, restrictions, and limitations</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn"
    """<p>The Amazon Resource Name (ARN) of the recovery point for which to create the backup access point. The recovery point must be an Amazon S3 recovery point in the <code>AVAILABLE</code>, <code>STOPPED</code>, or <code>COMPLETED</code> state.</p>"""
    tags: NotRequired["capo_backup.types.tag_map.TagMap"]
    """<p>The tags to assign to the backup access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupAccessPointRequest) -> dict:
    out: dict = {}
    if "access_point_metadata" in value:
        import capo_backup.types.access_point_metadata_map

        out["AccessPointMetadata"] = (
            capo_backup.types.access_point_metadata_map.serialize_json(
                value["access_point_metadata"]
            )
        )
    if "access_point_policy" in value:
        out["AccessPointPolicy"] = value["access_point_policy"]
    out["Name"] = value["name"]
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "tags" in value:
        import capo_backup.types.tag_map

        out["Tags"] = capo_backup.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBackupAccessPointRequest:
    out: CreateBackupAccessPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessPointMetadata") is not None:
        import capo_backup.types.access_point_metadata_map

        out["access_point_metadata"] = (
            capo_backup.types.access_point_metadata_map.deserialize_json(
                data["AccessPointMetadata"]
            )
        )
    if data.get("AccessPointPolicy") is not None:
        out["access_point_policy"] = data["AccessPointPolicy"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateBackupAccessPointRequest.name required")
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        raise DeserializationError(
            "CreateBackupAccessPointRequest.recovery_point_arn required"
        )
    if data.get("Tags") is not None:
        import capo_backup.types.tag_map

        out["tags"] = capo_backup.types.tag_map.deserialize_json(data["Tags"])
    return out
