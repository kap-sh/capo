"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.backup_creation_time_filter
    import capo_backupsearch.types.recovery_point_arn_list
    import capo_backupsearch.types.resource_arn_list
    import capo_backupsearch.types.resource_type_list
    import capo_backupsearch.types.tag_map


class SearchScope(TypedDict, closed=True):
    backup_resource_types: "capo_backupsearch.types.resource_type_list.ResourceTypeList"
    """<p>The resource types included in a search.</p> <p>Eligible resource types include S3 and EBS.</p>"""
    backup_resource_creation_time: NotRequired[
        "capo_backupsearch.types.backup_creation_time_filter.BackupCreationTimeFilter"
    ]
    """<p>This is the time a backup resource was created.</p>"""
    source_resource_arns: NotRequired[
        "capo_backupsearch.types.resource_arn_list.ResourceArnList"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the source resources.</p>"""
    backup_resource_arns: NotRequired[
        "capo_backupsearch.types.recovery_point_arn_list.RecoveryPointArnList"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the backup resources.</p>"""
    backup_resource_tags: NotRequired["capo_backupsearch.types.tag_map.TagMap"]
    """<p>These are one or more tags on the backup (recovery point).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchScope) -> dict:
    out: dict = {}
    import capo_backupsearch.types.resource_type_list

    out["BackupResourceTypes"] = (
        capo_backupsearch.types.resource_type_list.serialize_json(
            value["backup_resource_types"]
        )
    )
    if "backup_resource_creation_time" in value:
        import capo_backupsearch.types.backup_creation_time_filter

        out["BackupResourceCreationTime"] = (
            capo_backupsearch.types.backup_creation_time_filter.serialize_json(
                value["backup_resource_creation_time"]
            )
        )
    if "source_resource_arns" in value:
        import capo_backupsearch.types.resource_arn_list

        out["SourceResourceArns"] = (
            capo_backupsearch.types.resource_arn_list.serialize_json(
                value["source_resource_arns"]
            )
        )
    if "backup_resource_arns" in value:
        import capo_backupsearch.types.recovery_point_arn_list

        out["BackupResourceArns"] = (
            capo_backupsearch.types.recovery_point_arn_list.serialize_json(
                value["backup_resource_arns"]
            )
        )
    if "backup_resource_tags" in value:
        import capo_backupsearch.types.tag_map

        out["BackupResourceTags"] = capo_backupsearch.types.tag_map.serialize_json(
            value["backup_resource_tags"]
        )
    return out


def deserialize_json(data: dict) -> SearchScope:
    out: SearchScope = {}  # type: ignore[typeddict-item]
    if data.get("BackupResourceTypes") is not None:
        import capo_backupsearch.types.resource_type_list

        out["backup_resource_types"] = (
            capo_backupsearch.types.resource_type_list.deserialize_json(
                data["BackupResourceTypes"]
            )
        )
    else:
        out["backup_resource_types"] = []
    if data.get("BackupResourceCreationTime") is not None:
        import capo_backupsearch.types.backup_creation_time_filter

        out["backup_resource_creation_time"] = (
            capo_backupsearch.types.backup_creation_time_filter.deserialize_json(
                data["BackupResourceCreationTime"]
            )
        )
    if data.get("SourceResourceArns") is not None:
        import capo_backupsearch.types.resource_arn_list

        out["source_resource_arns"] = (
            capo_backupsearch.types.resource_arn_list.deserialize_json(
                data["SourceResourceArns"]
            )
        )
    if data.get("BackupResourceArns") is not None:
        import capo_backupsearch.types.recovery_point_arn_list

        out["backup_resource_arns"] = (
            capo_backupsearch.types.recovery_point_arn_list.deserialize_json(
                data["BackupResourceArns"]
            )
        )
    if data.get("BackupResourceTags") is not None:
        import capo_backupsearch.types.tag_map

        out["backup_resource_tags"] = capo_backupsearch.types.tag_map.deserialize_json(
            data["BackupResourceTags"]
        )
    return out
