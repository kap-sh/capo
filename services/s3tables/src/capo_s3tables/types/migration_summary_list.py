"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.migration_summary

MigrationSummaryList: TypeAlias = list[
    "capo_s3tables.types.migration_summary.MigrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSummaryList) -> list:
    import capo_s3tables.types.migration_summary

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.migration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MigrationSummaryList:
    import capo_s3tables.types.migration_summary

    out: MigrationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_s3tables.types.migration_summary.deserialize_json(item))
    return out
