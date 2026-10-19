"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#NoDatabaseMigrationPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.target_database_engines


class NoDatabaseMigrationPreference(TypedDict, closed=True):
    target_database_engine: (
        "capo_migrationhubstrategy.types.target_database_engines.TargetDatabaseEngines"
    )
    """<p> The target database engine for database migration preference that you specify. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoDatabaseMigrationPreference) -> dict:
    out: dict = {}
    import capo_migrationhubstrategy.types.target_database_engines

    out["targetDatabaseEngine"] = (
        capo_migrationhubstrategy.types.target_database_engines.serialize_json(
            value["target_database_engine"]
        )
    )
    return out


def deserialize_json(data: dict) -> NoDatabaseMigrationPreference:
    out: NoDatabaseMigrationPreference = {}  # type: ignore[typeddict-item]
    if data.get("targetDatabaseEngine") is not None:
        import capo_migrationhubstrategy.types.target_database_engines

        out["target_database_engine"] = (
            capo_migrationhubstrategy.types.target_database_engines.deserialize_json(
                data["targetDatabaseEngine"]
            )
        )
    else:
        out["target_database_engine"] = []
    return out
