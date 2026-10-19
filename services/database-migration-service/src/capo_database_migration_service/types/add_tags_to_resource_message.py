"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AddTagsToResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list


class AddTagsToResourceMessage(TypedDict, closed=True):
    resource_arn: "capo_database_migration_service.types.string.String"
    """<p>Identifies the DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).</p> <p>For DMS, you can tag a replication instance, an endpoint, or a replication task.</p>"""
    tags: "capo_database_migration_service.types.tag_list.TagList"
    """<p>One or more tags to be assigned to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceMessage) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_database_migration_service.types.tag_list

    out["Tags"] = capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceMessage:
    out: AddTagsToResourceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
