"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_summary

AutonomousDatabaseList: TypeAlias = list[
    "capo_odb.types.autonomous_database_summary.AutonomousDatabaseSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseList) -> list:
    import capo_odb.types.autonomous_database_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.autonomous_database_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabaseList:
    import capo_odb.types.autonomous_database_summary

    out: AutonomousDatabaseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.autonomous_database_summary.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: AutonomousDatabaseList) -> list[Any]:
    import capo_odb.types.autonomous_database_summary

    return [
        capo_odb.types.autonomous_database_summary.redact_sensitive(item)
        for item in value
    ]
