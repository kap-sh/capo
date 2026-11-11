"""Generated from Smithy shape ``com.amazonaws.athena#SystemTableStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.system_table_status

SystemTableStatusList: TypeAlias = list[
    "capo_athena.types.system_table_status.SystemTableStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTableStatusList) -> list:
    import capo_athena.types.system_table_status

    out: list = []
    for item in value:
        out.append(capo_athena.types.system_table_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SystemTableStatusList:
    import capo_athena.types.system_table_status

    out: SystemTableStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_athena.types.system_table_status.deserialize_aws_json_1_1(item))
    return out
