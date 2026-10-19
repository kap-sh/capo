"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DatabaseMigrationPreference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhubstrategy.errors import DeserializationError, SerializationError
from capo_migrationhubstrategy.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.heterogeneous
    import capo_migrationhubstrategy.types.homogeneous
    import capo_migrationhubstrategy.types.no_database_migration_preference


class _DatabaseMigrationPreference_heterogeneous(TypedDict, closed=True):
    heterogeneous: "capo_migrationhubstrategy.types.heterogeneous.Heterogeneous"


class _DatabaseMigrationPreference_homogeneous(TypedDict, closed=True):
    homogeneous: "capo_migrationhubstrategy.types.homogeneous.Homogeneous"


class _DatabaseMigrationPreference_noPreference(TypedDict, closed=True):
    noPreference: "capo_migrationhubstrategy.types.no_database_migration_preference.NoDatabaseMigrationPreference"


DatabaseMigrationPreference: TypeAlias = (
    _DatabaseMigrationPreference_heterogeneous
    | _DatabaseMigrationPreference_homogeneous
    | _DatabaseMigrationPreference_noPreference
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseMigrationPreference) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DatabaseMigrationPreference: cannot serialize unknown variant {value.name!r}"
        )
    elif "heterogeneous" in value:
        import capo_migrationhubstrategy.types.heterogeneous

        return {
            "heterogeneous": capo_migrationhubstrategy.types.heterogeneous.serialize_json(
                value["heterogeneous"]
            )
        }
    elif "homogeneous" in value:
        import capo_migrationhubstrategy.types.homogeneous

        return {
            "homogeneous": capo_migrationhubstrategy.types.homogeneous.serialize_json(
                value["homogeneous"]
            )
        }
    elif "noPreference" in value:
        import capo_migrationhubstrategy.types.no_database_migration_preference

        return {
            "noPreference": capo_migrationhubstrategy.types.no_database_migration_preference.serialize_json(
                value["noPreference"]
            )
        }
    else:
        raise SerializationError("DatabaseMigrationPreference: no variant present")


def deserialize_json(data: dict) -> DatabaseMigrationPreference:
    if data.get("heterogeneous") is not None:
        import capo_migrationhubstrategy.types.heterogeneous

        return {
            "heterogeneous": capo_migrationhubstrategy.types.heterogeneous.deserialize_json(
                data["heterogeneous"]
            )
        }
    elif data.get("homogeneous") is not None:
        import capo_migrationhubstrategy.types.homogeneous

        return {
            "homogeneous": capo_migrationhubstrategy.types.homogeneous.deserialize_json(
                data["homogeneous"]
            )
        }
    elif data.get("noPreference") is not None:
        import capo_migrationhubstrategy.types.no_database_migration_preference

        return {
            "noPreference": capo_migrationhubstrategy.types.no_database_migration_preference.deserialize_json(
                data["noPreference"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DatabaseMigrationPreference: no recognized variant key"
        )
