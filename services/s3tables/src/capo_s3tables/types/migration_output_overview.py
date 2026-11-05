"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationOutputOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.report_overview
    import capo_s3tables.types.s3_bucket_arn


class MigrationOutputOverview(TypedDict, closed=True):
    bucket: "capo_s3tables.types.s3_bucket_arn.S3BucketARN"
    """<p>The general purpose bucket that the migration writes every report to.</p>"""
    table_compatibility_report: "capo_s3tables.types.report_overview.ReportOverview"
    """<p>The table compatibility report: the sample object that the schema is inferred from, the table-level findings, and one row for each destination column with its type change and how the migration policies apply to it. The migration writes it when planning finishes, before any data migrates. If planning fails, the report might not be written.</p>"""
    object_compatibility_report: "capo_s3tables.types.report_overview.ReportOverview"
    """<p>The object compatibility report: one row for each source object under the source table's location, with whether the migration includes the object and its most severe finding. The migration writes it when planning finishes. If planning fails, the report might not be written.</p>"""
    object_migration_report: "capo_s3tables.types.report_overview.ReportOverview"
    """<p>The object migration report: one row for each source object that the migration tried to migrate, with whether it migrated, how it was transformed, and why it failed. The migration writes it once, when the migration ends. It isn't written if planning fails or if a sync has nothing to migrate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationOutputOverview) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    import capo_s3tables.types.report_overview

    out["tableCompatibilityReport"] = (
        capo_s3tables.types.report_overview.serialize_json(
            value["table_compatibility_report"]
        )
    )
    import capo_s3tables.types.report_overview

    out["objectCompatibilityReport"] = (
        capo_s3tables.types.report_overview.serialize_json(
            value["object_compatibility_report"]
        )
    )
    import capo_s3tables.types.report_overview

    out["objectMigrationReport"] = capo_s3tables.types.report_overview.serialize_json(
        value["object_migration_report"]
    )
    return out


def deserialize_json(data: dict) -> MigrationOutputOverview:
    out: MigrationOutputOverview = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("tableCompatibilityReport") is not None:
        import capo_s3tables.types.report_overview

        out["table_compatibility_report"] = (
            capo_s3tables.types.report_overview.deserialize_json(
                data["tableCompatibilityReport"]
            )
        )
    else:
        raise DeserializationError(
            "MigrationOutputOverview.table_compatibility_report required"
        )
    if data.get("objectCompatibilityReport") is not None:
        import capo_s3tables.types.report_overview

        out["object_compatibility_report"] = (
            capo_s3tables.types.report_overview.deserialize_json(
                data["objectCompatibilityReport"]
            )
        )
    else:
        raise DeserializationError(
            "MigrationOutputOverview.object_compatibility_report required"
        )
    if data.get("objectMigrationReport") is not None:
        import capo_s3tables.types.report_overview

        out["object_migration_report"] = (
            capo_s3tables.types.report_overview.deserialize_json(
                data["objectMigrationReport"]
            )
        )
    else:
        raise DeserializationError(
            "MigrationOutputOverview.object_migration_report required"
        )
    return out
