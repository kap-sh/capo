"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_requested_state
    import capo_s3tables.types.table_arn


class UpdateTableMigrationRequest(TypedDict, closed=True):
    table_arn: NotRequired["capo_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the destination table. Updates the table's most recent migration. Until the migration creates the destination table, specify <code>migrationId</code>. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>"""
    migration_id: NotRequired["capo_s3tables.types.migration_id.MigrationId"]
    """<p>The ID of the migration to update. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>"""
    requested_state: (
        "capo_s3tables.types.migration_requested_state.MigrationRequestedState"
    )
    """<p>The state to move the migration to: <code>queued</code> to continue a migration in the <code>pendingReview</code> state, or <code>cancelled</code> to cancel a migration in the <code>new</code>, <code>planning</code>, <code>pendingReview</code>, <code>queued</code> or <code>migrating</code> state.</p>"""
    update_description: NotRequired["str"]
    """<p>A description of the update, up to 1,024 characters, with no control characters. <code>GetTableMigration</code> doesn't return it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMigrationRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.migration_requested_state

    out["requestedState"] = (
        capo_s3tables.types.migration_requested_state.serialize_json(
            value["requested_state"]
        )
    )
    if "update_description" in value:
        out["updateDescription"] = value["update_description"]
    return out


def deserialize_json(data: dict) -> UpdateTableMigrationRequest:
    out: UpdateTableMigrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("requestedState") is not None:
        import capo_s3tables.types.migration_requested_state

        out["requested_state"] = (
            capo_s3tables.types.migration_requested_state.deserialize_json(
                data["requestedState"]
            )
        )
    else:
        import typing

        out["requested_state"] = typing.cast(
            "capo_s3tables.types.migration_requested_state.MigrationRequestedState", ""
        )
    if data.get("updateDescription") is not None:
        out["update_description"] = data["updateDescription"]
    return out
