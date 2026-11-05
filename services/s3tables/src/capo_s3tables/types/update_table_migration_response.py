"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_state
    import capo_s3tables.types.table_arn


class UpdateTableMigrationResponse(TypedDict, closed=True):
    migration_id: "capo_s3tables.types.migration_id.MigrationId"
    """<p>The ID of the migration.</p>"""
    state: "capo_s3tables.types.migration_state.MigrationState"
    """<p>The state of the migration after the update, such as <code>queued</code>, <code>migrating</code> or <code>cancelling</code>.</p>"""
    table_arn: NotRequired["capo_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMigrationResponse) -> dict:
    out: dict = {}
    out["migrationId"] = value["migration_id"]
    import capo_s3tables.types.migration_state

    out["state"] = capo_s3tables.types.migration_state.serialize_json(value["state"])
    if "table_arn" in value:
        out["tableARN"] = value["table_arn"]
    return out


def deserialize_json(data: dict) -> UpdateTableMigrationResponse:
    out: UpdateTableMigrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("migrationId") is not None:
        out["migration_id"] = data["migrationId"]
    else:
        out["migration_id"] = ""
    if data.get("state") is not None:
        import capo_s3tables.types.migration_state

        out["state"] = capo_s3tables.types.migration_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_s3tables.types.migration_state.MigrationState", ""
        )
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    return out
