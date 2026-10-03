"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_database_migration_service.types.string.String"]
    r"""<p>A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regular expressions: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").</p>"""
    value: NotRequired["capo_database_migration_service.types.string.String"]
    r"""<p>A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regular expressions: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").</p>"""
    resource_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the resource for which the tag is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out
