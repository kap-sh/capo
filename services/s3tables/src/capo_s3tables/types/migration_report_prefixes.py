"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationReportPrefixes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_report_prefix


class MigrationReportPrefixes(TypedDict, closed=True):
    table_compatibility_report: NotRequired[
        "capo_s3tables.types.migration_report_prefix.MigrationReportPrefix"
    ]
    """<p>The key prefix for the table compatibility report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.</p>"""
    object_compatibility_report: NotRequired[
        "capo_s3tables.types.migration_report_prefix.MigrationReportPrefix"
    ]
    """<p>The key prefix for the object compatibility report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.</p>"""
    object_migration_report: NotRequired[
        "capo_s3tables.types.migration_report_prefix.MigrationReportPrefix"
    ]
    """<p>The key prefix for the object migration report, up to 512 bytes. If not specified, the report's keys start at the root of the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationReportPrefixes) -> dict:
    out: dict = {}
    if "table_compatibility_report" in value:
        out["tableCompatibilityReport"] = value["table_compatibility_report"]
    if "object_compatibility_report" in value:
        out["objectCompatibilityReport"] = value["object_compatibility_report"]
    if "object_migration_report" in value:
        out["objectMigrationReport"] = value["object_migration_report"]
    return out


def deserialize_json(data: dict) -> MigrationReportPrefixes:
    out: MigrationReportPrefixes = {}  # type: ignore[typeddict-item]
    if data.get("tableCompatibilityReport") is not None:
        out["table_compatibility_report"] = data["tableCompatibilityReport"]
    if data.get("objectCompatibilityReport") is not None:
        out["object_compatibility_report"] = data["objectCompatibilityReport"]
    if data.get("objectMigrationReport") is not None:
        out["object_migration_report"] = data["objectMigrationReport"]
    return out
