"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_failure_code
    import capo_s3tables.types.migration_failure_detail


class MigrationFailureReason(TypedDict, closed=True):
    code: "capo_s3tables.types.migration_failure_code.MigrationFailureCode"
    """<p>The failure code. It names the cause or the report that lists the findings. Valid values:</p> <ul> <li> <p> <code>rolePermissions</code> - S3 Tables couldn't assume the migration role, or the role doesn't have a permission that the migration needs. <code>detail</code> is the role ARN.</p> </li> <li> <p> <code>sourcePermissions</code> - The migration role couldn't read the Amazon Web Services Glue table or the source objects. <code>detail</code> names the table (<code>database.table</code>) or the source bucket.</p> </li> <li> <p> <code>destinationPermissions</code> - The migration role couldn't write to the table bucket or the report bucket. <code>detail</code> names the bucket.</p> </li> <li> <p> <code>resourceNotFound</code> - A resource that you specified doesn't exist, such as the Amazon Web Services Glue table or the source bucket. <code>detail</code> names it.</p> </li> <li> <p> <code>sourceNotSupported</code> - The source table can't be migrated, for example because it is empty, has too many objects, or has columns or partitions that can't be migrated. The table compatibility report lists the findings.</p> </li> <li> <p> <code>tableCompatibilityReport</code> - The migration couldn't create the destination table, for example because a table with that name already exists or the KMS key can't be used. For a sync, the destination table changed after the previous migration. The table compatibility report lists the finding.</p> </li> <li> <p> <code>objectCompatibilityReport</code> - Some source objects can't be migrated, for example because they are archived, or because they were overwritten after an earlier migration migrated them. The object compatibility report lists them.</p> </li> <li> <p> <code>objectMigrationReport</code> - Some source objects failed to migrate. The object migration report lists them and the cause for each.</p> </li> <li> <p> <code>reportBucketNotSupported</code> - The report bucket can't receive the migration's reports, for example because it is in a different Region than the table bucket.</p> </li> <li> <p> <code>internalError</code> - S3 Tables encountered an internal error. Retry the migration, and contact Amazon Web Services Support if the error persists.</p> </li> </ul>"""
    detail: NotRequired[
        "capo_s3tables.types.migration_failure_detail.MigrationFailureDetail"
    ]
    """<p>The resource that the failure applies to, such as the role ARN, the Amazon Web Services Glue table (<code>database.table</code>) or a bucket. For <code>sourceNotSupported</code>, the reason that the source isn't supported, such as <code>EMPTY_TABLE</code>. This value isn't returned for the report codes or for <code>internalError</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationFailureReason) -> dict:
    out: dict = {}
    import capo_s3tables.types.migration_failure_code

    out["code"] = capo_s3tables.types.migration_failure_code.serialize_json(
        value["code"]
    )
    if "detail" in value:
        out["detail"] = value["detail"]
    return out


def deserialize_json(data: dict) -> MigrationFailureReason:
    out: MigrationFailureReason = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_s3tables.types.migration_failure_code

        out["code"] = capo_s3tables.types.migration_failure_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_s3tables.types.migration_failure_code.MigrationFailureCode", ""
        )
    if data.get("detail") is not None:
        out["detail"] = data["detail"]
    return out
