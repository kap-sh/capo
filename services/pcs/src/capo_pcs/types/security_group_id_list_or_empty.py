"""Generated from Smithy shape ``com.amazonaws.pcs#SecurityGroupIdListOrEmpty``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.security_group_id

SecurityGroupIdListOrEmpty: TypeAlias = list[
    "capo_pcs.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupIdListOrEmpty) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupIdListOrEmpty:
    return [item for item in data if item is not None]
