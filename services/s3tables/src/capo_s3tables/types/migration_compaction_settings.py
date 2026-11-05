"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationCompactionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_compaction_strategy
    import capo_s3tables.types.migration_target_file_size_mb


class MigrationCompactionSettings(TypedDict, closed=True):
    target_file_size_mb: (
        "capo_s3tables.types.migration_target_file_size_mb.MigrationTargetFileSizeMB"
    )
    """<p>The target size, from 64 to 512 MB, of the data files that the migration writes, and of the files that compaction writes after you complete the migration. The default is 512.</p>"""
    strategy: (
        "capo_s3tables.types.iceberg_compaction_strategy.IcebergCompactionStrategy"
    )
    """<p>The compaction strategy. The only valid value is <code>binpack</code>, which is the default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationCompactionSettings) -> dict:
    out: dict = {}
    out["targetFileSizeMB"] = value.get("target_file_size_mb", 512)
    import capo_s3tables.types.iceberg_compaction_strategy

    out["strategy"] = capo_s3tables.types.iceberg_compaction_strategy.serialize_json(
        value.get("strategy", "binpack")
    )
    return out


def deserialize_json(data: dict) -> MigrationCompactionSettings:
    out: MigrationCompactionSettings = {}  # type: ignore[typeddict-item]
    if data.get("targetFileSizeMB") is not None:
        out["target_file_size_mb"] = data["targetFileSizeMB"]
    else:
        out["target_file_size_mb"] = 512
    if data.get("strategy") is not None:
        import capo_s3tables.types.iceberg_compaction_strategy

        out["strategy"] = (
            capo_s3tables.types.iceberg_compaction_strategy.deserialize_json(
                data["strategy"]
            )
        )
    else:
        out["strategy"] = "binpack"
    return out
