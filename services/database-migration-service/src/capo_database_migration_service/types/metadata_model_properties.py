"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MetadataModelProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)
from capo_database_migration_service.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_database_migration_service.types.statement_properties


class _MetadataModelProperties_StatementProperties(TypedDict, closed=True):
    StatementProperties: (
        "capo_database_migration_service.types.statement_properties.StatementProperties"
    )


MetadataModelProperties: TypeAlias = (
    _MetadataModelProperties_StatementProperties | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataModelProperties) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MetadataModelProperties: cannot serialize unknown variant {value.name!r}"
        )
    elif "StatementProperties" in value:
        import capo_database_migration_service.types.statement_properties

        return {
            "StatementProperties": capo_database_migration_service.types.statement_properties.serialize_aws_json_1_1(
                value["StatementProperties"]
            )
        }
    else:
        raise SerializationError("MetadataModelProperties: no variant present")


def deserialize_aws_json_1_1(data: dict) -> MetadataModelProperties:
    if data.get("StatementProperties") is not None:
        import capo_database_migration_service.types.statement_properties

        return {
            "StatementProperties": capo_database_migration_service.types.statement_properties.deserialize_aws_json_1_1(
                data["StatementProperties"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MetadataModelProperties: no recognized variant key")
