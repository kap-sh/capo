"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_report_prefixes
    import capo_s3tables.types.s3_bucket_arn


class MigrationOutputConfiguration(TypedDict, closed=True):
    bucket: "capo_s3tables.types.s3_bucket_arn.S3BucketARN"
    """<p>The general purpose bucket that the migration writes every report to.</p>"""
    prefixes: NotRequired[
        "capo_s3tables.types.migration_report_prefixes.MigrationReportPrefixes"
    ]
    """<p>The key prefix for each report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationOutputConfiguration) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "prefixes" in value:
        import capo_s3tables.types.migration_report_prefixes

        out["prefixes"] = capo_s3tables.types.migration_report_prefixes.serialize_json(
            value["prefixes"]
        )
    return out


def deserialize_json(data: dict) -> MigrationOutputConfiguration:
    out: MigrationOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("prefixes") is not None:
        import capo_s3tables.types.migration_report_prefixes

        out["prefixes"] = (
            capo_s3tables.types.migration_report_prefixes.deserialize_json(
                data["prefixes"]
            )
        )
    return out
