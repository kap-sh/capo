"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)
from capo_database_migration_service.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_database_migration_service.types.default_error_details


class ErrorDetailsDefaultErrorDetailsMember(TypedDict, closed=True):
    defaultErrorDetails: "capo_database_migration_service.types.default_error_details.DefaultErrorDetails"


ErrorDetails: TypeAlias = ErrorDetailsDefaultErrorDetailsMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ErrorDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "defaultErrorDetails" in value:
        import capo_database_migration_service.types.default_error_details

        return {
            "defaultErrorDetails": capo_database_migration_service.types.default_error_details.serialize_aws_json_1_1(
                value["defaultErrorDetails"]
            )
        }
    else:
        raise SerializationError("ErrorDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ErrorDetails:
    if data.get("defaultErrorDetails") is not None:
        import capo_database_migration_service.types.default_error_details

        return {
            "defaultErrorDetails": capo_database_migration_service.types.default_error_details.deserialize_aws_json_1_1(
                data["defaultErrorDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ErrorDetails: no recognized variant key")
