"""Generated from Smithy shape ``com.amazonaws.s3tables#StartTableMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_state


class StartTableMigrationResponse(TypedDict, closed=True):
    migration_id: "capo_s3tables.types.migration_id.MigrationId"
    """<p>The ID of the migration.</p>"""
    state: "capo_s3tables.types.migration_state.MigrationState"
    """<p>The state of the migration when the request is accepted, such as <code>planning</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTableMigrationResponse) -> dict:
    out: dict = {}
    out["migrationId"] = value["migration_id"]
    import capo_s3tables.types.migration_state

    out["state"] = capo_s3tables.types.migration_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> StartTableMigrationResponse:
    out: StartTableMigrationResponse = {}  # type: ignore[typeddict-item]
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
    return out
