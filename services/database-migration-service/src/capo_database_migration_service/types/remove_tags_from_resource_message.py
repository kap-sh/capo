"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RemoveTagsFromResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.key_list
    import capo_database_migration_service.types.string


class RemoveTagsFromResourceMessage(TypedDict, closed=True):
    resource_arn: "capo_database_migration_service.types.string.String"
    """<p>An DMS resource from which you want to remove tag(s). The value for this parameter is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_database_migration_service.types.key_list.KeyList"
    """<p>The tag key (name) of the tag to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceMessage) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_database_migration_service.types.key_list

    out["TagKeys"] = (
        capo_database_migration_service.types.key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceMessage:
    out: RemoveTagsFromResourceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_database_migration_service.types.key_list

        out["tag_keys"] = (
            capo_database_migration_service.types.key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
