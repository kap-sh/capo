"""Generated from Smithy shape ``com.amazonaws.s3tables#CompleteTableMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn


class CompleteTableMigrationRequest(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the migrated table to complete the migration of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteTableMigrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CompleteTableMigrationRequest:
    out: CompleteTableMigrationRequest = {}  # type: ignore[typeddict-item]
    return out
