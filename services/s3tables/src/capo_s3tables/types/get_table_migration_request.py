"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.table_arn


class GetTableMigrationRequest(TypedDict, closed=True):
    migration_id: NotRequired["capo_s3tables.types.migration_id.MigrationId"]
    """<p>The ID of the migration to get. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>"""
    table_arn: NotRequired["capo_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the destination table. Gets the table's most recent migration. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMigrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableMigrationRequest:
    out: GetTableMigrationRequest = {}  # type: ignore[typeddict-item]
    return out
