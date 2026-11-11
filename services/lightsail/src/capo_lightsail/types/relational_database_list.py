"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database

RelationalDatabaseList: TypeAlias = list[
    "capo_lightsail.types.relational_database.RelationalDatabase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseList) -> list:
    import capo_lightsail.types.relational_database

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.relational_database.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseList:
    import capo_lightsail.types.relational_database

    out: RelationalDatabaseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lightsail.types.relational_database.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: RelationalDatabaseList) -> list[Any]:
    import capo_lightsail.types.relational_database

    return [
        capo_lightsail.types.relational_database.redact_sensitive(item)
        for item in value
    ]
