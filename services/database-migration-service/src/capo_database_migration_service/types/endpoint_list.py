"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EndpointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint

EndpointList: TypeAlias = list[
    "capo_database_migration_service.types.endpoint.Endpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointList) -> list:
    import capo_database_migration_service.types.endpoint

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.endpoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointList:
    import capo_database_migration_service.types.endpoint

    out: EndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_database_migration_service.types.endpoint.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: EndpointList) -> list[Any]:
    import capo_database_migration_service.types.endpoint

    return [
        capo_database_migration_service.types.endpoint.redact_sensitive(item)
        for item in value
    ]
